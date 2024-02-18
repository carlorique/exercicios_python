# CARLOS HENRIQUE TORRES MARINHO

# 1. Elabore um programa que calcule o que deve ser pago por um produto, considerando o preço
# normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir
# para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.

# Código Condição de Pagamento
# 1 À vista em dinheiro ou cheque, recebe 10% de desconto
# 2 À vista no cartão de crédito, recebe 15% de desconto
# 3 Em duas vezes, preço normal de etiqueta sem juros
# 4 Em duas vezes, preço normal de etiqueta mais juros de 10%

valor_produto = float(input("Digite o valor do produto: R$ "))

print("[1] À vista em dinheiro ou cheque, recebe 10% de desconto")
print("[2] À vista no cartão de crédito, recebe 15% de desconto")
print("[3] Em duas vezes, preço normal de etiqueta sem juros")
print("[4] Em duas vezes, preço normal de etiqueta mais juros de 10%")

codigo_pagamento = int(input("Digite o codigo do pagamento: "))

if codigo_pagamento == 1:
    total_pagar = valor_produto * 0.9
elif codigo_pagamento == 2:
    total_pagar = valor_produto * 0.85
elif codigo_pagamento == 3:
    total_pagar = valor_produto / 2
    print("2x de:", round(total_pagar, 2))
elif codigo_pagamento == 4:
    total_pagar = valor_produto / 2 * 1.1
    print("2x de:", round(total_pagar, 2))
else:
    print("Código inválido!")
    exit()

print(f"Valor a pagar: R$ {total_pagar:.2f}")
