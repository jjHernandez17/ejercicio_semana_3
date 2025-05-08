from funciones_inv import *             #importa todas las funciones que hay en el archivo funciones
inventario = { }                            #crea un diccionario vacío
DANGER = "\033[91m"                             
WARNING = "\033[93m"                    #crea colores para las letras de los prints
RESET = "\033[0m"

volver_menu = True                                  
while volver_menu:                      #se crea el while para volver al menu
    print("------------------------------")
    print("----BIENVENIDO A MI TIENDA----")
    print("------------------------------")

    menu = int(input("QUE DESEA HACER: " \
    "\n(1) Añadir productos " \
    "\n(2) Consultar productos " \
    "\n(3) actualizar precios "
    "\n(4) agregar cantidad a un producto " \
    "\n(5) Eliminar productos " \
    "\n(6) Calcular el valor total de el inventario " \
    "\n(7) Salir del programa\n"))                              #se crea menu de opciones

    print("---"*30)


    if menu == 1:                                                                       #si el menu de opciones es 1 haga
        agregar_mas_productos = True
        while agregar_mas_productos:
            print("---AGREGAR PRODUCTO---\n")
            nombre = input("Ingrese el nombre del producto: \n")
            res_no_va = True
            while res_no_va:                                                        #por si la respuesta ingresada por el usuario no es valida
                try:                                                    
                    precio = float(input("Indique el precio del producto: \n"))
                    cantidad = int(input("Indique la cantidad disponible del producto: \n"))
                    res_no_va = False                                                               #se rome el while
                except ValueError:                                                                  #haga esto si la respuesta no es un valor
                    print("---"*30)
                    print(WARNING + "Respuesta no valida, intentelo de nuevo "+RESET)
                    print("---"*30)

            

            inventario[nombre] = {"precio" : precio, "cantidad": cantidad}                                  #se guarda con la key el nombre del estudiante el precio y la cantidad
            print("---"*30)
            print("     PRODUCTO            PRECIO                  CANTIDAD")
            mostrar_inventario(inventario, nombre)
            print("---"*30)
            
            inco_agregar = True
            while inco_agregar:                                         #por si la respuesta de agregar mas no es ni si ni no
                ag_mas = input("Desea agregar mas productos? (si/no)")
                if ag_mas == "si":                                      #si la respuesta es si, haga:
                    print("")
                    inco_agregar= False                             #quiebra el while de la respuesta incorrecta para volver a agregar producto
                elif ag_mas == "no":                                    #quiebra los dos while para volver al menu
                    agregar_mas_productos = False
                    inco_agregar= False

                    
                else: 
                    print(WARNING + "Respuesta no valida, intentelo de nuevo "+RESET)
    elif menu == 2:                                                                     #si en el menu es la opcion 2
        buscar_otro_produ = True                                
        while buscar_otro_produ:                                                    #se crea el menu por si quiere volver a buscar un producto

            produ_no_encon = True
            while produ_no_encon:                                           #se crea el while por si no se encontró el producto
                buscar_produ = input("Ingrese el nombre del producto que desea buscar: (si quiere ver todos los productos digite: todos) ")
                if buscar_produ.lower() == "todos":                                 #si la respuesta es "todos"
                    print("     PRODUCTO                 PRECIO             CANTIDAD")
                    mostrar_inventario(inventario, nombre)                          #imprime todos los productos
                    produ_no_encon = False                          #quiebre el while de producto no encontrado
                    buscar_otro_produ = False                           #quiebra el while de buscar otro producto

                else:                                                   # si la respuesta no es "todos"
                    if buscar_produ in inventario:                              #comprobar que todos los productos esten en el diccionario
                        nom_bus = inventario.get(buscar_produ)
                        precio1 = nom_bus["precio"]
                        cantidad1 = nom_bus["cantidad"]

                        print(f"{buscar_produ:<15} {precio1:<15} {cantidad1:<15}")
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
                        print("---"*30)
                        print(WARNING + "El producto no se encontó en el inventario "+RESET)
                        print("---"*30)
                        
    elif menu == 3:
        intentelo_de_nuevo = True
        while intentelo_de_nuevo:
            nom_act_pre = input("Ingrese el nombre del producto al cual desea actualizar el precio")
            if nom_act_pre in inventario:
                act_precio_datos = inventario.get(nom_act_pre)
                cantidad1 = act_precio_datos["cantidad"]
                precio1 = act_precio_datos["precio"]
                print(f"{nom_act_pre:<15} {precio1:<15}{cantidad1:<15}")
                nuev_preci = float(input("Ingrese el precio actualizado"))
                inventario[nom_act_pre]["precio"] = nuev_preci
                intentelo_de_nuevo2  = True
                while intentelo_de_nuevo2:
                    act_otro_precio = input("Desea actualizar el precio de otro producto? (si/no) \n")
                    if act_otro_precio == "si":
                        print("")
                        intentelo_de_nuevo2 = False
                    elif act_otro_precio == "no":
                        intentelo_de_nuevo = False
                        intentelo_de_nuevo2 = False
                    else:
                        print("---"*30)
                        print(WARNING + "Respuesta no valida, intentelo de nuevo "+RESET)
            else:
                print(WARNING + "El producto no se encontrò en el diccionario, intentelo de nuevo"+ RESET)
    
    elif menu == 4:
        agregar_mas_cant = True
        while agregar_mas_cant:
            ag_nombre = input("Ingrese el nombre del producto al que quiere aumentarle la cantidad en el inventario\n")
            if ag_nombre in inventario:
                prod_ag = inventario.get(ag_nombre)
                cantid_agregar = int(input(f"ingrese la cantidad que quiere agregarle a: {ag_nombre}\n"))
                inventario[ag_nombre]["cantidad"] += cantid_agregar
                intentelo_de_nuevo3 = True
                while intentelo_de_nuevo3:
                    agregar_mas = input("Desea agregar mas cantidad a otro producto? (si/no)\n")
                    if agregar_mas == "si":
                        print("")
                        intentelo_de_nuevo3 = False
                    elif agregar_mas.lower() == "no":
                        agregar_mas_cant = False
                        intentelo_de_nuevo3 = False
                    else:
                        print(WARNING + "Respuesta no valida, intentelo de nuevo "+RESET)
            else:
                print(WARNING + "El producto no se encontrò en el diccionario, intentelo de nuevo"+ RESET)
                
                
        
                
        
    elif menu == 5:
        volver_opciones = True
        while volver_opciones:
            opcion = int(input("Ingrese que quiere hacer: \n" \
                                "(1) Eliminar un producto por completo \n" \
                                "(2) eliminar cantidad de un producto en especifico \n"
                                "(3) Volver al menu\n "))
            if opcion == 1:
                nom_eliminar_completo = input("Ingrese el nombre del producto que quiere eliminar por completo: \n")
                intentelo_de_nuevo4 = True
                while intentelo_de_nuevo4:
                    seguro = input(DANGER + f"seguro que quiere eliminar {nom_eliminar_completo} por completo del inventario? (si/no)\n"+RESET)
                    if seguro == "si":
                        del inventario[nom_eliminar_completo]
                        intentelo_de_nuevo4 = False
                        print(f"{nom_eliminar_completo} Eliminado por completo")
                    elif seguro == "no":
                        print("")
                        intentelo_de_nuevo4 = False
                    else:
                        print(WARNING + "Respuesta no valida, intentelo de nuevo "+RESET)
            elif opcion == 2: 
                nom_eliminar_cant = input("Ingrese el nombre del producto que quiere eliminarle cantidad: \n")
                
                elm_cant_datos = inventario[nom_eliminar_cant]
                print(f"{nom_eliminar_cant:<15} {elm_cant_datos["precio"]:<15} {elm_cant_datos["cantidad"]:<15} ")
                cant_eliminar = int(input(f"Ingrese la cantidad que desea eliminar de {nom_eliminar_cant}"))
                inventario[nom_eliminar_cant]["cantidad"] -=  cant_eliminar
                act_cant_prod = inventario[nom_eliminar_cant]
                print(f"asì quedò el producto: \n{nom_eliminar_cant:<15} {act_cant_prod["precio"]:<15} {act_cant_prod["cantidad"]:<15} ")
            elif opcion == 3 : 
                volver_opciones = False
            
            else: 
                print("---"*30)
                print(WARNING + "Respuesta no valida, intentelo de nuevo "+RESET)
                print("---"*30)
                
    elif menu == 6:
        print("---" * 30)
        print("   PRODUCTO                 PRECIO        CANTIDAD           SUBTOTAL")
        total = 0
        for producto, datos in inventario.items():
            cantidad = datos.get("cantidad")
            precio = datos.get("precio")
            subtotal = total_multi_cada_pro(precio, cantidad)
            print(f" {producto:<25} ${precio:<15.2f} {cantidad:<15} ${subtotal:<.2f}")
            total = total + subtotal
        print("---"*30)
        print(f"TOTAL INVENTARIO: {total:49}")
        print("---"*30)
    elif menu == 7:
        volver_menu = False
    else: 
        print(WARNING + "Respuesta no valida, intentelo de nuevo " +RESET)
        print("---"*30) 