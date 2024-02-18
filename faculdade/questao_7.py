# CARLOS HENRIQUE TORRES MARINHO

# 7. A Alíquota do cálculo mensal do imposto de renda 2023 é baseada na tabela abaixo:

# Base de Cálculo (Salário em R$) | Alíquota (%)
# Até R$ 1.903,98 | 0,0
# De R$ 1.903,99 a R$ 2.826,65 | 7,5
# De R$ 2.826,66 a R$ 3.751,05 | 15,0
# De R$ 3.751,06 a R$ 4.664,68 | 22,5
# Acima de R$ 4.664,68 | 27,5

#Crie um algoritmo para ler o salário, calcular a alíquota e mostrar o valor do Imposto de 
#Renda mensal

salario = float(input("Digite o salário: "))

if salario <= 1903.98:
    aliquota = 0.0
elif salario <= 2826.65:
    aliquota = 7.5
elif salario <= 3751.05:
    aliquota = 15.0
elif salario <= 4664.68:
    aliquota = 22.5
else:
    aliquota = 27.5
    
imposto_renda_calculado = salario * (aliquota / 100)
salario_liquido_calculado = salario - imposto_renda_calculado

print(f"O Imposto de Renda mensal a ser pago é: R$ {imposto_renda_calculado:.2f}")
print(f"Salário líquido após desconto do Imposto de Renda: R$ {salario_liquido_calculado:.2f}")
