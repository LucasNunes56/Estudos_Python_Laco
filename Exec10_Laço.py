# Faça um programa que receba dois números inteiros
#e gere os números inteiros que estão no intervalo compreendido por eles.
list = []
a = int(input('Digite um número: '))
b = int(input('Digite um número: '))

for i in range(a+1,b):
    list.append(i)

print(list)
