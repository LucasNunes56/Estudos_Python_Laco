# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs
#e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.

list = []

x = int(input('Quantos CDs tem a coleção?\n>_ '))
for i in range(x):
    i = i + 1
    c = float(input(f'Quanto gastou no {x}° disco?\nR$'))
    list.append(c)
media = sum(list)/x
print(f'Você gastou um total de R${sum(list):.2f} na coleção.')
print(f'A média é de R${media:.2f} por disco.')
