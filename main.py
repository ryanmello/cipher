import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
        
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", type=str)
    parser.add_argument("--verbose", "-v", action="store_true")
    
    args = parser.parse_args()
    
    print(f"Prompt: {args.prompt}")
    print(f"Verbose: {args.verbose}")
    
    prompt = args.prompt
    
    messgaes = [
        types.Content(role="user", parts=[types.Part(text=prompt)])
    ]

    client = genai.Client(api_key=api_key)

    res = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messgaes
    )
    
    if args.verbose:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {res.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {res.usage_metadata.candidates_token_count}")

    print(res.text)

if __name__ == "__main__":
    main()
    