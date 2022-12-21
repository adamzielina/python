import numpy as np

if __name__ == '__main__':
    matrix = np.random.rand(8, 8)
    det = np.linalg.det(matrix)
    print(det)