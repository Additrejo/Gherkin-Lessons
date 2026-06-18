Feature: Conexión al bus CAN del rover
  Verificar que el sistema puede conectarse
  y desconectarse correctamente del bus CAN.

  Scenario: Conexión exitosa al bus CAN
    Given que el bus CAN está disponible
    When  el sistema intenta conectarse
    Then  la conexión debe ser exitosa
    And   el estado debe ser "conectado"

  Scenario: Envío de mensaje por CAN
    Given que el sistema está conectado al bus CAN
    When  se envía el mensaje con ID 0x100 y datos "FF 00"
    Then  el mensaje debe enviarse sin errores
