# GETS DATE
# GETS NYTIMES API NEWS ARTICLE
# OPENS PROMPT FILE
# REPLACES VALUES AND RETURNS NEW PROMPT (DOESNT CHANGE .txt)

from datetime import date
import os
from dotenv import load_dotenv
import requests
load_dotenv()


API_KEY = os.getenv("NYT_API_KEY")
PROMPT_FILE = "ai_prompt.txt"
PLACEHOLDER = dict(date="{date}",headline="{headline}")

def get_news_from_nyt(number, section="home"):
    NYT_SECTIONS = ["home", "arts", "books", "business", "fashion", "home", "politics", "sports", "technology", "theater", "world"]

    # check if section is valid
    if section in NYT_SECTIONS:
        pass
    else:
        section = "home" # default

    TOP_STORY_HOMEPAGE_URL = f"https://api.nytimes.com/svc/topstories/v2/{section}.json?api-key={API_KEY}"
    response = requests.get(TOP_STORY_HOMEPAGE_URL, headers={"Accept": "application/json"})
    data = response.json()
    nyt_headline = data['results'][number] # first --> 0
    return nyt_headline


def new_prompt(headline, date):
    with open(PROMPT_FILE, "r") as f:
        old_prompt = f.read()
    
    new_prompt = old_prompt.replace(PLACEHOLDER.get("date"), str(date)).replace(PLACEHOLDER.get("headline"), headline)
    return new_prompt

if __name__ == "__main__":
    h = get_news_from_nyt(0, "home").get("abstract")
    n = new_prompt(h, date.today())
    print(n)