# Faça um programa que, dado um conjunto de N números,
#determine o menor valor, o maior valor e a soma dos valores.

list = []

x = int(input('Digite o conjunto de números: '))

for i in range(x):
    i = i + 1
    list.append(i)

print(f'Menor: {min(list)}')
print(f'Maior: {max(list)}')
print(f'Soma: {sum(list)}')