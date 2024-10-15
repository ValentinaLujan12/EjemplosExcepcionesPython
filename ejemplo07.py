class Numeros():
    def cuadrado(self, intx):
        return intx*intx

e=Numeros()
try:
    print(e.cuadrado("a"))
except TypeError:
    print("Capturamos una excepción de tipo TypeError")