from pathlib import Path

if __name__ == "__main__":
    for item in Path(r'C:\Users\Adam\Desktop').glob('*'):
        if item.is_file():
            print(str(item))