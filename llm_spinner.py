import os
import google.generativeai as genai
from google.generativeai import types

#Set up Gemini API key
os.environ["GEMINI_API_KEY"] = "AIzaSyCa0so4Fz28UXLsM3OQa7bD2B4h_m30nYs"

def spin_chapter_with_gemini(text):
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])

    model = genai.GenerativeModel("gemma-3n-e2b-it")
    response = model.generate_content(
        f"You are an AI writer.Spin the text for a modern reader:\n\n{text}"
    )

    return response.text

if __name__ == "__main__":
    with open("chapter1.txt", "r", encoding="utf-8") as f:
        original = f.read()

    spun = spin_chapter_with_gemini(original)

    with open("spun_chapter.txt", "w", encoding="utf-8") as f:
        f.write(spun)
