class Numeros():
    def cuadrado(self, intx):
        return intx*intx

e=Numeros()
try:
    print(e.cuadrado("a"))
except Exception:
    print("Capturamos exception")