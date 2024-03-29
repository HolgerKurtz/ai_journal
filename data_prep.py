B_FILE = "beethoven-letters_raw.txt"
B_FILE_prepped = "beethoven-letters_clean.txt"

list_of_newlines = []

with open(B_FILE, "r+") as b_file:
    numbers_replaced = 0
    for line in b_file:
        t = line.replace(".","").replace("[1]", "")
        try:
            if int(t) < 1000: # to include dates
                list_of_newlines.append("---\n")
                numbers_replaced +=1
            else:
                pass
        except:
            if "[Footnote" in line: # not needed
                pass
            elif "[1]" in line: # not needed
                no_footnote = line.replace("[1]", "")
                list_of_newlines.append(no_footnote)
            elif "[picture of music]" in line: # not needed
                pass
            elif not bool(line.strip()):
                pass
            elif "TO" in line:
                line = line.replace("\n","")
                h1 = f"<h1>{line}</h1>\n"
                list_of_newlines.append(h1)
            elif "beethoven" in line.lower():
                line = line.replace("\n","")
                h2 = f"<h2>{line}</h2>\n"
                list_of_newlines.append(h2)
            else:
                list_of_newlines.append(line)
    print(f"Zeilen = {len(list_of_newlines)}")
    print(f"Nummern ersetzt = {numbers_replaced}")

with open(B_FILE_prepped, "w") as b:
    new = "".join(list_of_newlines)
    b.write(new)
