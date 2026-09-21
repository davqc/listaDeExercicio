alcool = 0
gasolina = 0
diesel = 0

print("Álcool: 1 / Gasolina: 2 / Diesel: 3 / Encerrar: 4")

while True:
    x = int(input("Input: "))
    if x == 4:
        break
    elif x == 1:
        alcool += 1
    elif x == 2:
        gasolina += 1
    elif x == 3:
        diesel += 1
    # códigos fora de 1-4 são simplesmente ignorados (novo código é lido)

print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")