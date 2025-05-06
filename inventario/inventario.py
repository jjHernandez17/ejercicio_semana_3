from funciones_inv import *
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

            print("     PRODUCTO        PRECIO             CANTIDAD")
            mostrar_inventario(inventario, nombre)
            
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
        buscar_otro_produ = True
        while buscar_otro_produ:

            produ_no_encon = True
            while produ_no_encon:
                buscar_produ = input("Ingrese el nombre del producto que desea buscar: (si quiere ver todos los productos digite: todos) ")
                if buscar_produ.lower() == "todos":
                    print("     PRODUCTO        PRECIO             CANTIDAD")
                    mostrar_inventario(inventario, nombre)

                else:
                    if buscar_produ in inventario:
                        nom_bus = inventario.get(buscar_produ)
                        print(buscar_produ,nom_bus)
                        resp_inco = True
                        while resp_inco:
                            pre_buscar_otro_prod = input("Desea buscar otro producto? (si/no)")
                            if pre_buscar_otro_prod == "si":
                                print("")
                                resp_inco = False
                            elif pre_buscar_otro_prod == "no":
                                buscar_otro_produ = False
                                produ_no_encon = False
                                resp_inco = False
                            else:
                                print("respuesta no valida, intentelo de nuevo")
                    else: 
                        print("Priducto no encontrado, intentelo de nuevo")

           

       


