#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
list = []
for i in range(50):
    if i%2 != 0:
        list.append(i)
print(f'{list}')

