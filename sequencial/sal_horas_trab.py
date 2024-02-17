#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input("Digite a o valor que voce ganha por hora: "))
horas_trabalhadas = float(input("Digite o numero de horas trabalhadas no mes: "))

salario_mensal = valor_hora * horas_trabalhadas

print(f"seu salario é: R${salario_mensal:.2f}")