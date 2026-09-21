mensagem = input("Insira a mensagem cifrada: ").strip()
crib = input("Insira o crib: ").strip()

total_posicoes = 0
for i in range(len(mensagem) - len(crib) + 1):
    valido = True
    for j in range(len(crib)):
        if crib[j] == mensagem[i + j]:
            valido = False
            break
    if valido:
        total_posicoes += 1

print(total_posicoes)