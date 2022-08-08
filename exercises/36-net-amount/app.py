netAmount = 0

s = input()
    
values = s.split(" ")
print(values)

pos=0
for x in values:
    if x=="D":
        netAmount+=int(values[pos+1])
        pos +=1
    elif x=="W":
        netAmount-=int(values[pos+1])
        pos +=1
    else:
        pos +=1        
        pass
        
print(netAmount)