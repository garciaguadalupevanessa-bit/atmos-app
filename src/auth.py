# src/auth.py

import json
import os

from auth_validation import (
    validar_usuario,
    validar_email,
    validar_contrasena
)

# Ruta al archivo JSON donde se guardan los usuarios.
# __file__ apunta a src/auth.py.
# Subimos una carpeta (..), entramos en scripts y buscamos users.json.
RUTA_USUARIOS = os.path.join(
    os.path.dirname(__file__),
    "..",
    "scripts",
    "users.json"
)


def cargar_usuarios():
    """
    Lee el archivo users.json y devuelve la lista de usuarios.

    Si el archivo no existe o está vacío/corrupto,
    devuelve una lista vacía para que el programa no se rompa.
    """
    if not os.path.exists(RUTA_USUARIOS):
        return []

    with open(RUTA_USUARIOS, "r", encoding="utf-8") as archivo:
        try:
            usuarios = json.load(archivo)
            return usuarios
        except json.JSONDecodeError:
            return []


def guardar_usuarios(lista_usuarios):
    """
    Guarda en el archivo JSON la lista completa de usuarios.

    indent=4 sirve para que el archivo quede ordenado y legible.
    ensure_ascii=False sirve para respetar tildes y ñ.
    """
    with open(RUTA_USUARIOS, "w", encoding="utf-8") as archivo:
        json.dump(lista_usuarios, archivo, indent=4, ensure_ascii=False)


def buscar_usuario_por_email(email):
    """
    Busca un usuario usando su email.
    Si lo encuentra, devuelve su diccionario.
    Si no lo encuentra, devuelve None.
    """
    usuarios = cargar_usuarios()

    for usuario in usuarios:
        if usuario["email"].lower() == email.lower():
            return usuario

    return None


def registrar_usuario(usuario, email, contrasena):
    """
    Registra un usuario nuevo si:
    - el nombre de usuario es válido
    - el email es válido
    - la contraseña es válida
    - no existe ya ese email registrado
    """
    # 1) Validar usuario
    valido, mensaje = validar_usuario(usuario)
    if not valido:
        return False, mensaje

    # 2) Validar email
    valido, mensaje = validar_email(email)
    if not valido:
        return False, mensaje

    # 3) Validar contraseña
    valido, mensaje = validar_contrasena(contrasena)
    if not valido:
        return False, mensaje

    # 4) Comprobar si el email ya existe
    if buscar_usuario_por_email(email) is not None:
        return False, "Ese email ya está registrado."

    # 5) Cargar usuarios actuales
    usuarios = cargar_usuarios()

    # 6) Crear nuevo usuario
    nuevo_usuario = {
        "usuario": usuario,
        "email": email,
        "contrasena": contrasena
    }

    # 7) Añadir a la lista
    usuarios.append(nuevo_usuario)

    # 8) Guardar la lista actualizada
    guardar_usuarios(usuarios)

    return True, "Usuario registrado correctamente."


def login(email, contrasena):
    """
    Comprueba si existe un usuario con ese email
    y si la contraseña coincide.
    """
    usuario_encontrado = buscar_usuario_por_email(email)

    if usuario_encontrado is None:
        return False, "No existe ningún usuario con ese email."

    if usuario_encontrado["contrasena"] != contrasena:
        return False, "La contraseña es incorrecta."

    return True, f"Bienvenido/a, {usuario_encontrado['usuario']}."
