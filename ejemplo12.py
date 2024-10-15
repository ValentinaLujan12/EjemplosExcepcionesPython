class Numeros():
    def cuadrado(self, intx):
        return intx*intx

e=Numeros()
try:
    print(e.cuadrado(1))
except Exception:
    print("Capturamos exception")
else:
    print("Muy bien no se capturo nada")
finally:
    print("Siempre se ejecuta independiente de si se capturó o no una excepción")