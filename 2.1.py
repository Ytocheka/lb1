print("Таблица умножения:")
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i*j:3}", end="\t")
    print()

sum_odd = 0
for num in range(1, 101, 2):
    sum_odd += num
print("\nСумма всех нечётных чисел от 1 до 100:", sum_odd)


n = int(input("\nВведите число для поиска делителей: "))
print(f"Делители числа {n}:")
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")
print()


fact_n = int(input("\nВведите число для вычисления факториала: "))
factorial = 1
for i in range(1, fact_n + 1):
    factorial *= i
print(f"Факториал числа {fact_n} равен {factorial}")


fib_len = int(input("\nВведите длину последовательности Фибоначчи: "))
fib_sequence = []
a, b = 0, 1
for _ in range(fib_len):
    fib_sequence.append(a)
    a, b = b, a + b
print("Последовательность Фибоначчи:", fib_sequence)
