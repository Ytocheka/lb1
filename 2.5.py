import random

nums = [random.randint(1, 50) for _ in range(20)]
unique_nums = list(set(nums))
print("Список из 20 чисел:", nums)
print("Уникальные значения:", unique_nums)

count_dict = {}
for num in nums:
    count_dict[num] = count_dict.get(num, 0) + 1
print("Количество повторений чисел:", count_dict)

words = ["Яблоко", "Банан", "Груша", "соль", "Виноград"]
long_words_set = {word for word in words if len(word) > 5}
print("Слова длиной больше 5 символов:", long_words_set)

sentence = input("Введите предложение: ")
words_in_sentence = sentence.split()
word_count = {}
for w in words_in_sentence:
    w_lower = w.lower()
    word_count[w_lower] = word_count.get(w_lower, 0) + 1
print("Количество вхождений слов:", word_count)

# 5. Создать список чисел, преобразовать его в множество и обратно в список (удалить дубликаты)
numbers_list = [11, 2, 33, 1, 4, 2, 5, 6, 3]
unique_numbers_list = list(set(numbers_list))
print("Изначальный список:", numbers_list)
print("Список без дубликатов:", unique_numbers_list)

products = {"яблоко": 100, "банан": 300, "апельсин": 80, "манго": 600}
most_expensive = max(products, key=products.get)
print(f"Самый дорогой товар: {most_expensive} с ценой {products[most_expensive]}")


names = ["Лера", "Иван", "Антон", "Лера", "Иван"]
name_counts = {}
for name in names:
    name_counts[name] = name_counts.get(name, 0) + 1
duplicates = [name for name, count in name_counts.items() if count > 1]
most_common_name = max(name_counts, key=name_counts.get)
print("Имена, встречающиеся более одного раза:", duplicates)
print("Имя, встречающееся чаще всего:", most_common_name)

user_string = input("Введите строку: ")
char_index = {}
for idx, char in enumerate(user_string):
    if char not in char_index:
        char_index[char] = idx
print("Словарь символ → первый индекс вхождения:", char_index)
