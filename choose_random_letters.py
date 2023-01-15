"""
1. Opens the complete letter text file
2. Choose 10 random letters
3. Returns them as a complete prompt to openai
"""
import random

BEETHOVEN_TXT = "beethoven-letters.txt"

def choose_letters(path_to_file=BEETHOVEN_TXT, number=10):
    list_of_prompts = []
    
    with open(path_to_file, "r") as b:
        beethoven_text = b.read()
    
    each_letter = beethoven_text.split("---")
    for letter in each_letter:
        PROMPT = ""
        parts = letter.split("\n\n")
        anrede = parts[0]
        if "TO" in anrede:
            PROMPT +=anrede + "\n"
            PROMPT += " ".join(parts[1:])
            PROMPT += "\n---\n"
            list_of_prompts.append(PROMPT)
        else:
            pass
    
    random_letters = random.sample(list_of_prompts, number)
    random_letters_combined = " ".join(random_letters)
    return random_letters_combined


if __name__ == "__main__":
    prompt = choose_letters()

