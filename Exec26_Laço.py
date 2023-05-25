# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
#Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

a = 0
b = 0
padre = 0

x = int(input('Quantos eleitores temos nesta eleição?\n: '))
for i in range(x):
    c = int(input('Em qual candidato o eleitor quer votar?\n 1-Candidato A\n 2-Candidato B\n 3-Candidato Padre\n:  '))
    if c == 1:
        a = a + 1
    elif c == 2:
        b = b + 1
    elif c == 3:
        padre = padre + 1
    else:
        print('3RR0')

print(f'Candidaro A {a} votos\nCandidato B {b} votos\nCandidato Padre {padre} votos')
