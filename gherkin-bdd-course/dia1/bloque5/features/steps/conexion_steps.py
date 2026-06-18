from behave import given, when, then


class SimuladorCANBus:
    """Simula un bus CAN para pruebas sin hardware real."""

    def __init__(self):
        self.conectado = False
        self.mensajes = []

    def conectar(self) -> bool:
        self.conectado = True
        return True

    def enviar(self, msg_id: int, datos: str) -> bool:
        if not self.conectado:
            return False
        self.mensajes.append({"id": msg_id, "datos": datos})
        return True


@given("que el bus CAN está disponible")
def step_bus_disponible(context):
    context.can_bus = SimuladorCANBus()
    context.error = None


@given("que el sistema está conectado al bus CAN")
def step_ya_conectado(context):
    context.can_bus = SimuladorCANBus()
    context.can_bus.conectar()
    context.error = None


@when("el sistema intenta conectarse")
def step_conectar(context):
    context.resultado_conexion = context.can_bus.conectar()


@when('se envía el mensaje con ID {msg_id} y datos "{datos}"')
def step_enviar_mensaje(context, msg_id, datos):
    msg_id_int = int(msg_id, 16)  # Convierte "0x100" a entero
    context.resultado_envio = context.can_bus.enviar(msg_id_int, datos)


@then("la conexión debe ser exitosa")
def step_conexion_exitosa(context):
    assert context.resultado_conexion is True, "La conexión falló"


@then('el estado debe ser "{estado}"')
def step_verificar_estado(context, estado):
    estado_actual = "conectado" if context.can_bus.conectado else "desconectado"
    assert estado_actual == estado, (
        f"Estado esperado: '{estado}', estado actual: '{estado_actual}'"
    )


@then("el mensaje debe enviarse sin errores")
def step_mensaje_enviado(context):
    assert context.resultado_envio is True, "El mensaje no se pudo enviar"
    assert len(context.can_bus.mensajes) > 0, "No hay mensajes en el bus"
