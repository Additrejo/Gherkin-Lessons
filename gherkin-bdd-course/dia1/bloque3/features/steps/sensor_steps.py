from behave import given, when, then

LIMITE_CRITICO = 80  # grados Celsius


class SistemaMonitoreo:
    """Simula el sistema que procesa lecturas de sensores."""

    def __init__(self):
        self.temperatura = None
        self.sensor_disponible = True
        self.estado = None
        self.alertas = []

    def procesar_lectura(self):
        if not self.sensor_disponible:
            self.estado = "error"
            self.alertas.append("sensor desconectado")
            return

        if self.temperatura >= LIMITE_CRITICO:
            self.estado = "critico"
            self.alertas.append("sobrecalentamiento")
        else:
            self.estado = "normal"


# ---------- GIVEN ----------

@given("que el sensor reporta una temperatura de {temp:d} grados")
def step_temperatura(context, temp):
    context.sistema = SistemaMonitoreo()
    context.sistema.temperatura = temp


@given("que el sensor no está disponible")
def step_sensor_desconectado(context):
    context.sistema = SistemaMonitoreo()
    context.sistema.sensor_disponible = False


# ---------- WHEN ----------

@when("el sistema procesa la lectura")
def step_procesar(context):
    context.sistema.procesar_lectura()


@when("el sistema intenta leer la temperatura")
def step_intentar_leer(context):
    context.sistema.procesar_lectura()


# ---------- THEN ----------

@then('el estado del sistema debe ser "{estado_esperado}"')
def step_verificar_estado(context, estado_esperado):
    assert context.sistema.estado == estado_esperado, (
        f"Estado esperado: '{estado_esperado}', "
        f"Estado actual: '{context.sistema.estado}'"
    )


@then("no debe generarse ninguna alerta")
def step_sin_alertas(context):
    assert len(context.sistema.alertas) == 0, (
        f"Se esperaban 0 alertas, pero se encontraron: {context.sistema.alertas}"
    )


@then("debe generarse una alerta de sobrecalentamiento")
def step_alerta_sobrecalentamiento(context):
    assert "sobrecalentamiento" in context.sistema.alertas, (
        f"Alerta esperada no encontrada. Alertas actuales: {context.sistema.alertas}"
    )


@then("debe generarse una alerta de sensor desconectado")
def step_alerta_sensor(context):
    assert "sensor desconectado" in context.sistema.alertas, (
        f"Alerta esperada no encontrada. Alertas actuales: {context.sistema.alertas}"
    )
