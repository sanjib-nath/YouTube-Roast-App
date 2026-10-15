import os
from dotenv import load_dotenv
from flask import Flask, render_template, session, redirect, request
from services.roast import generate_roast

from services.auth import get_authorization_url, get_credentials

load_dotenv()

app = Flask(__name__, template_folder='templates')
app.secret_key = os.getenv("FLASK_SECRET_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    auth_url, state = get_authorization_url()
    session["oauth_state"] = state
    return redirect(auth_url)

@app.route('/callback')
def callback():
    if request.args.get("state") != session["oauth_state"]:
        return "Invalid OAuth state", 400
    
    redirect_uri = "http://localhost:5000/callback"
    get_credentials(redirect_uri, request.url)
    
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

if __name__ == '__main__':
    app.run()