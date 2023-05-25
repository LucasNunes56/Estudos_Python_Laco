# Faça um programa que calcule o mostre a média aritmética de N notas.

list = []
x = int(input('Quantas notas são? '))
for i in range(x):
    c = i + 1
    n = float(input(f'Digite a {c}° nota a nota: '))
    list.append(n)
media = sum(list)/x
print(f'A média de notas é {media}')
