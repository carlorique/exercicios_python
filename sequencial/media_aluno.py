nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
limite_aprovacao = 7.0

media = (nota1 + nota2 + nota3) / 3

print(f"Sua média foi: {media:.1f}")

if media >= limite_aprovacao:
    print("O aluno está aprovado!")
else:
    print("O aluno está reprovado.")
