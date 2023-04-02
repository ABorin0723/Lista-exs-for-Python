# 6 
# Crie um programa que solicita o nome e o estado civil de 20 pessoas pelo teclado.
# Ao final, imprima apenas o nome das pessoas separadas por estado civil:
# solteiras, casadas, divorciadas e viúvas (nesta ordem!)

solteiros = []
casados = []
divorciados = []
viúvos = []
inválidos = []

for i in range(20):
    nome = input("Qual seu nome? ")
    civil = input("Qual seu estado civil? (solteiro, casado, divorciado ou viúvo) ")

    if civil.lower() == "solteiro":
        solteiros.append(nome)
    elif civil.lower() == "casado":
        casados.append(nome)
    elif civil.lower() == "divorciado":
        divorciados.append(nome)
    elif civil.lower() == "viúvo" or civil == "viuvo":
        viúvos.append(nome)
    else:
        inválidos.append(nome)

print("Solteiros: \n")
print(solteiros)
print("\n Casados: \n")
print(casados)
print("\n Divorciados: \n")
print(divorciados)
print("\n Viúvos: \n")
print(viúvos)
print("\n Inválidos: \n")
print(inválidos)