out=''
for x in range(1000,3001,1):
    aux=1
    for i in str(x):
        if int(i)%2==0:
            aux +=1
            if aux==4:    
                out += str(x) + ', '
print(out)