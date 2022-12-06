from sendinblue import Newsletter, open_file
from ai import TextGen

ai_prompt = open_file("ai_prompt.txt")
text = TextGen(prompt=ai_prompt)
print(text.__dict__)
new_ai_text = text.create_text(tokens=500)
print(new_ai_text)

with open("ai_prompt.txt", 'a+') as file:
    file.write(new_ai_text)

# n = Newsletter(ai_text=new_ai_text)
# r = n.send(n.create_id())
