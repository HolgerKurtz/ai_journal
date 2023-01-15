# BEETHOVEN DATA AS TXT to JSON like openai needs

import json

BEETHOVEN_TXT = "beethoven-letters.txt"

with open(BEETHOVEN_TXT, "r") as b:
    beethoven_text = b.read()

each_letter = beethoven_text.split("---")
prompts = []
for letter in each_letter:
    part = letter.split("\n\n")
    p = f"Write a letter from Ludwig van Beethoven {part[0]}"
    if "TO" in p:
        cleaned_prompt = p.replace("\n", "")
        c = part[1:]
        comp = "\n".join(c)
        cleaned_c = f" {comp}\n---" # recommendation by openai
        structured =dict(prompt=cleaned_prompt, completion=cleaned_c)
        prompts.append(structured)
    else:
        pass

with open ("fine_tune.json", "w+") as json_file:
    for p in prompts:
        line = json.dumps(p)
        json_file.write(line+"\n")