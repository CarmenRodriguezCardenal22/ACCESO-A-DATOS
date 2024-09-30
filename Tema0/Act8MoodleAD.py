n = int(input("Dime un número"))
for i in range(1,n):
    resto = i%2
    if resto == 0:
        print(i)
