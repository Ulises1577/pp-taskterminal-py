class CRUD: 
    def __init__(self, id_tarea =  None, texto = None, estado = None, prioridad = None):
        self.id_tarea = id_tarea
        self.texto = texto
        self.estado = estado
        self.prioridad = prioridad

    def crearTarea (self, id_tarea, texto, estado, prioridad):
        return CRUD(id_tarea, texto, estado, prioridad)

    def eliminarTarea(self, tareasBD, id_delete):
        for j in tareasBD:
            if j.id_tarea == id_delete:
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
            
