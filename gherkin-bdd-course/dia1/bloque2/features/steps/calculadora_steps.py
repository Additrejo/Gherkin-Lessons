from behave import given, when, then

# 'context' es un objeto compartido entre todos los steps del escenario.
# Úsalo para pasar datos de un paso al siguiente.

@given("que tengo el número {numero:d}")
def step_tengo_numero(context, numero):
    # Si no existe la lista, la creamos
    if not hasattr(context, "numeros"):
        context.numeros = []
    context.numeros.append(numero)


@when("sumo los dos números")
def step_sumo_numeros(context):
    context.resultado = sum(context.numeros)


@then("el resultado debe ser {esperado:d}")
def step_verificar_resultado(context, esperado):
    assert context.resultado == esperado, (
        f"Se esperaba {esperado}, pero se obtuvo {context.resultado}"
    )
