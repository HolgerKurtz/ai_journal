from sendinblue import Newsletter, open_file
from ai import TextGen

from datetime import datetime


def get_weekday():
    # get current datetime
    dt = datetime.now()
    # get day of week as an integer
    week_day = dt.weekday()
    return week_day

def send(prompt_file=None):
    ai_prompt = open_file(prompt_file)
    text = TextGen(prompt=ai_prompt)
    print(text.__dict__)
    new_ai_text = text.create_text(tokens=500)
    print(new_ai_text)

    with open(prompt_file, 'w+') as file:
        file.write(new_ai_text)

    n = Newsletter(ai_text=new_ai_text)
    r = n.send(n.create_id())

if __name__ == "__main__":
    wd = get_weekday()
    if wd == 2:
        print("Mittwoch")
        # send(prompt_file="ai_prompt.txt")
