from PERSONA import Persona
class Empleado(Persona):
    def __init__(self, idempleado, sueldo):
        self._idempleado = idempleado
        self._sueldo = sueldo

    @property
    def idempleado(self):
        return self._idempleado

    @idempleado.setter
    def idempleado(self, nuevo_id):
        self._idempleado = nuevo_id

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, nuevo_sueldo):
        self._sueldo = nuevo_sueldo

    def __str__(self):
        return f"Empleado {self._idempleado}: Sueldo ${self._sueldo}"

# Ejemplo de uso
empleado1 = Empleado(idempleado=1, sueldo=12000)
print(empleado1)
