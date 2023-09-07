#este taller esta echo por:
#thomas madrigal
#Sebastian patiño preciado

concepcionario = []

while True:
    print("\nEliga la opcion la cual desea realizar:")
    print("\n1. crea un nuevo vehiculo")
    print("2. Actualizar un vehiculo")
    print("3. Consultar un vehiculo")
    print("4. Eliminar un vehiculo")
    print("5. mostrar lo vehiculos creados")
   

    opcion = int(input("\nSeleccione una opción (1/2/3/4/5): "))

    if opcion == 1:
        nombrevehiculo = input("\nIngrese el nombre del vehiculo que desea agregar: ")
        modelovehiculo = int(input("Ingrese el modelo de vehiculos: "))
        preciovehiculo = float(input("Ingrese el precio del vehiculo $: "))

        vehiculo = {
            "nombre": nombrevehiculo,
            "modelo": modelovehiculo,
            "precio": preciovehiculo
        }

        concepcionario.append(vehiculo)

        print(f"\nEl vehiculo '{nombrevehiculo}' ha sido agregado con éxito.")

    elif opcion == 2:
        nombreActualizarvehiculo = input("\nIngrese el nombre del vehiculo que desea actualizar: ")

        vehiculo_encontrado = False
        for vehiculo in concepcionario:
            if vehiculo["nombre"] == nombreActualizarvehiculo:
                modeloActualizarvehiculo = int(input("Ingrese el modelo de vehiculos: "))
                precioActualizarvehiculo = float(input("Ingrese el precio del vehiculo $: "))

                vehiculo["modelo"] = modeloActualizarvehiculo
                vehiculo["precio"] = precioActualizarvehiculo

                print(f"\nvehiculo '{nombreActualizarvehiculo}' actualizado correctamente.")
                vehiculo_encontrado = True
                break

        if not vehiculo_encontrado:
            print(f"\nvehiculo '{nombreActualizarvehiculo}' no encontrado en el inventario.")

    elif opcion == 3:
        nombreConsultarvehiculo = input("\nIngrese el nombre del vehiculo que desea consultar: ")

        vehiculo_encontrado = False
        for vehiculo in concepcionario:
            if vehiculo["nombre"] == nombreConsultarvehiculo:
                print(f"\nInformación del vehiculo '{nombreConsultarvehiculo}':")
                print(f"Nombre: {vehiculo['nombre']}")
                print(f"modelo: {vehiculo['modelo']}")
                print(f"Precio: ${vehiculo['precio']}")
                vehiculo_encontrado = True
                break

        if not vehiculo_encontrado:
            print(f"\nvehiculo '{nombreConsultarvehiculo}' no encontrado en el inventario.")

    elif opcion == 4:
        concepcionario.clear()
        print("Lista de vehiculos eliminada correctamente")
    elif opcion == 5:
        print(concepcionario)
