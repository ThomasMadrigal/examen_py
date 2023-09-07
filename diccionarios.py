#este taller esta echo por:
#thomas madrigal
#Sebastian patiño preciado

concepcionario = {}

while True:
    print("\nEliga la opcion la cual desea realizar:")
    print("\n1.  un nuevo vehiculo")
    print("2. Actualizar un vehiculo")
    print("3. Consultar un vehiculo")
    print("4. Eliminar un vehiculo")
    print("5. mostrar lo vehiculos creados")
    
    opcion = int(input("\nSeleccione una opción (1/2/3/4/5): "))
    
    if opcion == 1:
        nombrevehiculo = input("\nIngrese el nombre del vehiculo que desea agregar: ") 
        modelovehiculo = int(input("Ingrese modelo de vehiculos(solo numeros): ")) 
        preciovehiculo = int(input("Ingrese el precio del vehiculo $: "))
        
        vehiculo = {
            "nombre": nombrevehiculo,
            "modelo": modelovehiculo,
            "precio": preciovehiculo
        }
        
        concepcionario[nombrevehiculo] = vehiculo
        
        print(f"\nEl vehiculo '{nombrevehiculo}' ha sido agregado con éxito.")
        
    elif opcion == 2:
        nombreActualizarvehiculo = input("\nIngrese el nombre del vehiculo que desea actualizar: ") 
        
        if nombreActualizarvehiculo in concepcionario:
            modeloActualizarvehiculo = int(input("Ingrese modelo de vehiculos: ")) 
            precioActualizarvehiculo = int(input("Ingrese el precio del vehiculo $: "))
            
            concepcionario[nombreActualizarvehiculo]["modelo"] = modeloActualizarvehiculo
            concepcionario[nombreActualizarvehiculo]["precio"] = precioActualizarvehiculo
            
            print(f"\nvehiculo '{nombreActualizarvehiculo}' actualizado correctamente.")
        else:
            print(f"\nvehiculo '{nombreActualizarvehiculo}' no encontrado en el inventario.")
        
    elif opcion == 3:
        nombreConsultarvehiculo = input("\nIngrese el nombre del vehiculo que desea consultar: ") 
        
        if nombreConsultarvehiculo in concepcionario:
            vehiculo = concepcionario[nombreConsultarvehiculo]
            print(f"\nInformación del vehiculo '{nombreConsultarvehiculo}':")
            print(f"Nombre: {vehiculo['nombre']}")
            print(f"modelo: {vehiculo['modelo']}")
            print(f"Precio: ${vehiculo['precio']}")
        else:
            print(f"\nvehiculo '{nombreConsultarvehiculo}' no encontrado en el inventario.")
    elif opcion == 4:
        nombreEliminarvehiculo = input("\nIngrese el nombre del vehiculo que desea eliminar: ") 
        
        if nombreEliminarvehiculo in concepcionario:
            del concepcionario[nombreEliminarvehiculo]
            print(f"\nvehiculo '{nombreEliminarvehiculo}' eliminado correctamente.")
            print(concepcionario)
        else:
            print(f"\nvehiculo '{nombreEliminarvehiculo}' no encontrado en el inventario.")
    elif opcion == 5:
        print(concepcionario)