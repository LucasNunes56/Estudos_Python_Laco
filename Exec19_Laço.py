#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
list = []
x = int(input('Digite o conjunto de números: '))
if x >= 0 and x <= 1000:
    for i in range(x):
        i = i + 1
        list.append(i)

    print(f'Menor: {min(list)}')
    print(f'Maior: {max(list)}')
    print(f'Soma: {sum(list)}')
else:
    print('Aceitamos apenas números entre 0 e 1000')