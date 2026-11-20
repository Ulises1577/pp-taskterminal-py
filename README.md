#  TaskTUI — Minimalist Terminal Task Manager

    > Gestor de tareas ligero para la terminal construido en **Python** con interfaz gráfica TUI (**Rich**). Diseñado como herramienta de productividad personal e integrado al flujo de trabajo diario
  en **Linux / Hyprland**.

    ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
    ![Arch Linux](https://img.shields.io/badge/Arch_Linux-1793D1?style=for-the-badge&logo=arch-linux&logoColor=white)
    ![Hyprland](https://img.shields.io/badge/Hyprland-00A86B?style=for-the-badge&logo=wayland&logoColor=white)
    ![Rich](https://img.shields.io/badge/UI-Rich_Library-ff69b4?style=for-the-badge)

    ---

    ##  Sobre el Proyecto

    **TaskTUI** nació con el objetivo de ejercitar lógica de programación desde las bases y crear una herramienta simple, rápida y sin dependencias pesadas para gestionar pendientes sin salir de la
  terminal.

    Está configurado para ejecutarse al instante con un atajo global de teclado en el gestor de ventanas (Wayland/Hyprland), permitiendo abrir, revisar o tachar tareas en menos de 2 segundos.

    ---

    ##  Características

    *  **Interfaz TUI elegante:** Construida con la librería [Rich](https://github.com/Textualize/rich), ofreciendo tablas, paneles y colores nítidos en la terminal.
    *  **Ordenamiento por Prioridad (Bubble Sort):** Implementación deliberada de Bubble Sort como ejercicio algorítmico, óptimo para colecciones locales livianas de tareas cotidianas.
    *  **Persistencia Local Automática:** Guarda el estado en un archivo de texto plano (`.txt`) en cada operación (crear, completar, eliminar).
    *  **Integración con Hyprland / Linux:** Acceso instantáneo mediante atajo de teclado en un entorno de ventanas tipo *tiling*.

    ---

    ##  Integración con Hyprland (Workflow)

    Para llamarlo como una ventana flotante o terminal emergente rápida, se puede configurar en `~/.config/hypr/hyprland.conf`:

    ```ini
    # Abrir TaskTUI al instante con SUPER + SHIFT + T
    bind = $mainMod SHIFT, T, exec, kitty --class tasktui -e taskt
  ──────
  ##  Instalación y Uso

  ### 1. Requisitos

  • Python 3.8+
  • Librería rich

  En Arch Linux:

    sudo pacman -S python-rich

  En cualquier otra distribución Linux / Entorno virtual:

    pip install rich

  ### 2. Clonar el repositorio

    git clone https://github.com/Ulises1577/TaskTUI.git
    cd TaskTUI

  ### 3. Crear Alias rápido en tu Shell (~/.bashrc o ~/.zshrc)

  Para ejecutarlo desde cualquier directorio:

    echo "alias taskt='python3 /ruta/absoluta/a/TaskTUI/main.py'" >> ~/.bashrc
    source ~/.bashrc

  ### 4. Ejecución

  Simplemente escribe en tu terminal:

    taskt
  ──────
  ##  Decisiones Técnicas y Algoritmos

  • ¿Por qué Bubble Sort?
  Para listas de tareas personales (generalmente menores a 50-100 elementos), un algoritmo con complejidad temporal cuadrática O(n²) en el peor de los casos ofrece una respuesta prácticamente
  instantánea en memoria (menos de un milisegundo) con cero sobrecarga cognitiva o dependencias externas.
  • Persistencia en Texto Plano:
  Permite que las tareas sigan siendo legibles y respaldables manualmente incluso fuera del programa.
  ──────
  ##  Próximas Mejoras (Roadmap)

  [ ] Soporte para categorías o etiquetas (Trabajo, Estudio, Personal).
  [ ] Exportación a formato JSON / Markdown.
  [ ] Recordatorios o fechas límite (Deadlines).
