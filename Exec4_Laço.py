# Supondo que a população de um país A seja da ordem de 80.000 habitantes
#com uma taxa anual de crescimento de 3% e que a população de B seja 200.000 habitantes
#com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários
#para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.


a = 80000
b = 200000
i = 0
while a < b:
    a = a + (a*3/100)
    b = b + (b*0.015)
    i = i + 1

print(f'Demora {i} anos para a cidade A ter mais habitantes que a cidade B.\nA cidade A com {round(a)} habitantes e a B com {round(b)} habitantes.')