

inventory = []

def add_product():
    while True:
        product_add = input("Ingrese el producto que desea agregar: ").strip().lower()
        if product_add:
            break
        else:
            print("El nombre del producto no puede estar en blanco.")
    
    while True:
        try:
            price = float(input("Ingrese el precio de este producto: "))
            break
        except ValueError:
            print("Ingrese un valor numérico válido para el precio.")
    
    while True:
        try:
            quantity = int(input("Ingrese la cantidad de este producto: "))
            break
        except ValueError:
            print("Ingrese solo valores enteros válidos.")
    
    product_dict = {"name": product_add, "price": price, "quantity": quantity}
    inventory.append(product_dict)
    print(f"Producto '{product_add}' agregado correctamente.")

def search_product():
    user_search = input("Ingrese el producto que desea verificar: ").strip().lower()
    for product in inventory:
        if product["name"] == user_search:
            print("Producto encontrado!")
            print(f"Nombre: {product['name']}")
            print(f"Precio: {product['price']}")
            print(f"Cantidad: {product['quantity']}")
            return
    print("Producto no encontrado. Verifique nuevamente.")

def edit_product():
    name = input("Ingrese el nombre del producto a actualizar: ").strip().lower()
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
                        new_name = input("Ingrese el nuevo nombre: ").strip().lower()
                        if new_name:
                            product["name"] = new_name
                            print("Nombre actualizado correctamente.")
                        else:
                            print("El nombre no puede estar vacío.")
                        break
                    elif choice == 2:
                        new_price = float(input("Ingrese el nuevo precio: "))
                        product["price"] = new_price
                        print("Precio actualizado correctamente.")
                        break
                    elif choice == 3:
                        new_quantity = int(input("Ingrese la nueva cantidad: "))
                        product["quantity"] = new_quantity
                        print("Cantidad actualizada correctamente.")
                        break
                    else:
                        print("Opción inválida.")
                except ValueError:
                    print("Ingrese un valor válido.")
            return
    print(f"Producto '{name}' no encontrado.")

def delete_product():
    product_deleted = input("¿Qué producto desea eliminar?: ").strip().lower()
    for product in inventory:
        if product["name"] == product_deleted:
            inventory.remove(product)
            print(f"Producto '{product_deleted}' eliminado correctamente.")
            return
    print(f"Producto '{product_deleted}' no encontrado.")

def total_inventory_value():
    total = sum(map(lambda p: p["price"] * p["quantity"], inventory))
    print(f"Valor total del inventario: {total:.2f}")



def show_menu():
    while True:
        print("\n--- Sistema de Inventario ---")
        print("1. Agregar producto")
        print("2. Verificar existencia")
        print("3. Editar producto")
        print("4. Eliminar producto")
        print("5. Ver valor total del inventario")
        print("6. Salir")

        choice = input("Seleccione una opción: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            search_product()
        elif choice == "3":
            edit_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            total_inventory_value()
        elif choice == "6":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
            
show_menu()

    