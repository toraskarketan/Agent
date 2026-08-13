import os
import sys
from google import genai
from google.genai import types

def create_coding_agent():
    # Ensure API key is configured
    if not os.environ.get("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY environment variable is not set.")
        print("Please export GEMINI_API_KEY='your_key_here' before running.")
        sys.exit(1)

    # Initialize the Google GenAI Client
    client = genai.Client()

    # System instruction guiding the model's persona and architecture role
    system_instruction = (
        "You are an expert AI Software Engineer and Technical Architect assistant. "
        "Your role is to help write, debug, refactor, and structure Python and software projects. "
        "When requested, generate complete, clean, documented, and modular code. "
        "When executing math or algorithmic validation, use the built-in code execution tool."
    )

    # Enable native code execution tool
    config = types.GenerateContentConfig(
        system_instruction=system_instruction,
        temperature=0.2,  # Low temperature for precise code generation
        tools=[types.Tool(code_execution=types.ToolCodeExecution())]
    )

    # Create a persistent chat session using Gemini 2.5 Flash
    chat = client.chats.create(
        model="gemini-3.5-flash",
        config=config
    )

    print("=" * 60)
    print("🤖 AI Coding & Project Assistant Initialized")
    print("Type 'exit' or 'quit' to end the session.")
    print("=" * 60 + "\n")

    while True:
        try:
            user_input = input("\n👤 You: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit"]:
                print("Exiting session. Happy coding!")
                break

            print("\n🤖 Assistant is thinking...\n")
            
            # Send message to the agent chat session
            response = chat.send_message(user_input)

            # Display agent response
            print("🤖 Agent:")
            print(response.text)

        except KeyboardInterrupt:
            print("\nSession interrupted. Exiting...")
            break
        except Exception as e:
            print(f"\n❌ Error encountered: {e}")

if __name__ == "__main__":
    create_coding_agent()