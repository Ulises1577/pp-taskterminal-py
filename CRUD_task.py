class CRUD: 
    def __init__(self, id_tarea =  None, texto = None, estado = None, prioridad = None):
        self.id_tarea = id_tarea
        self.texto = texto
        self.estado = estado
        self.prioridad = prioridad

    def crearTarea (self, id_tarea, texto, estado, prioridad):
        return CRUD(id_tarea, texto, estado, prioridad)

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
        for k in tareasBD:
            print( f" Nombre: {k.texto} | Id: {k.id_tarea} | Estado: {k.estado} | Prioridad: {k.prioridad}")

    def guardarEnTXT(self, tareasBD):
        with open("tareas.txt", "w", encoding="utf-8") as file:
            for t in tareasBD:
                file.write(f"{t.id_tarea} | {t.texto} | {t.estado} | {t.prioridad} \n")

    def cargarTXT(self):
        tareas_cargadas = []
        try: 
            with open("tareas.txt", "r", encoding="utf-8") as file:
                for linea in file:
                    datos = linea.strip().split("|")
                    if len(datos) == 4:
                        id_t, texto, estado, prioridad = datos
                        nueva = CRUD(id_t, texto, estado == "False", int(prioridad))
                        tareas_cargadas.append(nueva)
        except FileNotFoundError:
            pass
        return tareas_cargadas
2            
