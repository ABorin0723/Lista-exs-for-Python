# 8
# Crie um programa que separa o joio do trigo. Seu programa deve ler a lista
# abaixo e criar duas listas diferentes: uma com todas as ocorrências da palavra "joio" e
# outra com todas as ocorrências da palavra "trigo". Ao final, imprima as listas separadas.
# Copie e cole a linha abaixo no seu código e complete o programa:

joioETrigo = ["joio", "trigo", "trigo", "joio", "trigo",
"joio", "joio", "joio", "joio", "trigo", "trigo", "joio",
"joio", "joio", "trigo", "trigo", "trigo", "trigo", "trigo",
"trigo", "trigo", "trigo", "trigo", "trigo", "trigo",
"joio", "joio", "joio", "joio", "joio", "joio", "joio",
"joio", "trigo", "trigo", "joio", "joio", "joio", "joio",
"joio", "joio", "joio", "joio", "joio", "joio", "joio",
"joio", "joio", "joio", "joio", "joio", "trigo", "trigo",
"trigo", "trigo", "trigo", "trigo", "trigo", "trigo",
"trigo", "trigo", "trigo", "trigo", "trigo", "trigo",
"trigo", "trigo", "trigo", "trigo", "joio", "joio", "joio",
"joio", "joio", "joio", "joio", "joio", "joio", "joio",
"trigo", "trigo", "trigo", "trigo", "trigo", "trigo",
"trigo", "trigo", "trigo", "joio", "joio", "joio", "joio",
"joio", "joio", "trigo", "joio", "joio", "joio", "joio",
"joio", "trigo", "trigo", "trigo", "trigo", "joio", "joio",
"joio", "joio", "joio", "joio", "joio", "trigo", "trigo",
"trigo", "joio", "trigo", "joio", "joio", "joio"]

joio = []
Trigo = []

for i in joioETrigo:
    if i == "joio":
        joio.append(i)
for i in joioETrigo:
    if i == "trigo":
        Trigo.append(i)

print(joio)
print(Trigo)