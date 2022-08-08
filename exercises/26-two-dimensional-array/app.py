input_str = input()
dim=[int(x) for x in input_str.split(',')]
rowNum=dim[0]
colNum=dim[1]
print(rowNum)
print(colNum)
arr=[]
arr1=[]

for row in range(rowNum):
    for col in range(colNum):
        arr1.append(col*row)   
    arr.append(arr1)
    arr1=[] 
print(arr)
