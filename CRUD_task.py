from datetime import datetime

class CRUD: 
    def __init__(self, fecha_creacion =  None, texto = None, estado = False, prioridad = None):
        self.fecha_creacion = fecha_creacion
        self.texto = texto
        self.estado = estado
        self.prioridad = prioridad

    def crearTarea (self, texto, prioridad):
        fecha_c = datetime.now().strftime("%Y-%m-%d %H:%M")
        estado_inicial = False #Nace como pendiente
        return CRUD(fecha_c, texto, estado_inicial, prioridad)

    def completarTarea(self, tareasBD, nombre_buscar):
        nombre_limpio = nombre_buscar.strip().lower()
        for tarea in tareasBD:
            if tarea.texto.strip().lower() == nombre_limpio:
                tarea.estado = True 
                print(f" Tarea '{tarea.texto}' fue marcada como COMPLETADA")
                return True
        print(" [AVISO]: No se encontró ninguna tarea con ese nombre.")
        return False

    def eliminarPorNombre(self, tareasBD, nombres_buscar):
        nombre_limpio = nombres_buscar.strip().lower()
        for j in tareasBD:
            if j.texto.strip().lower() == nombre_limpio:
                tareasBD.remove(j)
                print("Tarea eliminada")
                return True
            
        print("ERROR. Tarea no encontrada. ")
        return False

    def ordenarPrioridad(self, tareasBD):
        n = len(tareasBD)
        for i in range(n):
            for j in range(0, n - i -1):
                if tareasBD[j].prioridad < tareasBD[j + 1].prioridad:
                    tareasBD[j], tareasBD[j + 1] = tareasBD[j + 1], tareasBD[j]

    def mostrarTodas(self, tareasBD):
        if not tareasBD:
            print("\n No hay tareas registradas.")

        for k in tareasBD:
            simbolo_estado = "[X] Completado" if k.estado else "[ ] Pendiente"
            print( f" Tarea: {k.texto} | Fecha de Creacion: {k.fecha_creacion} | Estado: {simbolo_estado} | Prioridad: {k.prioridad}")

    def eliminarCompletadas(self, tareasBD):
        total_inicial = len(tareasBD)
        #esto es para comparar luego

        #El [:] es para usar la misma tareasBD y no que se cree otra por estar dentro de una funcion
        tareasBD[:] = [j for j in tareasBD if not j.estado]
        # y ahora se guardan unicamente en el mismo arreglo las que esten en False

        if len(tareasBD) < total_inicial:
            print("Todas las tareas completadas fueron eliminadas. ")
            return True
        else:
            print("ERROR. Aun no hay ninguna tarea completada.")
            return False


    def guardarEnTXT(self, tareasBD):
        with open("tareas.txt", "w", encoding="utf-8") as file:
            for t in tareasBD:
                file.write(f"{t.fecha_creacion}|{t.texto}|{t.estado}|{t.prioridad}\n")

    def cargarTXT(self):
        tareas_cargadas = []
        try: 
            with open("tareas.txt", "r", encoding="utf-8") as file:
                for linea in file:
                    datos = linea.strip().split("|")
                    if len(datos) == 4:
                        fecha_c, texto, estado_str, prioridad = datos
                        es_completada = True if estado_str == "True" else False

                        nueva = CRUD(fecha_c, texto, es_completada, int(prioridad))
                        tareas_cargadas.append(nueva)

        except FileNotFoundError:
            pass
        return tareas_cargadas
