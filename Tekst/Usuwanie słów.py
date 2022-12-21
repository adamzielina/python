import re
from pathlib import Path

if __name__ == "__main__":
    path = Path(r'C:\Users\Adam\OneDrive\Dokumenty\txt.txt')
    list = ['sie', 'i', 'oraz', 'nigdy', 'dlaczego']


    f = open(path, "r")
    inp = f.read()
    inp = inp.split()
    out = [item for item in inp if item not in list]
    out = " ".join(out)
    f = open(path, "w")
    f.write(out)