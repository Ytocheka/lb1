students = {
    "Лера": 91,
    "Иван": 77,
    "Антон": 92
}
average_score = sum(students.values()) / len(students)
print(f"Средний балл студентов: {average_score:.2f}")

text = input("\nВведите строку для подсчёта букв: ")
letter_count = {}
for char in text:
    if char.isalpha():  # считать только буквы
        char = char.lower()  # игнорируем регистр
        letter_count[char] = letter_count.get(char, 0) + 1
print("Количество каждой буквы:")
for letter, count in letter_count.items():
    print(f"{letter}: {count}")

squares = {i: i**2 for i in range(1, 11)}
print("\nСловарь с числами и их квадратами:", squares)


keys = ['a', 'b', 'z', 'd']
values = [1, 2, 3, 4]
dict_from_lists = {}
for i in range(min(len(keys), len(values))):
    dict_from_lists[keys[i]] = values[i]
print("Словарь из двух списков:", dict_from_lists)