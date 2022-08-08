import math

def formula():
    C=50
    H=30
    listaresultado = []
    valoresentrada = [x for x in input().split(',')]
    for x in valoresentrada:
        result = str(round(math.sqrt((2*C*int(x))/H)))
        listaresultado.append(result)
        Separator= ","
        out=Separator.join(listaresultado)
    print(out)

formula()