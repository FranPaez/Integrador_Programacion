# Esta función crea un nodo para un árbol binario. 
# Recibe un valor y asigna None a sus hijos izquierdo y derecho.
def crear_nodo(valor):
    return [valor, None, None] 
# Estas funciones asignan un subárbol hijo al nodo padre. 
# Dependiendo de la función, se agrega a la izquierda o a la derecha.
def agregar_izquierdo(padre, hijo):
    padre[1] = hijo

def agregar_derecho(padre, hijo):
    padre[2] = hijo
# Esta función recorre e imprime el árbol en preorden, 
# utilizando sangría para reflejar la profundidad.
def imprimir_arbol(nodo, nivel=0):
    if nodo is not None:
        print("  " * nivel + str(nodo[0]))
        imprimir_arbol(nodo[1], nivel + 1)
        imprimir_arbol(nodo[2], nivel + 1)

# Ejemplo de construcción de un árbol binario simple y su visualización por consola.
# Crear nodos
raiz = crear_nodo("A")
nodo_b = crear_nodo("B")
nodo_c = crear_nodo("C")
nodo_d = crear_nodo("D")
nodo_e = crear_nodo("E")

# Construir el árbol
#        A
#       / \
#      B   C
#     / \
#    D   E

agregar_izquierdo(raiz, nodo_b)
agregar_derecho(raiz, nodo_c)
agregar_izquierdo(nodo_b, nodo_d)
agregar_derecho(nodo_b, nodo_e)
# Función para imprimir el árbol con sangría según nivel
def imprimir_arbol(nodo, nivel=0):
    if nodo is not None:
        print("  " * nivel + str(nodo[0]))
        imprimir_arbol(nodo[1], nivel + 1)
        imprimir_arbol(nodo[2], nivel + 1)
# Mostrar árbol estructurado
print("=== Visualización del Árbol ===\n")
imprimir_arbol(raiz)
