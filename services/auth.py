import os
from dotenv import load_dotenv
from google_auth_oauthlib.flow import Flow

load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

GOOGLE_CLIENT_CONFIG = {
    "web": {
        "client_id": os.getenv("GOOGLE_CLIENT_ID"),
        "client_secret": os.getenv("GOOGLE_CLIENT_SECRET"),
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "redirect_uris": ["http://localhost:5000/callback"]
    }
}

def create_oauth_flow(state=None):
    flow = Flow.from_client_config(GOOGLE_CLIENT_CONFIG, scopes=SCOPES, state=state)
    flow.redirect_uri = "http://localhost:5000/callback"
    return flow

def get_authorization_url():
    flow = create_oauth_flow()
    auth_url, state = flow.authorization_url(
        access_type = "offline",
        include_granted_scopes = "true"
    )

    return auth_url, state

def get_credentials(redirect_url, callback_url):
    flow = create_oauth_flow()
    flow.redirect_uri = redirect_url
    flow.fetch_token(authorization_response = callback_url)

    return flow.credentials