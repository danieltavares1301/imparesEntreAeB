def impar(a,b):
    for i in range(a, b):
        if i%2!=0:
            print(i)
    return

a = int(input("insira o número inicial: "))
b = int(input("insira o número final: "))
impar(a, b)
