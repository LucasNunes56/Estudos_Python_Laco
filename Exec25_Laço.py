# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera
#verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60;
#e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

list = []
x = int(input('Digite a quantidade de pessoas selecionadas para a pesquisa: '))
for i in range(x):
    c = i + 1
    n = int(input(f'Digite a idade da {c}° pessoa: '))
    list.append(n)
    media = sum(list)/x

media = round(media)
#print(media)
if media > 0 and media <= 25:
    print(f'Com a idade média de {media}, essa turma é Jovem')
elif media >= 26 and media <= 60:
    print(f'Com a idade média de {media}, essa turma é Adulta')
elif media > 60:
    print(f'Com a idade média de {media}, essa turma é Idosa')
else:
    print('3RR0')
