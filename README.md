🔥 YouTube Roast

Your YouTube activity says a lot about you. Let's make fun of it.

YouTube Roast is an AI-powered web application that analyzes available YouTube account data and generates personalized, humorous roasts using Google's Gemini API.

Connect your YouTube account, choose your language, and let AI judge your viewing habits. 

✨ Features

- 🔐 Google OAuth 2.0 — Authenticate with your Google account and authorize read-only access to YouTube data.
- 📊 YouTube Data Integration — Retrieve available account data through the YouTube Data API v3.
- 🤖 AI-Powered Roasting — Generate personalized roasts using Google's Gemini API.
- 🌐 English and Hindi — Choose the language of your roast.
- 🎭 Interactive Web Interface — A simple interface built to make the experience entertaining.

🛠️ Tech Stack

|Technology| Purpose|
|---|---|
|Python| Backend logic|
|Flask| Web application framework|
|Google OAuth 2.0| Authentication and authorization|
|YouTube Data API v3| Accessing YouTube account data|
|Google Gemini API| Generating AI-powered roasts|
|HTML and CSS| Web interface and styling|
|Gunicorn| Production WSGI server|
|Railway| Application deployment|
|Git and GitHub| Version control and source code hosting|

📁 Project Structure

```text
YouTube-Roast-App/
├── app.py
├── services/
│   ├── auth.py
│   ├── youtube.py
│   └── roast.py
├── templates/
│   ├── base.html
│   ├── index.html
│   └── roast.html
└── static/
    └── style.css
```

⚙️ How It Works

1. The user opens the web application and selects a roast language.
2. Google OAuth 2.0 handles authentication and requests permission to access YouTube data.
3. The application exchanges the authorization response for credentials.
4. The YouTube service retrieves the available data permitted by the granted scope.
5. The data is passed to Google's Gemini API to generate a personalized roast.
6. Flask renders the generated roast on the results page.

🚀 Deployment

The application is deployed on Railway and connected to its GitHub repository.

Production deployment uses Gunicorn to serve the Flask application.

gunicorn app:app --bind 0.0.0.0:$PORT

Deployment process

1. Push application changes to the GitHub repository.
2. Allow Railway to build and deploy the updated commit.
3. Configure the required environment variables in Railway.
4. Configure the production OAuth redirect URI in Google Cloud Console.
5. Test the deployed application, including the Google login callback and roast-generation flow.

Environment variables

The application uses environment variables for API credentials and application configuration.

GEMINI_API_KEY=your_gemini_api_key
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
FLASK_SECRET_KEY=your_flask_secret_key

These values must be configured locally or in the deployment environment. Never commit actual API keys, client secrets, or ".env" files to a public repository.

🧠 Challenges & Lessons Learned

Building YouTube Roast involved more than writing the application code. Getting it to work in a production environment introduced several practical debugging challenges.

1. Deploying Flask to Railway

Getting the application to run locally was only part of the process. The production environment required the correct server configuration and startup command.

What I learned:

- The difference between local development and production deployment.
- Why a production WSGI server such as Gunicorn is used to serve Flask applications.
- How environment configuration affects a deployed application.

2. Debugging Google OAuth 2.0

OAuth integration was one of the most challenging parts of the project. I encountered redirect URI mismatches and callback errors while configuring Google authentication for the production domain.

I had to check redirect URI consistency, investigate the deployed configuration, and inspect Railway logs to identify the actual cause of errors.

What I learned:

- How the OAuth authorization and callback flow works.
- Why redirect URIs must match the registered configuration.
- How to distinguish authentication configuration errors from callback-processing errors.
- Why production HTTPS handling matters when working with OAuth libraries.

3. Managing Environment Variables

The application depends on external services, each requiring its own configuration and credentials. Missing environment variables caused deployment issues that did not necessarily appear during local development.

What I learned:

- How to configure environment variables locally and on Railway.
- Why secrets should be kept outside source code.
- How to diagnose configuration-related failures in production.

4. Debugging with Deployment Logs

Some errors appeared only after deploying the application. Repeatedly changing settings was not enough; I needed to inspect the actual traceback and determine where the application was failing.

What I learned:

- How to use deployment logs to locate Python exceptions.
- Why reading a traceback is more effective than guessing at a fix.
- How to trace errors across Flask routes, service modules, and external libraries.
- Why confirming the deployed Git commit matters when a fix appears not to take effect.

5. Integrating External APIs

The project combines Google authentication, the YouTube Data API, and the Gemini API. Each service has its own configuration, credentials, and behavior.

What I learned:

- How different APIs fit together in a web application.
- How OAuth credentials are used to make authorized API requests.
- How to organize API-related logic into separate service modules.

🔒 Security Considerations

- Use the minimum OAuth permissions required by the application.
- Store API keys and client secrets in environment variables.
- Keep ".env" out of version control.
- Protect OAuth tokens and user data from unauthorized access.
- Review Google's OAuth verification requirements before making the application available to the general public.

⚠️ Disclaimer

YouTube Roast is an independent entertainment project and is not affiliated with or endorsed by Google or YouTube.

The generated roasts are AI-generated humor and may not accurately reflect a user's interests or personality.

👨‍💻 Author: Sanjib Nath

Built as a hands-on project to explore Python web development, API integration, OAuth authentication, AI-powered features, and production deployment.
