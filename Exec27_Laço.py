# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas
#e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

list = []

x = int(input('Quantas turmas?\n:_ '))
for i in range(x):
    i = i + 1
    c = int(input(f'Quantos alunos temos na {i}° turma: '))
    list.append(c)

media = sum(list)/x
print(f'Temos, em média, {media:.2f} alunos por turma')