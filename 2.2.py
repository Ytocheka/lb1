import random

numbers = [random.randint(-5, 5) for _ in range(10)]
print("Исходный список:", numbers)

even_numbers = [num for num in numbers if num % 2 == 0]
print("Чётные элементы:", even_numbers)

max_num = numbers[0]
min_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
print("Максимальное число:", max_num)
print("Минимальное число:", min_num)

user_numbers = []
print("\nВведите 5 чисел:")
for _ in range(5):
    val = int(input())
    user_numbers.append(val)
user_numbers.sort()
print("Отсортированный список:", user_numbers)

unique_list = []
for element in numbers:
    if element not in unique_list:
        unique_list.append(element)
print("\nСписок без дубликатов:", unique_list)
print("Исходный список:", numbers)
if len(numbers) > 1:
    numbers[0], numbers[-1] = numbers[-1], numbers[0]
print("Список после замены первого и последнего элементов:", numbers)
