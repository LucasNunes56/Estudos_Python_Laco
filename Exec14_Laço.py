#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares
# e a quantidade de números ímpares.
lista = []
listb = []
for i in range(10):
    x = i + 1
    n = int(input(f'Digite o {x}° número: '))
    if n % 2 == 0:
        lista.append(n)
    else:
        listb.append(n)

print(f'Pares: {lista}')
print(f'Ímpares: {listb}')


