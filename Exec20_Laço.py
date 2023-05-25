# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial
#várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

n = 0
while n < 1:
    x = int(input('Digite o número que deseja o fatorial: '))
    if x >= 16:
        print('Aceitamos apenas números entre 1 e 15, Digite novamente.')
    else:
        f = 1
        for i in range(1, x+1):
            f = f * i
        print(f'{x}!= {f}')
    m = input('Deseja continuar? (S)- Sim | (N)- Não: ')
    if m.upper() == 'S':
        n = 0
    elif m.upper() == 'N':
        n = 1
        print('Obrigado!')
    else:
        print('Não entendi, digite novamente.')