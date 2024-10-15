class Numeros():
    def cuadrado(self, intx):
        return intx*intx

e=Numeros()
try:
    print(e.cuadrado(-1))
except TypeError:
    print("Capturamos una excepción de tipo TypeError")
except ValueError:
    print("Capturamos una excepción de tipo ValueError")
except:
    print("Capturamos cualquier otro tipo de excepción")