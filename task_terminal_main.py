#!/usr/bin/env python3
from CRUD_task import CRUD
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich import print as rprint

console = Console()
crud = CRUD()
tareasBD = crud.cargarTXT()

def mostrar_menu():
    console.clear()

    color_orange_main = "#ed7d05"
    color_orange_dark = "#e64a1b"
    color_orange_bright = "#ff9e3b"

    #Este es el encabezado
    console.print(Panel(
         f"[bold {color_orange_bright}]TASK_TUI[/bold {color_orange_bright}]",
          border_style=color_orange_dark,
          expand=True
     ))

    #Tabla expandida
    table = Table(
        title=f"\n[bold {color_orange_main} Tus Tareas Pendientes y Completadas [/ bold {color_orange_main}]\n",
        show_header=True,
        header_style=f"bold {color_orange_bright}",
        border_style=color_orange_bright,
        expand=True
    )

    table = Table(
        title=f"\n[not italic bold {color_orange_main}]Tus Tareas Pendientes y Completadas[/not italic bold {color_orange_main}]\n",
        show_header=True,
        header_style=f"bold {color_orange_main}",
        border_style=color_orange_dark,
        expand=True
    )




    
    table.add_column("Creada", style="dim white", min_width=10, justify="center")
    table.add_column("Tarea", style="bold white", ratio=3)
    table.add_column("Estado", justify="center", min_width=10)
    table.add_column("Prioridad", justify="center", min_width=8)

    if not tareasBD:
          table.add_row("-", "[not italic bold]No hay tareas registradas[/not italic bold]", "-", "-")
    else:
          for t in tareasBD:
               if t.estado:
                    estado_fmt = "[bold green] Completada [/bold green]"
                    texto_fmt = f"[strike dim]{t.texto}[/strike dim]"
               else: 
                    estado_fmt = f"[bold {color_orange_bright}] Pendiente [/bold {color_orange_bright}]"
                    texto_fmt = f"[bold white]{t.texto}[/bold white]"

               if t.prioridad >= 7:
                prio_fmt = f"[bold #ff5555] {t.prioridad}[/bold #ff5555]" # Rojardo
               elif t.prioridad >= 4:
                prio_fmt = f"[bold {color_orange_bright}] {t.prioridad}[/bold {color_orange_bright}]" # Naranja para media
               else:
                prio_fmt = f"[{color_orange_dark}] {t.prioridad}[/{color_orange_dark}]" 

               table.add_row(t.fecha_creacion, texto_fmt, estado_fmt, prio_fmt)

    console.print(table)
    console.print()

    menu_content = (
        f"[{color_orange_bright}][1][/{color_orange_bright}]  Crear tarea   "
        f"[{color_orange_bright}][2][/{color_orange_bright}]  Marcar completada   "
        f"[{color_orange_bright}][3][/{color_orange_bright}]  Eliminar tarea   "
        f"[bold red][0][/bold red]  Salir"
    )

    console.print(Panel(menu_content, border_style=color_orange_dark, expand=True))
    console.print()

Prompt.illegal_choice_message="[bold red] Opción no válida. [/bold red]"
while True:
    mostrar_menu()
    choice = Prompt.ask("[bold white] Selecciona una opción [/bold white]", choices=["1","2","3","0"], default="0")

    if choice == "0":
        break

    elif choice == "1":
        texto = Prompt.ask("\n [bold]Título de la tarea[/bold]").strip().lower()
        if not texto:
            continue
        try:
            prioridad = int(Prompt.ask(" [bold]Prioridad (1 a 10)[/bold]", default="5"))
        except ValueError:
            prioridad = 5

        nueva = crud.crearTarea(texto, prioridad)
        tareasBD.append(nueva)
        crud.ordenarPrioridad(tareasBD)
        crud.guardarEnTXT(tareasBD)

    elif choice == "2":
        nombre = Prompt.ask("\n [bold]Nombre de la tarea a COMPLETAR[/bold]").strip().lower()
        if crud.completarTarea(tareasBD, nombre):
            crud.guardarEnTXT(tareasBD)
            Prompt.ask("\n[dim]Presiona ENTER para continuar...[/dim]")

    elif choice == "3":
        nombre = Prompt.ask("\n  [bold]Nombre de la tarea a ELIMINAR[/bold]").strip().lower()
        if crud.eliminarPorNombre(tareasBD, nombre):
            crud.guardarEnTXT(tareasBD)
            Prompt.ask("\n[dim]Presiona ENTER para continuar...[/dim]")

