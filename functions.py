import numpy as np
import math

# Завдання 1: Функція Minmax
def minmax(x, y):
    """
    Функція знаходить мінімум і максимум з двох чисел.
    Параметри:
        x (float): перше число (вхід/вихід).
        y (float): друге число (вхід/вихід).
    """
    if x > y:
        x, y = y, x
    return x, y

# Завдання 1: Функція для знаходження мінімуму та максимуму з чотирьох чисел
def find_minmax(a, b, c, d):
    """
    Використовуючи чотири виклики minmax, знаходить мінімум і максимум з чотирьох чисел.
    """
    a, b = minmax(a, b)
    c, d = minmax(c, d)
    a, c = minmax(a, c)
    b, d = minmax(b, d)
    return a, d  # Мінімум і максимум

# Завдання 2: Функція TrianglePS
def triangle_ps(a):
    """
    Обчислює периметр і площу рівностороннього трикутника.
    Параметри:
        a (float): сторона трикутника.
    Повертає:
        P (float): периметр.
        S (float): площа.
    """
    P = 3 * a
    S = (a**2 * math.sqrt(3)) / 4
    return P, S

# Завдання 2: Обробка матриць
def process_matrix(filename):
    """
    Зчитує матрицю з файлу, обчислює її параметри та перетворює.
    Параметри:
        filename (str): ім'я файлу з даними.
    Повертає:
        params (dict): параметри матриці.
        transformed_matrix (ndarray): перетворена матриця.
    """
    # Зчитування матриці з файлу
    matrix = np.loadtxt(filename, delimiter=",")
    
    # Обчислення параметрів
    params = {
        "sum": np.sum(matrix),
        "mean": np.mean(matrix),
        "min": np.min(matrix),
        "max": np.max(matrix)
    }
    
    # Перетворення матриці (транспонування)
    transformed_matrix = matrix.T
    
    return params, transformed_matrix
