import os
import requests
import ai
from dotenv import load_dotenv
load_dotenv()


def open_file(filepath):
    with open(filepath, 'r') as file:
        html_as_string = file.read()
    return str(html_as_string)

class Newsletter:
    def __init__(self, ai_text=None):
        self.ai_text = open_file('mail.txt').replace("{{AI_TEXT}}", ai_text.replace("\n", "<br />"))
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
            "subject": "📧 A Letter From Beethoven",
            "replyTo": "hk@holgerkurtz.de",
            "toField": "{FNAME}",
            "recipients": {
                "listIds": [2]
            },
            "inlineImageActivation": True,
            "mirrorActive": True,
            "footer": "[DEFAULT_FOOTER]",
            "header": "[DEFAULT_HEADER]",
            "params": {
                "FNAME": "{{contact.VORNAME}}",
                "AINAME": "HILDE"
            }
        }

    def create_id(self):
        url = "https://api.sendinblue.com/v3/emailCampaigns"
        response = requests.post(url, json=self.payload, headers=self.headers)
        return response.json().get('id')

    def send(self, campaign_id=14):
        url = f"https://api.sendinblue.com/v3/emailCampaigns/{campaign_id}/sendNow"
        response = requests.post(url, headers=self.headers)
        print(response.text)
        return response
    
    def send_test(self, campaign_id=14):
        url = f"https://api.sendinblue.com/v3/emailCampaigns/{campaign_id}/sendTest"
        payload = {"emailTo": ["hk@holgerkurtz.de"]} # only for 
        response = requests.post(url, headers=self.headers, json=payload)
        print(response.text)
        return response

if __name__ == "__main__":
    ai_prompt = open_file("ai_prompt.txt")

    text = ai.TextGen(prompt=ai_prompt)
    new_ai_text = text.create_text()

    with open("ai_prompt.txt", 'a+') as file:
        file.write(new_ai_text)
    
    n = Newsletter(ai_text=new_ai_text)
    r = n.send(n.create_id())