from functions import minmax, find_minmax, process_matrix
import numpy as np

def main_menu():
    while True:
        print("\nМеню:")
        print("1. Завдання 1: Знайти мінімум і максимум з чотирьох чисел")
        print("2. Завдання 2: Периметр і площа трикутників")
        print("3. Вихід")
        
        choice = input("Оберіть опцію (1-3): ")
        
        if choice == "1":
            # Завдання 1
            def process_minmax(data):
                """
                Функція для пошуку мінімального і максимального значень серед чотирьох чисел.
                
                Args:
                    data (list): Список чисел [A, B, C, D].
                
                Returns:
                    tuple: Мінімальне та максимальне значення.
                """
                A, B, C, D = data
                A, B = minmax(A, B)
                C, D = minmax(C, D)
                A, C = minmax(A, C)
                B, D = minmax(B, D)
                return A, D  # Мінімальне і максимальне значення

            def main_minmax():
                """
                Основна функція для введення даних, виклику minmax і виведення результату.
                """
                data = list(map(float, input("Введіть чотири числа через пробіл (A B C D): ").split()))
                if len(data) != 4:
                    print("Помилка: потрібно ввести рівно чотири числа!")
                    return
                
                minimum, maximum = process_minmax(data)
                print(f"Мінімальне значення: {minimum}")
                print(f"Максимальне значення: {maximum}")

            main_minmax()

        elif choice == "2":
            
            def process_matrix():
                """
                Зовнішня функція без параметрів, яка викликає внутрішню функцію для обробки матриці.
                """
                def inner_function(file_name):
                    
                    # Внутрішня функція для обробки двовимірної матриці.
                    
                    
                    # Зчитування матриці з текстового файлу
                    matrix = np.loadtxt(file_name, delimiter=' ')
                    
                    # Обчислення суми та добутку елементів кожного стовпця
                    column_sums = matrix.sum(axis=0)
                    column_products = matrix.prod(axis=0)
                    
                    # Генерація матриці такого ж розміру з випадковими числами
                    random_matrix = np.random.randint(1, 10, size=matrix.shape)
                    
                    # Сума початкової матриці з випадковою
                    transformed_matrix = matrix + random_matrix
                    
                    return (column_sums, column_products), transformed_matrix

                # Введення імені файлу та виклик внутрішньої функції
                file_name = input("Введіть ім'я файлу з матрицею .txt: ")
                try:
                    (column_sums, column_products), transformed_matrix = inner_function(file_name)
                    
                    # Вивід результатів
                    print("Сума елементів кожного стовпця:", column_sums)
                    print("Добуток елементів кожного стовпця:", column_products)
                    print("Сума початкової матриці з випадковою:\n", transformed_matrix)
                except FileNotFoundError:
                    print("Файл не знайдено. Будь ласка, перевірте ім'я файлу.")
                except ValueError:
                    print("Файл має неправильний формат або не містить числових даних.")

            # Виклик зовнішньої функції
            process_matrix()
        
        elif choice == "3":
            print("Вихід з програми.")
            break
        
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main_menu()
