numero = float(input("Introduce un número"))
print("La tabla de multiplicar de ese número es: ")
a = 0
while a < 11:
    result = numero * a
    print(numero,"x",a,"=",result)
    a = a + 1
