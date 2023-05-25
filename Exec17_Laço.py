#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

x = int(input('Digite o número quedejsa o fatorial: '))
f = 1
for i in range(1, x+1):
    f = f * i
print(f'{x}!= {f}')