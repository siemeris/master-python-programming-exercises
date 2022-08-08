def desecalista(secuencia):
    lista = secuencia.split(",")
    return lista

print(desecalista("34, 67, 55"))
print(tuple(desecalista("34, 67, 55")))