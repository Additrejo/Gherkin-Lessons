# Ejemplo completo — Bloque 1
# Este archivo muestra la sintaxis básica de Gherkin.
# Todavía no tiene steps en Python — solo es para leer y entender.

Feature: Monitoreo de batería del rover
  Como sistema de control del rover C2V2,
  quiero detectar voltajes bajos en la batería
  para proteger el hardware y alertar al operador.

  Scenario: Alerta cuando el voltaje es crítico
    Given que el sensor INA219 está conectado al bus CAN
    And   el voltaje de la batería es de 10.5V
    When  el rover solicita una lectura de voltaje
    Then  el sistema debe publicar una alerta de batería baja
    And   el LED de estado debe cambiar a rojo

  Scenario: Sin alerta cuando el voltaje es normal
    Given que el sensor INA219 está conectado al bus CAN
    And   el voltaje de la batería es de 12.6V
    When  el rover solicita una lectura de voltaje
    Then  el sistema no debe publicar ninguna alerta
    And   el LED de estado debe permanecer verde
