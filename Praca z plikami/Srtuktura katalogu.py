from pathlib import Path

if __name__ == "__main__":
    for item in Path(r'C:\Users\Adam\Desktop').rglob('*'):
        if item.is_file():
            print(str(item))
        elif item.is_dir():
            print(str(item))