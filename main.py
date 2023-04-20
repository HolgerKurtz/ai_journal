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
    beethoven_prompt = f"You are BeethovenGPT. You come up with new letters from Ludwig van Beethoven. You write in the style of Beethoven himself but you add what he might have thought about new and upcoming artists from today. Here are some real letters from him as a reference:\n{choose_letters(number=6)}"
    text = TextGen(prompt=beethoven_prompt)
    # print(text.__dict__)
    new_ai_text = text.create_text(tokens=500)
    # print(new_ai_text)
    print("1. Text wurde erstellt.")
    print("2. E-Mail wird erstellt.")
    n = Newsletter(ai_text=new_ai_text)
    r = n.send(n.create_id()) # real
    # n.send_test(n.create_id()) # test
    print("3. E-Mail versandt")

if __name__ == "__main__":
    wd = get_weekday()
    if wd == 3: # mittwoch
        send()
    else:
        send()
