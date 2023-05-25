# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha
#igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

i = 0

while i < 1:
    login = input('Login: ')
    senha = input('Senha: ')
    if login == senha:
        print('Login não pode ser o mesmo que a senha, digite novamente.')
    else:
        i = i + 1
        print('Bem-vindo!')


