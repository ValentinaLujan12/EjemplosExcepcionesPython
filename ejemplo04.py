class Numeros():
    def cuadrado(self, intx):
        if not isinstance(intx, int):
            raise TypeError("Solo se puede calcular el cuadrado de enteros")
        if intx < 0:
            raise ValueError("Solo números mayores que cero")
        return intx*intx

e=Numeros()
print(e.cuadrado(1))
print(e.cuadrado("a"))
print(e.cuadrado(2))