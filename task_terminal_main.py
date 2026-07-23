from CRUD_task import CRUD
#Creamos base de datos en array
tareasBD = []
crud = CRUD()

while True:
    print("\n") 
    print("Bienvenido a TaskTUI")
    print("¿Qué deseas hacer? ")
    print("1- Crear tarea. ")
    print("2- Ver todas las tareas. ")
    print("3- Eliminar tarea (id). ")
    print("0- Para cerrar el programa.")

    try: 
        choice = int(input("Ingrese un valor: "))
    except ValueError: 
        print("\n Porfavor, ingrese el mismo caracter pedido. ")
        continue

    if choice == 0:
        print("Programa finalizado. ")
        break

    elif choice == 1: 
            id_tarea = int(input("- Ingrese el ID de la tarea: "))
            texto = input("- Ingrese el título de la tarea: ").strip().lower()
            estado = False
            print("- Ingrese la prioridad según este rango de números: ")
            print("- 1 - 3: Baja \n - 4 - 6: Media \n - 7 - 9: Alta \n - 10: Muy Alta")
            try: 
                 prioridad = int(input("- Ingrese la prioridad segun este rango de números: "))
            except ValueError:
                 print("\n Aviso, ingresa unicamente numeros. Creacion cancelada.")
                 continue
            
            nueva_Tarea = crud.crearTarea(id_tarea, texto, estado, prioridad)
            tareasBD.append(nueva_Tarea)
            crud.ordenarPrioridad(tareasBD)
            
            print("\n Tarea creada con éxito.")
                
    elif choice == 2: 
        #un metodo para ordenar segun prioridad
        crud.mostrarTodas(tareasBD)
        print("Estas son todas las tareas")

    elif choice == 3: 
        id_delete = int(input("Elige el ID de la tarea: "))
        crud.eliminarTarea(tareasBD, id_delete)
    else: 
        print("ERROR. Elige entre las opcionces dadas")
        #Hacer para que las opciones se repitan

