import os, argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import SYSTEM_PROMPT
from available_funcs import available_functions, call_function

def main():
    print("Hello from AiAgent!")
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key == None:
        raise RuntimeError("api_key == None")

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User Prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    client = genai.Client(api_key = api_key)
    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = messages,
        config = types.GenerateContentConfig(
            tools = [available_functions],
            system_instruction = SYSTEM_PROMPT
        )
    )
    

    if response.usage_metadata == None:
        raise Exception("Exception: response has usage_metadata = None")
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    if response.function_calls != None:
        function_results = []
        for function_call in response.function_calls:

            function_call_result = call_function(function_call, args.verbose)
            if len(function_call_result.parts) == 0:
                raise Exception("Error: Empty function_call_result.parts")
            if function_call_result.parts[0].function_response == None:
                raise Exception("Error: function_call_result.parts[0].function_response == None")
            if function_call_result.parts[0].function_response.response == None:
                raise Exception("Error: function_call_result.parts[0].function_response.response == None")
            if args.verbose:
                print(f"-> {function_call_result.parts[0].function_response.response['result']}")
        
            function_results.append(function_call_result.parts[0])
    else:
        print(f"Response: {response.text}")
    
        





if __name__ == "__main__":
    main()




