sentence=input()
contadorletra=0
contadornumero=0
otros=0
for letra in sentence:
    if letra==" " or letra=="!" or letra=="\r":
        otros +=1
    elif letra=="1" or letra=="2" or letra=="3" or letra=="4" or letra=="5" or letra=="6" or letra=="7" or letra=="8" or letra=="9" or letra=="0":
        contadornumero +=1
    else:
        contadorletra +=1
        

print("LETTERS " + str(contadorletra), "DIGITS " + str(contadornumero) )