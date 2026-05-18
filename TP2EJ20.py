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
 
 
OPUESTOS = {
    "norte":    "sur",
    "sur":      "norte",
    "este":     "oeste",
    "oeste":    "este",
    "noreste":  "suroeste",
    "noroeste": "sureste",
    "sureste":  "noroeste",
    "suroeste": "noreste",
}
 
def registrar_movimiento(pila_movimientos, pasos, direccion):
    movimiento = {"pasos": pasos, "direccion": direccion}
    apilar(pila_movimientos, movimiento)
 
def retorno_robot(pila_movimientos):
    pila_retorno = Pila()
    pila_aux = Pila()
 
    while not pila_vacia(pila_movimientos):
        mov = desapilar(pila_movimientos)
        movimiento_inverso = {
            "pasos": mov["pasos"],
            "direccion": OPUESTOS[mov["direccion"]]
        }
        apilar(pila_retorno, movimiento_inverso)
        apilar(pila_aux, mov)
 
    while not pila_vacia(pila_aux):
        apilar(pila_movimientos, desapilar(pila_aux))
 
    return pila_retorno