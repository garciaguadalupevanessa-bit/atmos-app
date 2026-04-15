import subprocess
import platform
from datetime import datetime
from logger import log_warning

def limpiar_pantalla():
    """
    Limpia la consola dependiendo del sistema operativo.
    """
    try:
        print("\033[H\033[2J", end="", flush=True)

        # En caso de que el código ANSII no funcione
        # Definir el comando según el sistema operativo
        es_windows = platform.system() == "Windows"
        comando = "cls" if es_windows else "clear"
        subprocess.run(comando, shell=es_windows, check=True)
        
    except Exception as e:
        log_warning(f"No se pudo limpiar la pantalla: {e}")
        print("\033[H\033[2J", end="")

def imprimir_encabezado_h1(titulo):
    """
    Imprime un encabezado para el menú principal de la consola.
    """
    ancho = 50
    print("╔" + "═" * (ancho - 2) + "╗")
    print(f"║{titulo.center(ancho - 2)}║")
    print("╚" + "═" * (ancho - 2) + "╝")

def imprimir_encabezado_h2(titulo: str):
    """
    Imprime un encabezado para los menus secundarios de la consola.
    """
    ancho = 50
    print("=" * ancho)
    print(f"{titulo.center(ancho)}")
    print("=" * ancho)

def normalizar_entrada(texto: str) -> str:
    """
    Limpia el texto de entrada: elimina espacios extra y convierte 
    comas en puntos para asegurar que float() no falle.
    """
    if not texto:
        return ""
    return texto.strip().replace(",", ".")