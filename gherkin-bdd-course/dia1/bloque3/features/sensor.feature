Feature: Lectura de sensor de temperatura
  Verificar que el sistema procesa correctamente
  los valores del sensor y genera alertas cuando corresponde.

  Scenario: Temperatura dentro del rango normal
    Given que el sensor reporta una temperatura de 45 grados
    When  el sistema procesa la lectura
    Then  el estado del sistema debe ser "normal"
    And   no debe generarse ninguna alerta

  Scenario: Temperatura por encima del límite
    Given que el sensor reporta una temperatura de 85 grados
    When  el sistema procesa la lectura
    Then  el estado del sistema debe ser "critico"
    And   debe generarse una alerta de sobrecalentamiento

  Scenario: Sensor desconectado
    Given que el sensor no está disponible
    When  el sistema intenta leer la temperatura
    Then  el estado del sistema debe ser "error"
    And   debe generarse una alerta de sensor desconectado
