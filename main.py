import os
import sys
from dotenv import load_dotenv
from google import genai

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if len(sys.argv) < 2:
        print("I need a prompt")
        sys.exit(1)
    
    prompt = sys.argv[1]
    print(f"Prompt: {prompt}")

    client = genai.Client(api_key=api_key)

    res = client.models.generate_content(
        model="gemini-2.0-flash-001", contents=prompt
    )

    print(res.text)

if __name__ == "__main__":
    main()
    