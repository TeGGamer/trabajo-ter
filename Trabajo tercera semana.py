inventory = []

#Defino funcion de agregar produictos con usando un .strip para evitar que el usuario no registre un espacio en blanco 
def add_product():
    while True:
        product_add = input("Ingrese el producto que desea agregar: ").strip() 
        if product_add:
            break
        else:
            print("El nombre del producto no puede estar en blanco intente nuevamente")    
    while True:
        try: 
            price = float(input("Ingrese el precio de este producto:"))
            break
        except ValueError:
            print("Ingrese un valor numerico valido para el precio.")    
    while True:
        try:
            quantity = int(input ("Ingrese la cantidad de este producto:"))
            break
        except ValueError:
            print("Ingrese solo valores validos")
    
    product_dict = {"name" : product_add, "price" : price, "quantity" : quantity
    }
    inventory.append(product_dict)
    
#En la funcion de buscar producto uso el .lower para que no hayan problemas a laa hora de escribir con una mayuscula 
def search_product():
    user_search = input("Ingrese el producto que desea verificar: ") 
    for x in inventory:  
     if x ["name"] == user_search.lower():
         print ("Producto encontrado!")
         print ("Producto", x["name"] )
         print ("Precio",x["price"])
         print ("Cantidad", x["quantity"])
         break
    else:
        print("Producto no encontrado verifique nuevamente")

#en edit and update permiti tambien realizar cambios de nombre del producto ya que por experiencia suele ser necesario 
def edit_updated():
    
    name = input("Ingrese el nombre del producto a actualizar: ").lower()
    for product in inventory:
        if product["name"] == name:
            print(f"Producto encontrado: {product}")
            print("¿Qué desea editar?")
            print("1. Nombre")
            print("2. Precio")
            print("3. Cantidad")
            
            while True:
                try:
                    choice = int(input("Ingrese el número de la opción: "))
                    if choice == 1:
                        new_name = input("Ingrese el nuevo nombre: ").strip()
                        if new_name:
                            product["name"] = new_name.lower()
                            print(f"Nombre actualizado a: {new_name}")
                            break
                        else:
                            print("El nombre del producto no puede estar en blanco intente nuevamente")
                    elif choice == 2:
                        new_price = float(input("Ingrese el nuevo precio: "))
                        product["price"] = new_price
                        print(f"Precio actualizado a: {new_price}")
                        break
                    elif choice == 3:
                        new_quantity = int(input("Ingrese la nueva cantidad en stock: "))
                        product["quantity"] = new_quantity
                        print(f"Cantidad actualizada a: {new_quantity}")
                        break
                    else:
                        print("Ingrese solo valores validos.")
                except ValueError:
                    print("Ingrese solo valores validos.")
            break
    else:
        print(f"Producto '{name}' no encontrado en el inventario.")
                       
def deleted_prodcut():
    product_deleted = input("Que producto desea eliminar: ")
    for product in inventory:
        if product ["name"] == product_deleted:
            inventory.remove(product)                  
            print(f"producto '{product_deleted}' eliminado.")
            return
        print(f"Producto '{product_deleted}' no encontrado.")            
                
#uso metodo lambda para calcular total del inventario 
def total_inventory():
    total = sum(map(lambda product: product["price"] * product["quantity"], inventory))
    print (f"Este es el valor total en productos del inventario: {total}")



def menu ():
    while True:
        menu_option = input("""Bienvenido seleccione que opcion desea ejecutar el dia de hoy
        1.Agregar producto
        2.Verificar existencia del producto
        3.Editar producto
        4.Eliminar producto
        5.Ver total valor en del inventario 
        6.Salir 
        """)
        if menu_option == "1":
            add_product()
        elif menu_option ==  "2":
            search_product()
        elif menu_option == "3":
            edit_updated()     
        elif menu_option == "4":
            deleted_prodcut()
        elif menu_option == "5":
            total_inventory()
        elif menu_option == "6":
            break
        else:
            print("Solo entradas y/o caracteres validos")
            

menu()