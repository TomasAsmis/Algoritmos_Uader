class NodoPila:
    def __init__(self, info):
        self.informacion = info
        self.siguiente = None

class Pila:
    def __init__(self):
        self.cima = None
        self.tamanio = 0

def apilar(pila, elemento):
    nodo = NodoPila(elemento)
    nodo.siguiente = pila.cima
    pila.cima = nodo
    pila.tamanio += 1

def desapilar(pila):
    aux = pila.cima.informacion
    pila.cima = pila.cima.siguiente
    pila.tamanio -= 1
    return aux

def pila_vacia(pila):
    return pila.cima is None

def cima(pila):
    return pila.cima.informacion

def tamanio(pila):
    return pila.tamanio


def posicion_personajes(pila_mcu, nombre1, nombre2):
    aux = Pila()
    pos = 1
    pos1, pos2 = -1, -1

    while not pila_vacia(pila_mcu):
        personaje = desapilar(pila_mcu)
        nombre = personaje["nombre"].lower()
        if nombre == nombre1.lower():
            pos1 = pos
        if nombre == nombre2.lower():
            pos2 = pos
        apilar(aux, personaje)
        pos += 1

    while not pila_vacia(aux):
        apilar(pila_mcu, desapilar(aux))

    return pos1, pos2

def personajes_mas_de_5_peliculas(pila_mcu):
    aux = Pila()
    resultado = []

    while not pila_vacia(pila_mcu):
        personaje = desapilar(pila_mcu)
        if personaje["peliculas"] > 5:
            resultado.append(personaje)
        apilar(aux, personaje)

    while not pila_vacia(aux):
        apilar(pila_mcu, desapilar(aux))

    return resultado

def peliculas_viuda_negra(pila_mcu):
    aux = Pila()
    cantidad = 0

    while not pila_vacia(pila_mcu):
        personaje = desapilar(pila_mcu)
        if personaje["nombre"].lower() in ("viuda negra", "black widow"):
            cantidad = personaje["peliculas"]
        apilar(aux, personaje)

    while not pila_vacia(aux):
        apilar(pila_mcu, desapilar(aux))

    return cantidad

def personajes_por_iniciales(pila_mcu, iniciales):
    aux = Pila()
    resultado = []
    iniciales_lower = [i.lower() for i in iniciales]

    while not pila_vacia(pila_mcu):
        personaje = desapilar(pila_mcu)
        if personaje["nombre"][0].lower() in iniciales_lower:
            resultado.append(personaje)
        apilar(aux, personaje)

    while not pila_vacia(aux):
        apilar(pila_mcu, desapilar(aux))

    return resultado