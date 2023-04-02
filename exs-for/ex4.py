import unicodedata

# 4
# Sabendo que uma string é uma lista de letras, peça para o usuário digitar um texto e imprima na tela a quantidade
# de vogais que existem no texto.

texto = input("Digite o texto: ")

texto_new = unicodedata.normalize("NFD", texto)
texto_new = texto_new.encode("ascii", "ignore")
texto_new = texto_new.decode("utf-8")

vogais = ["a","e","i","o","u"]
vogaisNum = 0

for i in texto_new.lower:
    if i in vogais:
        vogaisNum += 1

print(vogaisNum)