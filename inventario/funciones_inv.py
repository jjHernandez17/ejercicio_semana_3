
def mostrar_inventario(inventario, nombre):
    for i, n in inventario.items():
                print(f"     {i:<10}         ${n['precio']:<10}               {n['cantidad']:<10}")

total_multi_cada_pro = lambda almacenar_cant, almacenar_precio: almacenar_cant * almacenar_precio


