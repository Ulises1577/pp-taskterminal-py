from create_task import crearTarea
#Creamos base de datos en array
tareasBD = []
 
while True: 
    print("Bienvenido a TaskTUI")
    print("¿Qué deseas hacer? ")
    print("1- Crear tarea. ")
    print("2- Ver todas las tareas. ")
    print("3- Eliminar tarea (id). ")
    print("0- Para cerrar el programa.")

    choice = int(input("Ingrese un valor: "))

    if choice == 0:
        print("Programa finalizado. ")
        break

    if choice == 1:

        id_tarea = input("- Ingrese el ID de la tarea: ")
        texto = input("- Ingrese el título de la tarea: ")
        estado = False
        print("- Ingrese la prioridad según este rango de números: ")
        print("- 1 - 3: Baja \n - 4 - 6: Media \n - 7 - 9: Alta \n - 10: Muy Alta")
        prioridad = int(input("- Ingrese la prioridad segun este rango de números: "))

        #todoMinusculas(texto)
        #quitarEspacio(texto, id_tarea)
        nueva_Tarea = crearTarea(id_tarea, texto, estado, prioridad)
        tareasBD.append(nueva_Tarea)
    elif choice == 2: 
        print("Prubeq")
    #mostrarTodos()
        pass
    elif choice == 3: 
        print("Elige el ID de la tarea: ")
    #eliminarTarea(id_tarea)
        pass
    else: 
        print("ERROR. Elige entre las opcionces dadas")
        #Hacer para que las opciones se repitan

