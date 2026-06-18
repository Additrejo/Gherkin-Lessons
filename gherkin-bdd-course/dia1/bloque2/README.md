# Bloque 2 · Instalación y primer .feature con Behave 🟢

## Instalación

```bash
pip install behave
```

## Estructura de un proyecto Behave

```
mi_proyecto/
└── features/
    ├── mi_feature.feature   ← escenarios en Gherkin
    └── steps/
        └── mis_steps.py     ← código Python que conecta cada paso
```

## Archivos de este bloque

| Archivo | Descripción |
|---------|-------------|
| `features/calculadora.feature` | Primer feature: suma de dos números |
| `features/steps/calculadora_steps.py` | Steps en Python conectados al feature |

## ▶️ Cómo ejecutar

```bash
cd dia1/bloque2
behave
```

## Conceptos nuevos

- `@given`, `@when`, `@then` — decoradores que conectan cada línea Gherkin a una función Python
- `context` — objeto compartido entre todos los steps de un escenario
