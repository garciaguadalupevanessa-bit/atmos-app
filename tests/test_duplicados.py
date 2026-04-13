from src.validation import validar_duplicado


def test_validar_duplicado_devuelve_false_si_ya_existe():
    registros_existentes = [
        {
            "fecha_registro": "2026-04-07",
            "zona_registro": "centro",
            "temperatura": 23.5,
            "humedad_nivel": 60,
            "viento_velocidad": 20
        }
    ]

    assert validar_duplicado("2026-04-07", "centro", registros_existentes) is False


def test_validar_duplicado_devuelve_true_si_no_existe():
    registros_existentes = [
        {
            "fecha_registro": "2026-04-07",
            "zona_registro": "centro",
            "temperatura": 23.5,
            "humedad_nivel": 60,
            "viento_velocidad": 20
        }
    ]

    assert validar_duplicado("2026-04-08", "sur", registros_existentes) is True


def test_validar_duplicado_devuelve_true_si_fecha_igual_pero_zona_distinta():
    registros_existentes = [
        {
            "fecha_registro": "2026-04-07",
            "zona_registro": "centro",
            "temperatura": 23.5,
            "humedad_nivel": 60,
            "viento_velocidad": 20
        }
    ]

    assert validar_duplicado("2026-04-07", "sur", registros_existentes) is True


def test_validar_duplicado_devuelve_true_si_zona_igual_pero_fecha_distinta():
    registros_existentes = [
        {
            "fecha_registro": "2026-04-07",
            "zona_registro": "centro",
            "temperatura": 23.5,
            "humedad_nivel": 60,
            "viento_velocidad": 20
        }
    ]

    assert validar_duplicado("2026-04-08", "centro", registros_existentes) is True

def test_validar_duplicado_devuelve_true_si_lista_vacia():
    registros_existentes = []

    assert validar_duplicado("2026-04-07", "centro", registros_existentes) is True

def test_validar_duplicado_devuelve_true_si_lista_vacia():
    registros_existentes = []

    assert validar_duplicado("2026-04-07", "centro", registros_existentes) is True
