Subcriptions().list(...) retrun:

{
    "kind": "youtube#subscriptionListResponse",
    "etag": "some-etag-value",
    "nextPageToken": "CAUQAA",
    "pageInfo": {
        "totalResults": 120,
        "resultsPerPage": 50
    },
    "items": [
        {
            "kind": "youtube#subscription",
            "snippet": {
                "publishedAt": "2024-05-12T10:30:00Z",
                "title": "Example Anime Channel",
                "description": "Anime rankings and analysis",
                "resourceId": {
                    "kind": "youtube#channel",
                    "channelId": "UCxxxxxxxx"
                }
            }
        },
        {
            "kind": "youtube#subscription",
            "snippet": {
                "publishedAt": "2023-11-20T08:15:00Z",
                "title": "Python Tutorials",
                "description": "Learn Python programming",
                "resourceId": {
                    "kind": "youtube#channel",
                    "channelId": "UCyyyyyyyy"
                }
            }
        }
    ]
}


Liked videos data:

{
    "kind": "youtube#videoListResponse",
    "etag": "some-etag-value",
    "nextPageToken": "CAUQAA",
    "pageInfo": {
        "totalResults": 75,
        "resultsPerPage": 50
    },
    "items": [
        {
            "kind": "youtube#video",
            "etag": "some-video-etag",
            "id": "abc123",
            "snippet": {
                "publishedAt": "2025-03-10T12:00:00Z",
                "channelId": "UCxxxxxxxx",
                "title": "How to Build a Game in Python",
                "description": "A beginner tutorial...",
                "channelTitle": "Example Coding Channel",
                "tags": ["Python", "Game Development"],
                "categoryId": "27"
            }
        },
        {
            "kind": "youtube#video",
            "etag": "another-video-etag",
            "id": "xyz789",
            "snippet": {
                "publishedAt": "2025-02-15T09:00:00Z",
                "channelId": "UCyyyyyyyy",
                "title": "Why Is Space So Strange?",
                "description": "Exploring the mysteries of the universe...",
                "channelTitle": "Example Science Channel",
                "tags": ["Space", "Science"],
                "categoryId": "28"
            }
        }
    ]
}