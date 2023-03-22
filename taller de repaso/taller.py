from dataclasses import dataclass


@dataclass
class Elemento:
    nombre: str

    def __eq__(self, otro):
        if isinstance(otro, Elemento):
            return self.nombre == otro.nombre
        return False


class Conjunto:
    contador = 0

    def __init__(self, nombre):
        self.__id = Conjunto.contador
        Conjunto.contador += 1
        self.nombre = nombre
        self.elementos = []

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento):
        for e in self.elementos:
            if e == elemento:
                return True
        return False

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        for e in otro_conjunto.elementos:
            self.agregar_elemento(e)

    def __add__(self, otro_conjunto):
        nuevo_conjunto = Conjunto(f"{self.nombre} UNIDO {otro_conjunto.nombre}")
        nuevo_conjunto.unir(self)
        nuevo_conjunto.unir(otro_conjunto)
        return nuevo_conjunto

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        elementos_interseccion = []
        for e in conjunto1.elementos:
            if conjunto2.contiene(e):
                elementos_interseccion.append(e)
        nombre_conjunto = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        conjunto_interseccion = Conjunto(nombre_conjunto)
        for e in elementos_interseccion:
            conjunto_interseccion.agregar_elemento(e)
        return conjunto_interseccion

    def __str__(self):
        elementos_str = ', '.join([e.nombre for e in self.elementos])
        return f"Conjunto {self.nombre}: ({elementos_str})"
