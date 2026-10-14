from flask import Flask, render_template
from services.roast import generate_roast

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

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