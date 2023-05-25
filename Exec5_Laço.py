#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento
#iniciais. Valide a entrada e permita repetir a operação.

a = float(input('Habitantes da cidade A: '))
txa = float(input('Taxa de crescimento em porcentagem (%) da cidade A: '))
b = float(input('Habitantes da cidade B: '))
txb = float(input('Taxa de crescimento em porcentagem (%) da cidade B: '))
i = 0
while a < b:
    a = a + (a*txa/100)
    b = b + (b*txb/100)
    i = i + 1

print(f'Demora {i} anos para a cidade A ter mais habitantes que a cidade B.'
      f'\nA cidade A com {round(a)} habitantes e a B com {round(b)} habitantes.')

