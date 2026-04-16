# src/auth_validation.py

import re


def validar_usuario(usuario):
    """
    Comprueba que el nombre de usuario:
    - no esté vacío
    - tenga entre 3 y 20 caracteres
    """
    # quitamos espacios al principio y al final
    usuario = usuario.strip()

    if usuario == "":
        return False, "El usuario no puede estar vacío."

    if len(usuario) < 3:
        return False, "El usuario debe tener al menos 3 caracteres."

    if len(usuario) > 20:
        return False, "El usuario no puede tener más de 20 caracteres."

    return True, ""


def validar_email(email):
    """
    Comprueba que el email tenga:
    - texto antes de la arroba
    - una arroba (@)
    - un dominio
    - un punto final con extensión como .com, .es, .org, etc.

    Esta expresión regular NO es la más compleja del mundo,
    pero para vuestro nivel es clara y suficiente.
    """
    email = email.strip()

    if email == "":
        return False, "El email no puede estar vacío."

    # Patrón sencillo:
    # algo@algo.algo
    patron = r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$"

    if re.match(patron, email) is None:
        return False, "El email no tiene un formato válido."

    return True, ""


def validar_contrasena(contrasena):
    """
    Comprueba que la contraseña:
    - tenga entre 8 y 15 caracteres
    - tenga al menos una mayúscula
    - tenga al menos una minúscula
    - tenga al menos un número
    - tenga al menos un carácter especial
    """
    if contrasena == "":
        return False, "La contraseña no puede estar vacía."

    if len(contrasena) < 8 or len(contrasena) > 15:
        return False, "La contraseña debe tener entre 8 y 15 caracteres."

    # any(...) devuelve True si encuentra al menos un caso que cumple
    if not any(letra.isupper() for letra in contrasena):
        return False, "La contraseña debe incluir al menos una mayúscula."

    if not any(letra.islower() for letra in contrasena):
        return False, "La contraseña debe incluir al menos una minúscula."

    if not any(letra.isdigit() for letra in contrasena):
        return False, "La contraseña debe incluir al menos un número."

    caracteres_especiales = "!@#$%^&*()-_=+[]{};:,.<>?/\\|"

    if not any(letra in caracteres_especiales for letra in contrasena):
        return False, "La contraseña debe incluir al menos un carácter especial."

    return True, ""
