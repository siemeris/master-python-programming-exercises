sentence=input()
mayusculas=0
minusculas=0
otros=0
for letra in sentence:
    if letra==" " or letra=="!" or letra=="\r":
        otros +=1
    elif letra.isupper():
        mayusculas +=1
    else:
        minusculas +=1
        

print("UPPER CASE " + str(mayusculas), "LOWER CASE " + str(minusculas) )