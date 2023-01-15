# BEETHOVEN DATA AS TXT to JSON like openai needs

import json

BEETHOVEN_TXT = "beethoven-letters_clean.txt"

with open(BEETHOVEN_TXT, "r") as b:
    beethoven_text = b.read()

each_letter = beethoven_text.split("\n---\n")
print(f"Anzahl der Briefe: {len(each_letter)}")
prompts = []
print(each_letter[1])
for letter in each_letter:
    part = letter.split("\n")
    p = f"Write a letter from Ludwig van Beethoven {part[0]}"
    if "TO" in p:
        c = part[1:]
        comp = "\n".join(c)
        cleaned_c = f" {comp}\n---" # recommendation by openai
        structured =dict(prompt=p, completion=cleaned_c)
        prompts.append(structured)
    else:
        pass

with open ("fine_tune.json", "w+") as json_file:
    for p in prompts:
        line = json.dumps(p)
        json_file.write(line+"\n")