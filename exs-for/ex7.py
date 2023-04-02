# 7
# Crie um programa que solicita ao usuário que ele defina sua senha. A senha
# deve ser um texto (string) composto apenas por dígitos e deve ter entre 5 e 10 valores.
# O usuário tem apenas 6 chances de definir corretamente a senha. Caso ele defina
# corretamente a senha nas tentativas que ele tem, imprima uma mensagem de sucesso.
# Caso ele não defina a senha corretamente, imprima uma mensagem de insucesso. Dica:
# na aula aprendemos a ver se uma string é formada apenas por dígitos e aprendemos a
# descobrir o tamanho do texto digitado.

tentativas = 0
maxTentativas = 6
for i in range(tentativas, maxTentativas):
    senha = input("Defina sua senha: ")

    if (senha.isdigit() and len(senha) >= 5 and len(senha) <= 10):
        print("Senha definida com sucesso")
        break
    else:
        print("tentativa inválida, tente novamente. ")
    tentativas += 1

if tentativas == maxTentativas:
    print("Quantidade de tentativas excedido.")