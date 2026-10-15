import os, json
from dotenv import load_dotenv
from flask import Flask, render_template, session, redirect, request, url_for
from services.roast import generate_roast
from google.oauth2.credentials import Credentials

from services.auth import get_authorization_url, get_credentials
from services.youtube import create_yt_clinet, get_user_data

load_dotenv()

app = Flask(__name__, template_folder='templates')
app.secret_key = os.getenv("FLASK_SECRET_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    auth_url, state, code_verifer = get_authorization_url()
    session["code_verifer"] = code_verifer
    session["oauth_state"] = state
    return redirect(auth_url)

@app.route('/callback')
def callback():
    if request.args.get("state") != session["oauth_state"]:
        return "Invalid OAuth state", 400
    
    redirect_uri = "http://localhost:5000/callback"
    credentials = get_credentials(redirect_uri, request.url, session["code_verifer"])

    session["credentials"] = credentials.to_json()
    session.pop("oauth_state", None)

    return redirect(url_for("roast"))

@app.route('/roast')
def roast():
    credentials_json = session.get("credentials")

    if not credentials_json:
        return redirect(url_for("login"))

    credentials_info = json.loads(credentials_json)

    credentials = Credentials.from_authorized_user_info(credentials_info)

    youtube = create_yt_clinet(credentials)
    data = get_user_data(youtube)
    roast_text = generate_roast(data)

    return render_template("roast.html", roast = roast_text)

if __name__ == '__main__':
    app.run()