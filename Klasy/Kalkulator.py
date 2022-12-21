from Liczby_zespolone import Complex
if __name__ == '__main__':

    while True:
        print("podaj realis liczby zespolonej 1")
        real = int(input())
        print("podaj imaginaris liczby zespolonej 1")
        imag = complex(input())
        compl1 = Complex(real,imag)
        print("podaj realis liczby zespolonej 1")
        real = int(input())
        print("podaj imaginaris liczby zespolonej 1")
        imag = complex(input())
        compl2 = Complex(real,imag)

        print("podaj dzialanie + - * /")
        znak = input()
        match znak:
            case '+':
                print(compl1+compl2)
            case '-':
                print(compl1-compl2)
            case '*':
                print(compl1*compl2)
            case '/':
                print(compl1/compl2)
            case _:
                print("zly symbol")