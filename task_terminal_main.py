from CRUD_task import CRUD

crud = CRUD()

tareasBD = crud.cargarTXT()

while True:
    print("\n" + "="*35) 
    print("        TaskTUI - Menú")
    print("="*35)
    print("1- Crear tarea.")
    print("2- Ver todas las tareas.")
    print("3- Marcar tarea como COMPLETADA.")
    print("4- Eliminar tarea (por nombre).")
    print("0- Salir.")
    print("="*35)

    try: 
        choice = int(input("Ingrese un valor: "))
    except ValueError: 
        print("\n Porfavor, ingrese solo el número de la opción.")
        continue

    if choice == 0:
        print("Programa finalizado. ")
        break

    elif choice == 1: 
            texto = input("- Ingrese el título de la tarea: ").strip().lower()

            print("- Rango de prioridad: ")
            print("- 1 - 3: Baja \n - 4 - 6: Media \n - 7 - 9: Alta \n - 10: Muy Alta")
            try: 
                 prioridad = int(input("- Ingrese la prioridad: "))
            except ValueError:
                 print("\n [AVISO]: Unicamente números enteros. Creación cancelada.")
                 continue
            
            nueva_Tarea = crud.crearTarea(texto, prioridad)
            tareasBD.append(nueva_Tarea)
            crud.ordenarPrioridad(tareasBD)
            crud.guardarEnTXT(tareasBD)

            print("\n Tarea creada con éxito.")
                
    elif choice == 2: 
        print("\n--- LISTA DE TAREAS ---")
        crud.mostrarTodas(tareasBD)

    elif choice == 3:

        nombre_buscar = input("Elige el nombre de la tarea a COMPLETAR: ")
        crud.completarTarea(tareasBD, nombre_buscar)
        crud.guardarEnTXT(tareasBD)
    elif choice == 4:
         nombre_borrar = input("Ingrese el nombre de la tarea a ELIMINAR: ")
         crud.eliminarPorNombre(tareasBD, nombre_borrar)
         crud.guardarEnTXT(tareasBD)
    else: 
        print("\n [AVISO]: Opción no válida")
        #Hacer para que las opciones se repitan

