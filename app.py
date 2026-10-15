from flask import Flask, render_template, session, redirect, request
from services.roast import generate_roast
from google_auth_oauthlib.flow import Flow

import os
from dotenv import load_dotenv

load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

GOOGLE_CLIENT_CONFIG = {
    "web": {
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "redirect_uris": ["http://localhost:5000/callback"]
    }
}

app = Flask(__name__, template_folder='templates')
app.secret_key = os.getenv("FLASK_SECRET_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    flow = Flow.from_client_config(GOOGLE_CLIENT_CONFIG, scopes=SCOPES)
    flow.redirect_uri = "http://localhost:5000/callback"

    authorization_url, state = flow.authorization_url(
        access_type = "offline",
        include_granted_scopes = "true"
    )

    session["oauth_state"] = state

    return redirect(authorization_url)


@app.route('/callback')
def callback():
    if request.args.get("state") != session.get("oauth_state"):
        return "Invalid OAuth state", 400

    flow = Flow.from_client_config(GOOGLE_CLIENT_CONFIG, scopes=SCOPES, state=session["oauth_state"])
    flow.redirect_uri = "http://localhost:5000/callback"
    flow.fetch_token(authorization_response=request.url)

    credentials = flow.credentials

    return "Google authentication successful!"

@app.route('/roast')
def roast():
    test_data = {
        "subscriptions": ["MrBeast", "Gordon Ramsay", "Lofi Girl", "Minecraft Let's Plays"],
        "liked_videos": [
            "10 Hour Rain Sounds",
            "How to Become a Millionaire by 25",
            "Cat Falls Off Couch Compilation",
        ],
        "playlists": ["Gym Motivation", "Study Music", "Watch Later (2,347 videos)"],
    }

    roast_text = generate_roast(test_data)
    return render_template('roast.html', roast=roast_text)

app.run()