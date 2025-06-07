def crear_nodo(valor):
    return [valor, None, None] 

def agregar_izquierdo(padre, hijo):
    padre[1] = hijo

def agregar_derecho(padre, hijo):
    padre[2] = hijo

def longitud_de_camino(nodo, valor_buscado, longitud_actual):
    if nodo is None:
        return -1
    if nodo[0] == valor_buscado:
        return longitud_actual
    resultado_izquierdo = longitud_de_camino(nodo[1], valor_buscado, longitud_actual + 1)
    if resultado_izquierdo != -1:
        return resultado_izquierdo
    return longitud_de_camino(nodo[2], valor_buscado, longitud_actual + 1)

def profundidad(nodo, valor_buscado, profundidad_actual):
    if nodo is None:
        return -1
    if nodo[0] == valor_buscado:
        return profundidad_actual
    resultado_izquierdo = profundidad(nodo[1], valor_buscado, profundidad_actual + 1)
    if resultado_izquierdo != -1:
        return resultado_izquierdo
    return profundidad(nodo[2], valor_buscado, profundidad_actual + 1)

def nivel(nodo, valor_buscado, nivel_actual):
    if nodo is None:
        return -1
    if nodo[0] == valor_buscado:
        return nivel_actual
    resultado_izquierdo = nivel(nodo[1], valor_buscado, nivel_actual + 1)
    if resultado_izquierdo != -1:
        return resultado_izquierdo
    return nivel(nodo[2], valor_buscado, nivel_actual + 1)


def altura(nodo):
    if nodo is None:
        return -1
    if nodo[1] is None and nodo[2] is None:
        return 0
    altura_izquierda = altura(nodo[1])
    altura_derecha = altura(nodo[2])
    return 1 + max(altura_izquierda, altura_derecha)

def grado(nodo, valor_buscado):
    if nodo is None:
        return -1
    if nodo[0] == valor_buscado:
        grado_actual = 0
        if nodo[1] is not None:
            grado_actual = grado_actual + 1
        if nodo[2] is not None:
            grado_actual = grado_actual + 1
        return grado_actual

    resultado_izquierdo = grado(nodo[1], valor_buscado)
    if resultado_izquierdo != -1:
        return resultado_izquierdo

    resultado_derecho = grado(nodo[2], valor_buscado)
    return resultado_derecho

def peso(nodo):
    if nodo is None:
        return 0
    peso_izquierdo = peso(nodo[1])
    peso_derecho = peso(nodo[2])
    return 1 + peso_izquierdo + peso_derecho


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

# Mostrar propiedades
print("=== Propiedades del Árbol ===\n")
print("Altura del árbol:", altura(raiz))
print("Peso del árbol:", peso(raiz))
for valor in [1, 4, 5, 6, 7]:
    print(f"Longitud del camino hasta el nodo {valor}:", longitud_de_camino(raiz, valor, 0))
for valor in [1, 4, 5, 6, 7]:
    print(f"Profundidad del nodo {valor}:", profundidad(raiz, valor, 0))
for valor in [1, 4, 5, 6, 7]:
    print(f"Nivel del nodo {valor}:", nivel(raiz, valor, 0))
for valor in [1, 2, 3, 6, 7]:
    print(f"Grado del nodo {valor}:", grado(raiz, valor))
