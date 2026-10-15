import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def format_data(data):
    lines = []

    for category, items in data.items():
        label = category.replace("_", " ").title()
        lines.append(f"{label}:")

        for item in items:
            if isinstance(item, dict):
                details = ", ".join( f"{key}: {value}" for key, value in item.items())
                lines.append(f"- {details}")
            else:
                lines.append(f"- {item}")

        lines.append("")

    return "\n".join(lines)

def generate_roast(data, language="English"):
    formatted_data = format_data(data)

    
    prompt = f"""
        You are an exceptionally funny roast comedian with the observational
        humor of a brutally honest best friend. Your job is to roast this
        person based on their REAL YouTube data.

        ROAST LANGUAGE: {language}

        Write the entire roast in the selected language.
        If Hindi is selected, use natural, casual Hindi with a little
        Hinglish where it makes jokes funnier. Avoid formal textbook Hindi.

        YOUR COMEDY STYLE:
        - Be witty, savage, unpredictable, and genuinely funny.
        - Make the person laugh AND feel personally exposed.
        - Roast like a friend who has known them for years.
        - Use sarcasm, absurd comparisons, irony, exaggeration, and callbacks.
        - Never sound like a generic AI writing an essay.

        HOW TO FIND THE FUNNIEST ROASTS:
        1. Find contradictions between their subscriptions, liked videos,
        and playlists.
        2. Identify suspiciously specific interests and bizarre combinations.
        3. Find evidence of procrastination, unrealistic ambitions,
        abandoned interests, or questionable taste IF the data supports it.
        4. Turn ordinary details into unexpectedly hilarious observations.
        5. Connect unrelated pieces of data into one memorable punchline.
        6. If a video title is embarrassing or bizarre, quote it and explain
        exactly why it is funny in this context.

        COMEDY RULES:
        - Start with your FUNNIEST punchline. No introductions.
        - Every paragraph must contain a joke, a clever observation,
        or an escalating punchline.
        - Prefer a few devastating, specific jokes over dozens of weak insults.
        - Use actual channel names, video titles, and playlist names.
        - Make jokes about the implications of the data, not just the names.
        - Use callbacks: bring an earlier joke back later in a funnier way.
        - End with the strongest punchline of the entire roast.
        - Never explain why a joke is funny.
        - Never praise the person or add motivational advice.
        - Do not repeat the same joke in different words.
        - Aim for 250–350 words, but NEVER add filler to reach the length.

        IMPORTANT:
        - Only use evidence present in the supplied data.
        - Never claim to know their personality, intentions, or real-life
        habits with certainty. Frame these as comedic observations.
        - Do not invent searches, watch history, or videos they did not like.
        - Roast their entertainment choices and digital habits, not
        sensitive personal characteristics.
        - If the data is ordinary, find creative angles rather than
        inventing embarrassing details.

        THEIR YOUTUBE DATA:
        {formatted_data}

        Now deliver a roast that feels frighteningly specific,
        hilarious, and impossible to confuse with a generic AI response.
        Remember: the selected language is {language}.
        """


    responce = client.models.generate_content(
        model='gemini-3.5-flash-lite',
        contents=prompt
    )

    return responce.text   