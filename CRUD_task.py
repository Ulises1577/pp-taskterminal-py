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

    def mostrarTodas(self, tareasBD):
        for k in tareasBD:
            print( f" Nombre: {k.texto} | Id: {k.id_tarea} | Estado: {k.estado} | Prioridad: {k.prioridad}")
            
