
def mostrar_inventario(inventario, nombre):
    for i, n in inventario.items():
                print(f"     {i}         ${n['precio']}               {n['cantidad']}")