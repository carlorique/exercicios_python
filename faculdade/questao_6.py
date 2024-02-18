# CARLOS HENRIQUE TORRES MARINHO

# 6. Faça um programa que leia o ano de nascimento de uma pessoa, calcule e mostre sua 
# idade em relação ao ano corrente (2023) e, também, verifique e mostre se a ela já tem idade para votar 
# e para tirar a carteira de habilitação.

ano_nascimento = int(input("Digite o ano do seu nascimento: "))

idade = 2023 - ano_nascimento

print("Sua idade é:", idade)

if idade >= 18:
    print("Você ja tem idade pra votar!")
    print("Voce ja tem idade pra tirar habilitação!")
else:
    print("Você nao tem idade pra votar!")
    print("Você nao tem idade pra tirar habilitação!")