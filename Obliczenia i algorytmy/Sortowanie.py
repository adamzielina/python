import random

if __name__ == '__main__':

    array = []
    for i in range(50):
        array.append(random.randint(1,30))
    print(array)

    for i in range(1, len(array)):
        element  = array[i]
        j = i - 1
        while j >= 0 and element > array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = element
    print(array)