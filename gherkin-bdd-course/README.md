# 🥒 Curso Express: Gherkin + Python con Behave

Curso de 2 días para aprender BDD (Behavior-Driven Development) con Gherkin y el framework **Behave** en Python, aplicado a contextos de **sistemas embebidos y protocolos automotrices (CAN/LIN)**.

---

## 📦 Requisitos

```bash
pip install behave
pip install python-can       # Día 2 - Bloque 8
pip install allure-behave    # Día 2 - Bloque 10
```

---

## 📂 Estructura del curso

```
gherkin-bdd-course/
├── dia1/
│   ├── bloque1/   🟢 ¿Qué es BDD y Gherkin?
│   ├── bloque2/   🟢 Instalación y primer .feature
│   ├── bloque3/   🟢 Ejercicio práctico básico
│   ├── bloque4/   🔵 Scenario Outline y parametrización
│   └── bloque5/   🔵 Hooks y environment.py
├── dia2/
│   ├── bloque6/   🔵 Tags, Background y organización
│   ├── bloque7/   🔵 Mocking con unittest.mock
│   ├── bloque8/   🟠 Gherkin en contexto automotriz (CAN/LIN)
│   ├── bloque9/   🟠 Proyecto integrador: rover C2V2
│   └── bloque10/  🟠 Reportes y buenas prácticas
└── .vscode/
    └── settings.json
```

---

## 🗓️ Plan de 2 días

### Día 1 — Básico + Intermedio (~3.5 hrs)
| Bloque | Tema | Tiempo |
|--------|------|--------|
| 1 | ¿Qué es BDD y Gherkin? Feature, Scenario, Given/When/Then | 45 min |
| 2 | Instalación de Behave, estructura de proyecto, primer `.feature` | 45 min |
| 3 | Ejercicio práctico: assertions, context, output | 45 min |
| ☕ | Descanso | 15 min |
| 4 | Scenario Outline, Examples table, tipos de datos | 45 min |
| 5 | Hooks: before/after scenario, environment.py | 45 min |

### Día 2 — Intermedio + Avanzado (~3.5 hrs)
| Bloque | Tema | Tiempo |
|--------|------|--------|
| 6 | Tags, filtrado de scenarios, Background | 45 min |
| 7 | Mocking con `unittest.mock`, aislar dependencias | 45 min |
| 8 | Gherkin en contexto automotriz: CAN/LIN con `python-can` | 45 min |
| ☕ | Descanso | 15 min |
| 9 | Proyecto integrador: rover C2V2, INA219, CAN bus | 45 min |
| 10 | Reportes: Allure, JSON, integración CI | 30 min |

---

## ▶️ Cómo ejecutar los tests

Desde la carpeta de cualquier bloque que tenga un proyecto Behave:

```bash
# Ejecutar todos los tests
behave

# Ejecutar con output detallado
behave --no-capture -v

# Ejecutar solo un .feature
behave features/nombre.feature

# Ejecutar por tag
behave --tags=@smoke
```

---

## 📖 Recursos

- [Documentación oficial de Behave](https://behave.readthedocs.io/)
- [Referencia de Gherkin](https://cucumber.io/docs/gherkin/reference/)
- [python-can docs](https://python-can.readthedocs.io/)
