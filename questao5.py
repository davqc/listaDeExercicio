input1 = int(input("Insira o número de funcionários do primeiro andar: "))
input2 = int(input("Insira o número de funcionários do segundo andar: "))
input3 = int(input("Insira o número de funcionários do terceiro andar: "))

pos1 = input1 * 0 + input2 * 1 + input3 * 2
pos2 = input1 * 1 + input2 * 0 + input3 * 1
pos3 = input1 * 2 + input2 * 1 + input3 * 0

menor = pos1
andar = 1

if pos2 < menor:
    menor = pos2
    andar = 2

if pos3 < menor:
    menor = pos3
    andar = 3

print(f"Para essa situação, o {andar}° andar é o mais óptimo.")
print("tempo andado:", menor * 2)