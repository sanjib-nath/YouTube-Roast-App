from googleapiclient.discovery import build

def create_yt_clinet(credentials):
    youtube = build("youtube", "v3", credentials=credentials)
    return youtube

def get_subscriptions(youtube):
    subcriptions = []
    next_page_token = None

    while True:
        response = youtube.subscriptions().list(
            part="snippet",
            mine=True,
            maxResults=50,
            pageToken = next_page_token
        ).execute()

        for item in response['items']:
            subcriptions.append(item["snippet"]["title"])

        next_page_token = response.get("nextPageToken")

        if not next_page_token: 
            break

    return subcriptions

def get_liked_videos(youtube):
    liked_videos = []
    next_page_token = None

    while True:
        response = youtube.videos().list(
            part="snippet",
            myRating="like",
            maxResults=50,
            pageToken = next_page_token
        ).execute()
    
        for item in response['items']:
            title = item["snippet"]["title"]
            channel = item["snippet"]["channelTitle"]

            liked_videos.append({
                "Title": title,
                "Channel": channel
                })
    
        next_page_token = response.get("nextPageToken")
    
        if not next_page_token: 
            break

    return liked_videos

def get_playlists(youtube):
    playlists = []
    next_page_token = None

    while True:
        response = youtube.playlists().list(
            part="snippet",
            mine=True,
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        for item in response.get("items", []):
            snippet = item["snippet"]

            playlists.append({
                "title": snippet["title"],
                "description": snippet.get("description", "")
            })

        next_page_token = response.get("nextPageToken")

        if not next_page_token:
            break

    return playlists

def get_user_data(youtube):
    subs = get_subscriptions(youtube)
    likes = get_liked_videos(youtube)
    playlist = get_playlists(youtube)

    data = {
        "subscriptions": subs,
        "Liked_Video": likes,
        "playlist": playlist
    }

    return data
