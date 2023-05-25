#Faça um programa que leia e valide as seguintes informações:
#    Nome: maior que 3 caracteres;
#    Idade: entre 0 e 150;
#    Salário: maior que zero;
#    Sexo: 'f' ou 'm';
#    Estado Civil: 's', 'c', 'v', 'd';
#Use a função len(string) para saber o tamanho de um texto (número de caracteres).

i = 0
while i < 1:
    nome = input('Digite o nome: ')
    if len(nome) < 3:
        print('O nome deve ter mais que 3 caracteres.')
    else:
        i = i +1
i = 0
while i < 1:
    idd = int(input('Digite a idade: '))
    if idd < 0 or idd > 150:
        print('Idade inválida, Digite novamente')
    else:
        i = i +1
i = 0
while i < 1:
    sal = float(input('Digite o salário: '))
    if sal < 0:
        print('O salário deve ser maior que 0')
    else:
        i = i +1
i = 0
while i < 1:
    sex = input('Digite o sexo M - Masculino || F - Feminino || N - Neutro: ')
    if sex.upper() != 'M' and sex.upper() != 'F' and sex.upper() != 'N':
        print('Sexo inválido, digite novamente.')
    else:
        i = i +1
i = 0
while i < 1:
    estd = input('Digite o esatdo civil S - Solteiro(e) || C - Casado(e) || V - Viuvo(e) || D - Divorciado(e): ')
    if estd.upper() != 'S' and estd.upper() != 'C' and estd.upper() != 'V' and estd.upper() != 'D':
        print('Estado civil inválido, digite novamente.')
    else:
        i = i +1

