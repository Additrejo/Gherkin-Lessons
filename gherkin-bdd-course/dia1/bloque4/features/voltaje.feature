Feature: Clasificación de voltaje del rover
  El sistema debe clasificar el nivel de batería
  según el voltaje recibido del sensor INA219.

  # Scenario Outline permite repetir el mismo escenario
  # con diferentes valores de la tabla Examples.

  Scenario Outline: Clasificar nivel de batería por voltaje
    Given que el voltaje de la batería es <voltaje> V
    When  el sistema clasifica el nivel de batería
    Then  el nivel debe ser "<nivel>"

    Examples:
      | voltaje | nivel    |
      | 12.6    | lleno    |
      | 11.8    | normal   |
      | 11.0    | bajo     |
      | 10.5    | critico  |
      | 9.0     | critico  |
