from sendinblue import Newsletter
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
    # abstract = get_news_from_nyt(0, "home").get("abstract")
    # ai_prompt = new_prompt(abstract, date.today())
    beethoven_prompt = "Write a letter from Ludwig van Beethoven. Be specific and detail oriented:\n" + choose_letters(number=6)

    text = TextGen(prompt=beethoven_prompt)
    print(text.__dict__)
    new_ai_text = text.create_text(tokens=500)
    print(new_ai_text)

    n = Newsletter(ai_text=new_ai_text)
    r = n.send(n.create_id()) # n.send_test(n.create_id())

if __name__ == "__main__":
    wd = get_weekday()
    if wd == 3: # mittwoch
        send()
