n = int(input("Введіть розмірність матриці (NxN). (Наприклад: 2): "))

matrix = []
for i in range(n):
    row = input(f"Введіть {n} цілих чисел для {i+1}-го рядку, розділені пробілами. (Наприклад: 4 6): ").split()
    row = [int(x) for x in row]
    matrix.append(row)

def average(row):
    return sum(row) / len(row)

sorted_matrix = sorted(matrix, key=average)

print("Матриця яку ви ввели:")
for row in matrix:
    print(row)

print("Посортована матриця:")
for row in sorted_matrix:
    print(row, "-", (sum(row) / len(row)) )