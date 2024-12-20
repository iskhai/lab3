from functions import minmax, find_minmax, triangle_ps, process_matrix

def main_menu():
    while True:
        print("\nМеню:")
        print("1. Завдання 1: Знайти мінімум і максимум з чотирьох чисел")
        print("2. Завдання 2: Периметр і площа трикутників")
        print("3. Завдання 2: Обробка матриці з файлу")
        print("4. Вихід")
        
        choice = input("Оберіть опцію (1-4): ")
        
        if choice == "1":
            # Завдання 1
            print("Введіть чотири числа:")
            a = float(input("A: "))
            b = float(input("B: "))
            c = float(input("C: "))
            d = float(input("D: "))
            min_val, max_val = find_minmax(a, b, c, d)
            print(f"Мінімум: {min_val}, Максимум: {max_val}")
        
        elif choice == "2":
            # Завдання 2.1
            print("Введіть три сторони трикутників:")
            for i in range(1, 4):
                a = float(input(f"Сторона трикутника {i}: "))
                P, S = triangle_ps(a)
                print(f"Трикутник {i}: Периметр = {P}, Площа = {S}")
        
        elif choice == "3":
            # Завдання 2.2
            filename = input("Введіть ім'я файлу з матрицею: ")
            params, transformed_matrix = process_matrix(filename)
            print("Параметри матриці: ")
            for key, value in params.items():
                print(f"{key.capitalize()}: ",value)
            print("Перетворена матриця: ")
            print(transformed_matrix)
        
        elif choice == "4":
            print("Вихід з програми.")
            break
        
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main_menu()
