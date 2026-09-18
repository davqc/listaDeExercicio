x = int(input())

print("Lista de valores ímpares:")

for i in range(1, x + 1):
    if i % 2 != 0:
        print(i)