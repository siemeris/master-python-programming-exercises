entrada=input()
lista= [x for x in entrada.split(",") if int(x)%2!=0]
print(lista)
