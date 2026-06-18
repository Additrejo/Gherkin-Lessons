# ✏️ EJERCICIO — Bloque 1
# Completa el escenario de detección de obstáculos del rover.
#
# Situación:
#   El rover está en movimiento. Si detecta un obstáculo a menos de 20 cm,
#   debe detenerse y enviar un mensaje de alerta por CAN.
#
# Instrucciones:
#   - Usa Given, When, Then y al menos un And
#   - Puedes escribirlo en español
#   - No necesitas código todavía

Feature: Detección de obstáculos del rover

  Scenario: El rover se detiene al detectar un obstáculo cercano
    Given # TODO: estado inicial del rover
    And   # TODO: condición del sensor de distancia
    When  # TODO: qué acción ocurre
    Then  # TODO: resultado esperado (movimiento)
    And   # TODO: resultado esperado (comunicación CAN)
