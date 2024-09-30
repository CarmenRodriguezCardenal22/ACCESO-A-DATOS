import random
lista = []
for i in range(0,10):
    lista.append(random.randint(1,51))
print(lista)
n = int(input("Dime un número"))
if n in lista:
    print("Bingo")
else:
    print("No encontrado")
        
