a = int(input("Insira o primeiro valor: "))
b = int(input("Insira o segundo valor: "))
c = int(input("Insira o terceiro valor: "))

valores = [a, b, c]
ordenados = sorted(valores)

startA, startB, startC = a, b, c

print("Valores ordenados:")

for i in ordenados:
    print(i)


print("Valores enviados:")

print(startA)
print(startB)
print(startC)