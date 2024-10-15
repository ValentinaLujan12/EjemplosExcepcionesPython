class Numeros():
    def cuadrado(self, intx):
        return intx*intx

e=Numeros()
try:
    print(e.cuadrado(1))
    print(e.cuadrado("a"))
    print(e.cuadrado(2))
except:
    print("Capturamos una excepción")

print("continuemos con el programa")