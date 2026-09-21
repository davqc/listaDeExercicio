import sys

for linha in sys.stdin:
    linha = linha.strip()
    if linha == "":
        continue
    n = int(linha)
    if n == 0:
        print("Vai ter copa!")
    else:
        print("Vai ter duas!")