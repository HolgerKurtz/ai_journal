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
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=self.prompt,
            temperature=0.3,
            max_tokens=tokens,
            top_p=1,
            frequency_penalty=0.8,
            presence_penalty=0.7,
            stop="---"
        )

        # print the first response
        ai_response = response.choices[0].text
        print(response)
        return ai_response


if __name__ == "__main__":
    from choose_random_letters import choose_letters
    beethoven_prompt = "Write a letter from Ludwig van Beethoven. Be specific and detail oriented:\n" + choose_letters(number=6)
    text = TextGen(prompt=beethoven_prompt)
    ai_text = text.create_text()
    print(ai_text)
