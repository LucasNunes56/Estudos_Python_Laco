#Altere o programa anterior para mostrar no final a soma dos números.
list = []
a = int(input('Digite um número: '))
b = int(input('Digite um número: '))

for i in range(a+1,b):
    list.append(i)

print(list)
print(sum(list))
