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

    console.print(Panel.fit(
         "[bold cyan] TASK_TUI[/bold cyan] | [dim]Gestor de Tareas[/dim]",
          border_style="cyan"
     ))

    table = Table(title=" Tus Tareas Pendientes y Completadas", show_header=True, header_style="bold magenta")
    table.add_column("Creada", style="dim", width=18)
    table.add_column("Tarea", style="bold white", min_width=20)
    table.add_column("Estado", justify="center", width=15)
    table.add_column("Prioridad", justify="right", width=10)

    if not tareasBD:
          table.add_row("-", "[italic dim]No hay tareas registradas[/italic dim]", "-", "-")
    else:
          for t in tareasBD:
               if t.estado:
                    estado_fmt = "[bold green] Completada [/bold green]"
                    texto_fmt = f"[strike dim]{t.texto}[/strike dim]"
               else: 
                    estado_fmt = "[bold yellow] Pendiente [/bold yellow]"
                    texto_fmt = t.texto

               prio_color = "red" if t.prioridad >= 7 else ("yellow" if t.prioridad >= 4 else "blue")
               prio_fmt = f"[{prio_color}]{t.prioridad}[/{prio_color}]"

               table.add_row(t.fecha_creacion, texto_fmt, estado_fmt, prio_fmt)

    console.print(table)
    console.print()

    console.print("[bold cyan][1][/bold cyan]  Crear tarea")
    console.print("[bold cyan][2][/bold cyan]  Marcar completada")
    console.print("[bold cyan][3][/bold cyan]  Eliminar tarea")
    console.print("[bold cyan][0][/bold cyan]  Salir\n")

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

