# environment.py — Hooks globales de Behave
#
# Este archivo se ejecuta automáticamente antes/después de cada
# scenario, feature o toda la suite. Ideal para setup/teardown.


def before_all(context):
    """Se ejecuta UNA VEZ antes de toda la suite."""
    print("\n🚀 Iniciando suite de pruebas CAN...")
    context.config.stop = True  # Detener al primer fallo


def after_all(context):
    """Se ejecuta UNA VEZ al terminar toda la suite."""
    print("\n✅ Suite de pruebas CAN finalizada.")


def before_scenario(context, scenario):
    """Se ejecuta antes de CADA scenario."""
    print(f"\n▶  Iniciando: {scenario.name}")
    # Aquí podrías inicializar conexiones, limpiar estado, etc.
    context.can_bus = None
    context.mensajes_enviados = []


def after_scenario(context, scenario):
    """Se ejecuta después de CADA scenario."""
    # Limpieza: cerrar conexión si quedó abierta
    if context.can_bus is not None:
        context.can_bus = None
        print(f"   🔌 Bus CAN cerrado después de: {scenario.name}")

    if scenario.status == "failed":
        print(f"   ❌ FALLÓ: {scenario.name}")
    else:
        print(f"   ✔  OK: {scenario.name}")
