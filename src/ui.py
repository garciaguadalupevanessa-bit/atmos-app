import validation  # 1. Conecta UI con Validation

def capturar_datos_estacion():
    print("\n--- 🛰️ SISTEMA ATMOS: REGISTRO DE DATOS ---")
    
    # --- ZONA ---
    zona = input("Introduce la zona (norte/centro/sur): ").strip().lower()
    if not validation.validar_zona_registro(zona):
        print("❌ Error: Zona no válida.")
        return 

    # --- TEMPERATURA ---
    try:
        temp = float(input("Temperatura (ºC): "))
        if not validation.validar_temperatura(temp):
            print("❌ Error: Temperatura fuera de rango.")
            return
    except ValueError:
        print("❌ Error: Introduce un número válido.")
        return

    # --- HUMEDAD ---
    try:
        humedad = float(input("Humedad (%): "))
        if not validation.validar_humedad_nivel(humedad):
            print("❌ Error: Humedad fuera de rango.")
            return
    except ValueError:
        print("❌ Error: Introduce un número válido.")
        return

    # --- VIENTO ---
    try:
        viento = float(input("Velocidad del viento (km/h): "))
        if not validation.validar_viento_velocidad(viento):
            print("❌ Error: Viento fuera de rango.")
            return
    except ValueError:
        print("❌ Error: Introduce un número válido.")
        return

    return {
        "zona": zona,
        "temperatura": temp,
        "humedad": humedad,
        "viento": viento
    }

# 3. EL ARRANCADOR (Indispensable para que funcione el Play)
if __name__ == "__main__":

    datos = capturar_datos_estacion()
    print("\n✅ Datos validados correctamente:")
    print(datos)
    
