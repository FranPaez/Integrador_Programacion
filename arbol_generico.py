# Crear un nodo para un árbol genérico.
# A diferencia de un árbol binario, cada nodo puede tener múltiples hijos.
def crear_nodo(valor, ramas=None):
    return [valor, ramas if ramas is not None else []]

# Agrega una rama (hijo) a un nodo existente.
def agregar_rama(nodo_raiz, valor_rama):
    rama = crear_nodo(valor_rama)
    nodo_raiz[1].append(rama)
    return rama

# Imprime el árbol con indentación para reflejar la jerarquía.
def imprimir_arbol(nodo, nivel=0):
    print("  " * nivel + nodo[0])
    for rama in nodo[1]:
        imprimir_arbol(rama, nivel + 1)
# Construcción del árbol:
# Raíz (100)
# ├── Rama 1 (50)
# │   ├── Rama 1.1 (25)
# │   │   ├── Hoja 1.1.1 (5)
# │   │   └── Hoja 1.1.2 (3)
# │   └── Hoja 1.2 (15)
# └── Rama 2 (30)
#     ├── Hoja 2.1 (12)
#     └── Hoja 2.2 (8)
# Construye un árbol general con valores asignados a cada nodo.
def construir_arbol_con_valores():
    raiz = crear_nodo("Raíz (Valor: 100)")

    rama1 = agregar_rama(raiz, "Rama 1 (Valor: 50)")
    rama2 = agregar_rama(raiz, "Rama 2 (Valor: 30)")

    rama11 = agregar_rama(rama1, "Rama 1.1 (Valor: 25)")
    agregar_rama(rama1, "Hoja 1.2 (Valor: 15)")

    agregar_rama(rama2, "Hoja 2.1 (Valor: 12)")
    agregar_rama(rama2, "Hoja 2.2 (Valor: 8)")

    agregar_rama(rama11, "Hoja 1.1.1 (Valor: 5)")
    agregar_rama(rama11, "Hoja 1.1.2 (Valor: 3)")

    return raiz

# Mostrar el árbol por consola
print("=== Árbol General con Valores ===\n")
arbol = construir_arbol_con_valores()
imprimir_arbol(arbol)
