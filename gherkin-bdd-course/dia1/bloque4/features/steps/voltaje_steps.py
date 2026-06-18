from behave import given, when, then


def clasificar_voltaje(voltaje: float) -> str:
    """Clasifica el nivel de batería según el voltaje."""
    if voltaje >= 12.4:
        return "lleno"
    elif voltaje >= 11.5:
        return "normal"
    elif voltaje >= 10.8:
        return "bajo"
    else:
        return "critico"


@given("que el voltaje de la batería es {voltaje:f} V")
def step_voltaje(context, voltaje):
    context.voltaje = voltaje


@when("el sistema clasifica el nivel de batería")
def step_clasificar(context):
    context.nivel = clasificar_voltaje(context.voltaje)


@then('el nivel debe ser "{nivel_esperado}"')
def step_verificar_nivel(context, nivel_esperado):
    assert context.nivel == nivel_esperado, (
        f"Voltaje {context.voltaje}V → "
        f"Se esperaba '{nivel_esperado}', se obtuvo '{context.nivel}'"
    )
