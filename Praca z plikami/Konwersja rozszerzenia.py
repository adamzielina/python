from PIL import Image

if __name__ == "__main__":
    image = Image.open(r'C:\Users\Adam\Desktop\jpg.jpg')
    image.save(r'C:\Users\Adam\Desktop\png.png')