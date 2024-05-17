class Persona():
    def __init__(self, nombre, genero, edad, direccion):
        self._nombre = nombre
        self._genero = genero
        self._edad = edad
        self._direccion = direccion

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, nuevo_genero):
        self._genero = nuevo_genero

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, nueva_direccion):
        self._direccion = nueva_direccion

    def __str__(self):
        return f"Persona: {self._nombre}, {self._genero}, {self._edad} años, vive en {self._direccion}"

# Ejemplo de uso
persona1 = Persona(nombre="Anahi Mantilla Minda", genero="Femenino", edad=20, direccion="16 y sedalana Calle Principal")
print(persona1)
