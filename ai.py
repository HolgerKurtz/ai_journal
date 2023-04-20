import os
import openai
from dotenv import load_dotenv

# load environment variables
load_dotenv()


class TextGen:
    openai.api_key = os.getenv("OPENAI_API_KEY")

    def __init__(self,prompt=None, variable=None):
        self.prompt = prompt
        self.variable = variable

    def create_text(self, tokens=256):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                    {"role": "user", "content": self.prompt}
                ]
            )
        # print the first response
        ai_response = response['choices'][0]['message']['content']
        print(response)
        return ai_response


if __name__ == "__main__":
    from choose_random_letters import choose_letters
    beethoven_prompt = f"You are BeethovenGPT. You come up with new letters from Ludwig van Beethoven. You write in the style of Beethoven himself and you keep the given formatting. Here are some real letters from him as a reference:\n{choose_letters(number=6)}"
    text = TextGen(prompt=beethoven_prompt)
    ai_text = text.create_text()
    print(ai_text)
