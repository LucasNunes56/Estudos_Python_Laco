#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado
# ao segundo número. Não utilize a função de potência da linguagem.

a = float(input('1°Número: '))
b = int(input('2°Número: '))
pot = 1
for i in range(b):
    pot = pot * a
    i = i + 1
print(pot)
print(a**b)