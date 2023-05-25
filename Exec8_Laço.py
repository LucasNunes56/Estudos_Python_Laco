#Faça um programa que leia 5 números e informe a soma e a média dos números.

list = []
for i in range(5):
    x = int(input('Número: '))
    list.append(x)
mx = max(list)
print(f'Soma: {sum(list)}')
print(f'Maior: {mx}')
print(f'Média {(sum(list)/5):.2f}')


