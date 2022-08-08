class with2methods():
    def __init__(self):
        self.entrada=""

    def getString(self):
        self.entrada=input()
        
    def printString(self):
        texto = self.entrada.upper()
        print(texto)

strObj = with2methods()
strObj.getString()
strObj.printString()
