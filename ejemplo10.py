class Numeros():
    def cuadrado(self, intx):
        return intx*intx

e=Numeros()
try:
    print(e.cuadrado("a"))
except (TypeError, ValueError):
    print("Capturamos varios tipos de excepciones juntas")