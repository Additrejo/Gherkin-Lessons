# Bloque 1 · ¿Qué es BDD y Gherkin? 🟢

## Objetivo
Entender qué es BDD, para qué sirve Gherkin, y escribir tu primer escenario sin código.

---

## Conceptos clave

### BDD — Behavior-Driven Development
Metodología de desarrollo donde las pruebas se escriben en **lenguaje natural** antes del código.
- Cierra la brecha entre desarrolladores, testers y stakeholders.
- Cada prueba describe un *comportamiento* del sistema.

### Gherkin — el lenguaje
Archivos `.feature` con palabras clave fijas:

| Palabra   | Rol                        |
|-----------|----------------------------|
| `Feature` | Agrupa escenarios          |
| `Scenario`| Un caso de prueba concreto |
| `Given`   | Estado inicial             |
| `When`    | Acción / evento            |
| `Then`    | Resultado esperado         |
| `And/But` | Continúa el paso anterior  |

---

## Archivos de este bloque

| Archivo | Descripción |
|---------|-------------|
| `ejemplos/bateria.feature` | Ejemplo: alerta de voltaje bajo en rover |
| `ejercicio/obstaculos.feature` | ✏️ Tu turno: escenario de detección de obstáculo |

---

## ✏️ Ejercicio

Abre `ejercicio/obstaculos.feature` y completa el escenario.

**Situación:**
> El rover está en movimiento. Si detecta un obstáculo a menos de 20 cm,
> debe detenerse y enviar un mensaje de alerta por CAN.

Usa `Given`, `When`, `Then` y al menos un `And`.
