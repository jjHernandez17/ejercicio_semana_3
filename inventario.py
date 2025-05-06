inventario = { }

volver_menu = True
while volver_menu:
    print("------------------------------")
    print("----BIENVENIDO A MI TIENDA----")
    print("------------------------------")

    menu = int(input("QUE DESEA HACER: " \
    "\n(1) Añadir productos " \
    "\n(2) Consultar productos " \
    "\n(3) actualizar precios " \
    "\n(4) Eliminar productos " \
    "\n(5) Calcular el valor total de el inventario " \
    "\n(6) Salir del programa"))

    if menu == 1:
        agregar_mas_productos = True
        while agregar_mas_productos:
            print("---AGREGAR PRODUCTO---\n")
            nombre = input("Ingrese el nombre del producto: \n")
            precio = float(input("Indique el precio del producto: \n"))
            cantidad = int(input("Indique la cantidad disponible del producto: \n"))

            inventario[nombre] = {"precio" : precio, "cantidad": cantidad}

            for i, n in inventario.items():
                print(f"PRODUCTO: {i} PRECIO: ${inventario[nombre]['precio']} CANTIDAD: {inventario[nombre]['cantidad']}")
            inco_agregar = True
            while inco_agregar:
                ag_mas = input("Desea agregar mas productos? (si/no)")
                if ag_mas == "si":
                    print("")
                    inco_agregar= False
                elif ag_mas == "no":
                    agregar_mas_productos = False
                    inco_agregar= False

                    
                else: 
                    print("respuesta no valida, intentelo de nuevo")
    elif menu == 2:
        buscar_produ = input("Ingrese el nombre del producto que desea buscar: ")
        info = inventario.get(nombre)
        print(buscar_produ,info)

           

       


