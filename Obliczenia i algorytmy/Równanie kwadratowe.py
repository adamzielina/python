import cmath

if __name__ == '__main__':
    print('podaj a')
    a = int(input())
    print('podaj b')
    b = int(input())
    print('podaj c')
    c = int(input())

    delta = (b ** 2) - (4 * a * c)
    x1 = (-b + cmath.sqrt(delta)) / (2 * a)
    x2 = (-b - cmath.sqrt(delta)) / (2 * a)

    print(x1," ", x2)