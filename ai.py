import os
import logging
import openai
from dotenv import load_dotenv

# load environment variables
load_dotenv()

logging.basicConfig(
    filename="gpt-3_newsletter.log",
    filemode="a",
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG,
)
logger = logging.getLogger(__name__)


class TextGen:
    openai.api_key = os.getenv("OPENAI_API_KEY")

    def __init__(self,prompt=None, variable=None):
        self.prompt = prompt
        self.variable = variable

    def create_text(self):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=self.prompt,
            temperature=0.5,
            max_tokens=50,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )

        # print the first response
        ai_response = response.choices[0].text
        logging.info(ai_response)
        return ai_response


if __name__ == "__main__":
    text = TextGen(prompt="This is a fictional story about Joe. Joe is stranded on an empty island and thinks about his life. He speaks about himself.\n I remember the day I got my apartment in New York. I")
    ai_text = text.create_text()
    print(ai_text)
