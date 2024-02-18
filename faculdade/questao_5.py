# CARLOS HENRIQUE TORRES MARINHO

# 5. Elabore um programa para ler o código de um banco e mostrar o nome, conforme a tabela abaixo:

# Código Banco
# [1] Banco do Brasil
# [33] Santander
# [104] Caixa Econômica Federal
# [237] Bradesco
# [Qualquer outro código] Banco não identificado

banco = int(input("Digite o codigo do banco: "))

if banco == 1:
    print("Banco do Brasil")
elif banco == 33:
    print("Santander")
elif banco == 104:
    print("Caixa Econômica Federal")
elif banco == 237:
    print("Bradesco")
else:
    print("Banco não identificado")

