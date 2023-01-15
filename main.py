from sendinblue import Newsletter
from update_prompt import get_news_from_nyt, new_prompt
from ai import TextGen
from choose_random_letters import choose_letters
from datetime import datetime, date


def get_weekday():
    # get current datetime
    dt = datetime.now()
    # get day of week as an integer
    week_day = dt.weekday()
    return week_day

def send():
    abstract = get_news_from_nyt(0, "home").get("abstract")
    ai_prompt = new_prompt(abstract, date.today())
    text = TextGen(prompt=ai_prompt)
    print(text.__dict__)
    new_ai_text = text.create_text(tokens=500)
    print(new_ai_text)

    n = Newsletter(ai_text=new_ai_text)
    r = n.send(n.create_id())

if __name__ == "__main__":
    wd = get_weekday()
    if wd == 3:
        print("mittwoch")
        send()
    else:
        send()
