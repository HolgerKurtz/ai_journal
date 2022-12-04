import os
import requests
import ai
from dotenv import load_dotenv
load_dotenv()


def open_html(filepath):
    with open(filepath, 'r') as file:
        html_as_string = file.read()
    return html_as_string

class Newsletter:
    """
    PLACEHOLDER
    """
    def __init__(self, ai_text=None):
        self.ai_text = open_html('mail.html').replace("{{AI_TEXT}}", ai_text)
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "api-key" : os.getenv("SENDINBLUE_API")
        }
        self.payload = {
            "tag": "Newsletter",
            "sender": {
                "name": "Holger",
                "email": "hk@holgerkurtz.de"
            },
            "name": "Newsletter - HEUTE",
            "htmlContent": self.ai_text,
            "subject": "Message from an AI",
            "replyTo": "hk@holgerkurtz.de",
            "toField": "{FNAME} {LNAME}",
            "recipients": {
                "listIds": [2]
            },
            "inlineImageActivation": True,
            "mirrorActive": True,
            "footer": "[DEFAULT_FOOTER]",
            "header": "[DEFAULT_HEADER]",
            "utmCampaign": "NL_05_2017",
            "params": {
                "FNAME": "Joe",
                "LNAME": "Doe",
                "AINAME": "HILDE"
            }
        }

    def create_id(self):
        url = "https://api.sendinblue.com/v3/emailCampaigns"
        response = requests.post(url, json=self.payload, headers=self.headers)
        print(response.json())
        return response.json().get('id')

    def send(self, campaign_id=14):
        url = f"https://api.sendinblue.com/v3/emailCampaigns/{campaign_id}/sendNow" # sendTest
        response = requests.post(url, headers=self.headers)
        return response


if __name__ == "__main__":
    text = ai.TextGen(prompt="This is a fictional story about Joe. Joe is stranded on an empty island and thinks about his life. He speaks about himself.\n I remember the day I got my apartment in New York.")
    new_ai_text = text.create_text()
    
    with open("ai_text.txt", 'a+') as file:
        file.write(new_ai_text)
    
    with open("ai_text.txt", 'r') as file:
        ai_text = file.read()
    
    n = Newsletter(ai_text=ai_text)
    _id = n.create_id()
    print(_id)
    r = n.send(_id)
    print(r)