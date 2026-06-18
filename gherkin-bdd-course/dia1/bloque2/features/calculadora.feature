Feature: Calculadora básica
  Como desarrollador aprendiendo Behave,
  quiero probar operaciones matemáticas simples
  para entender cómo funciona el flujo Given/When/Then.

  Scenario: Suma de dos números positivos
    Given que tengo el número 5
    And   que tengo el número 3
    When  sumo los dos números
    Then  el resultado debe ser 8

  Scenario: Suma con cero
    Given que tengo el número 10
    And   que tengo el número 0
    When  sumo los dos números
    Then  el resultado debe ser 10
