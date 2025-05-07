
def mostrar_inventario(inventario, nombre):
    for i, n in inventario.items():
                print(f"     {i:<10}         ${n['precio']:<10}               {n['cantidad']:<10}")

