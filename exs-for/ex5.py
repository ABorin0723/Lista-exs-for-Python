# 5 
# Crie um programa que permita que o usuário crie sua lista de compras.
# Primeiramente, solicite que ele informe quantos produtos serão adicionados na lista.
# Depois disto, peça para que o usuário digite os produtos que ele vai comprar, e
# armazene em uma lista. Ao final, imprima a lista de compras do usuário.

numList = int(input("Qual a quantidade de itens? "))
list = ""

if numList <= 0:
    print("Erro, a lista não pode ser negativa ou igual a zero.")
else:
    for i in range(numList):
        item = input("Qual o item? ")
        list += "\n" + item

    print("A lista é: \n" + list)