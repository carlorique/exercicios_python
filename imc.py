pes = float(input("Digite o seu peso:"))
alt = float(input("Digite sua altura:"))

imc = pes / (alt ** 2)

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obeso")