set1 = {1, 6, 3, 4, 5}
set2 = {4, 5, 9, 7, 8}

intersection = set1 & set2  # пересечение
union = set1 | set2         # объединение

print("Пересечение множеств:", intersection)
print("Объединение множеств:", union)


text = input("\nВведите текст: ")
words = text.split()
unique_words = set(words)
print("Уникальные слова:", unique_words)

list1 = [1, 9, 3, 4, 5]
list2 = [4, 5, 6, 7]

common_elements = set(list1) & set(list2)
print("\nОбщие элементы в списках:", common_elements)

a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

print("\nМножество a подмножество b?", a.issubset(b))
print("Множество b подмножество a?", b.issubset(a))

# 5. Удалить из множества все элементы, которые меньше заданного числа
set_values = {11, 15, 2, 33, 7, 15}
threshold = int(input("\nВведите пороговое число: "))

filtered_set = {x for x in set_values if x >= threshold}
print("Множество после удаления элементов меньше порога:", filtered_set)
