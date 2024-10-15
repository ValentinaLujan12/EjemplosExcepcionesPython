class SinFondos(Exception):
    def __init__(self, nombreUsuario, cantidad):
        super().__init__("Tu cuenta no tiene ${}".format(cantidad))
        self._cantidad = cantidad
        self._nombreUsuario = nombreUsuario
    
    def mostrarMensaje(self):
        print("La cuenta de " + self._nombreUsuario + " no tiene: $" + str(self._cantidad))

try:
    raise SinFondos("Juan",20)
except Exception as f:
    f.mostrarMensaje()