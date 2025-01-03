import sys
from pathlib import Path
from openai import OpenAI
from IPython.display import display, Markdown

def get_api_key():
    """Retrieve the OpenAI API key from a hidden file."""
    home_dir = Path.home()
    key_file = home_dir / ".secrets" / "openai_api_key.txt"

    if not key_file.exists():
        raise FileNotFoundError(
            f"API Key file not found at {key_file}. "
            "Please ensure the key is saved correctly."
        )

    with key_file.open("r") as f:
        api_key = f.read().strip()

    if not api_key:
        raise ValueError("API Key file is empty. Provide a valid API key.")

    return api_key


class ChatGPTAnalyzer:
    def __init__(self, yaml_content):
        """Initialize the analyzer with YAML content."""
        try:
            self.api_key = get_api_key()
            print("OpenAI API Key retrieved successfully.")
        except (FileNotFoundError, ValueError) as e:
            print(e)
            sys.exit(1)  # Exit with an error code

        self.yaml_content = yaml_content
        self.messages = [
            {
                "role": "system",
                "content": "You are an expert in analyzing YAML files for system design.",
            }
        ]

    def _construct_prompt(self, user_prompt):
        """Construct the full prompt with YAML content."""
        return f"""
The following is a YAML file describing a system design component in Capella:
---
{self.yaml_content}
---

{user_prompt}
"""

    def add_prompt(self, user_prompt):
        """Add a user prompt to the conversation."""
        prompt = self._construct_prompt(user_prompt)
        self.messages.append({"role": "user", "content": prompt})

    def get_response(self):
        """Send messages to ChatGPT and get a response."""
        try:
            client = OpenAI(
            api_key=self.api_key,  # This is the default and can be omitted
            )
            response = client.chat.completions.create(
                messages=self.messages,
                model="gpt-4o",
            )
            assistant_message =  response.choices[0].message.content
            self.messages.append({"role": "assistant", "content": assistant_message})
            return assistant_message
            
        except Exception as e:
            return f"Error communicating with OpenAI API: {e}"


def interactive_chat(analyzer):
    """Interactive chat loop."""
    while True:
        user_prompt = input("Enter your prompt (or type 'exit' to quit): ")
        if user_prompt.lower() == "exit":
            print("Exiting...")
            break

        analyzer.add_prompt(user_prompt)
        response = analyzer.get_response()
        display(Markdown(f"**Your Prompt:**\n\n{user_prompt}\n"))
        display(Markdown(f"**ChatGPT Response:**\n\n{response}\n"))
