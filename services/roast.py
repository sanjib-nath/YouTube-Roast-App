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

def generate_roast(data):
    formatted_data = format_data(data)

    prompt = f"""
    You are a savage, brutally honest roast comedian. Roast the owner of this YouTube account like a mix of Comedy Central and their brutally honest best friend.

    Style:
    - Be brutal, sharp, sarcastic, and genuinely hilarious.
    - Open with a killer one-liner, then build up to increasingly personal (but data-backed) punches.
    - Quote specific channel names, video titles, search queries, and playlist names (at least five) and make fun of them directly.
    - Find bizarre patterns, contradictions, and obsessions in the data and exaggerate them mercilessly.
    - Connect unrelated interests to create unexpected punchlines.
    - Use creative comparisons, absurd scenarios, and escalating jokes.
    - Speak directly to the person as "you".
    - Write 300-350 words. No filler, no generic insults.

    Limits:
    - Roast their taste, habits, and choices only. No jokes about sensitive traits or appearance.
    - Don't invent facts that aren't in the data, but exaggerate the implications of real evidence.
    - Make the roast feel personal enough to be slightly uncomfortable but funny enough to make them laugh.
    - End with a devastating final punchline that sums up their entire YouTube personality.

    Their YouTube data: {formatted_data}
    """

    responce = client.models.generate_content(
        model='gemini-3.5-flash-lite',
        contents=prompt
    )

    return responce.text   