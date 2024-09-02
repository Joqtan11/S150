import re
from pdfminer.high_level import extract_pages, extract_text

page = 13
text = extract_text("Ejemplo.pdf", page_numbers=[page])
text = re.sub("\s", "", text)
pattern = re.compile(r"[0-9][0-9]-[0-9][0-9]")
matches = pattern.findall(text)

if range(len(matches)) == range(0, 0):
    pattern = re.compile(r"[0-9][-][0-9][0-9][D][E]")
    matches = pattern.findall(text)

    if range(len(matches)) == range(0, 0):
        pattern = re.compile(r"[0-9]-[0-9][D][E]")
        matches = pattern.findall(text)
        if range(len(matches)) == range(0, 0):
            pattern = re.compile(r"[0-9][0-9][D][E]")
            info = matches[0]
            if (int(info) - 1) == page:
                print("none")
            else:
                print(info)
        else:
            info = re.sub("-[0-9][D][E]", "", matches[0])
            print(info)
    else:
        info = re.sub("\s", "", matches[0])
        info = re.sub("-[0-9][0-9][DE]", "", info)
        print()
elif range(len(matches)) == (0, 1):
    info = re.sub("\s", "", matches[0])
    info = re.sub("-[-0-9][0-9][DE]", "", info)
    print(info)
else:
    info = re.sub("-[-0-9][0-9]", "", matches[0])
    print(info)

    # \s[0-9]\s[a-zA-Z]\s[a-zA-Z]
