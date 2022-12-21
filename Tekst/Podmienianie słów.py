import re
from pathlib import Path

if __name__ == "__main__":

    path = Path(r'C:\Users\Adam\OneDrive\Dokumenty\txt2.txt')
    replace_words = {
        'i': 'oraz',
        'oraz': 'i',
        'nigdy': 'prawie nigdy',
        'dlaczego': 'czemu'
    }

    f = open(path, "r")
    inp = f.read()

    out = []
    for item in inp.split():
        if item in replace_words.keys():
            out.append(replace_words[item])
        else:
            out.append(item)

    out = " ".join(out)

    f = open(path, "w")
    f.write(out)