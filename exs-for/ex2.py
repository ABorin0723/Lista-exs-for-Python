# 2
# Crie um programa que imprime na tela todos os valores entre dois valores digitados pelo teclado.

val1 = int(input("Primeiro valor "))
val2 = int(input("Segundo valor "))

if val1 < val2:
    menor = val1
    maior = val2
else:
    menor = val2
    maior = val1

for x in range(menor,maior):
    print(x)