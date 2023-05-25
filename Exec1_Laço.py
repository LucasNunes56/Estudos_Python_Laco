#Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

i = 0
while i < 1:
    x = int(input('Digite um número de 0 a 10: '))
    if x < 0 or x > 10:
        print(f'{x} não está entre números pedidos, tente novamente: ')
    elif x >= 0 and x <= 10:
        print(f'{x} Está entre os números pedidos, Obrigado!')
        i = i + 1
    else:
        print('3RR0')


