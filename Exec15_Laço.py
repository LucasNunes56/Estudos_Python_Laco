#A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,...
#Faça um programa capaz de gerar a série até o n−ésimo termo.

x = int(input('Digite a range da sequência fibonacci: '))
n1 = 1
n2 = 1
if x == 1 or x == 2:
    print('1')
else:
    for i in range(2, x):
        f = n1 + n2
        n2 = n1
        n1 = f
        i = i + 1

    print(f'{f}')