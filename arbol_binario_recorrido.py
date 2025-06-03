def crear_nodo(valor):
    return [valor, None, None] 

def agregar_izquierdo(padre, hijo):
    padre[1] = hijo

def agregar_derecho(padre, hijo):
    padre[2] = hijo

def pre_orden(nodo):
    if nodo is None:
        return
    print(nodo[0])
    pre_orden(nodo[1])
    pre_orden(nodo[2])

def in_orden(nodo):
    if nodo is None:
        return
    in_orden(nodo[1])
    print(nodo[0])
    in_orden(nodo[2])

def post_orden(nodo):
    if nodo is None:
        return
    post_orden(nodo[1])
    post_orden(nodo[2])
    print(nodo[0])

# Crear nodos
raiz = crear_nodo(1)
nodo2 = crear_nodo(2)
nodo3 = crear_nodo(3)
nodo4 = crear_nodo(4)
nodo5 = crear_nodo(5)
nodo6 = crear_nodo(6)
nodo7 = crear_nodo(7)

# Construir el árbol
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6
#             \
#              7

agregar_izquierdo(raiz, nodo2)
agregar_derecho(raiz, nodo3)
agregar_izquierdo(nodo2, nodo4)
agregar_derecho(nodo2, nodo5)
agregar_derecho(nodo3, nodo6)
agregar_derecho(nodo6, nodo7)

# Recorridos

print("=== Recorridos del Árbol ===\n")
print("Recorrido en Pre-orden:")
pre_orden(raiz)
print("Recorrido en In-orden:")
in_orden(raiz)
print("Recorrido en Post-orden:")
post_orden(raiz)

