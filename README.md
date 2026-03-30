# 🏦 Simulador de Banco en Consola (Python)

## 📌 Descripción
Este proyecto consiste en el desarrollo de un simulador bancario en consola utilizando Python.

Permite administrar cuentas bancarias mediante operaciones fundamentales como crear cuentas, consultar saldo, depositar, retirar, transferir entre cuentas y visualizar el historial de movimientos, incorporando persistencia de datos mediante archivos JSON.

---

## 🎯 Objetivo
Consolidar los conocimientos de Python aplicando estructuras de datos más complejas, como listas dentro de diccionarios, y reforzar la lógica de programación construyendo una aplicación funcional con múltiples entidades relacionadas.

---

## ⚙️ Funcionalidades

### ➕ Crear cuenta
- Solicita nombre del titular
- Solicita saldo inicial (mínimo $100)
- Genera un número de cuenta único automático
- Registra la cuenta en el sistema

### 📋 Mostrar cuentas
- Lista todas las cuentas registradas
- Muestra:
  - Número de cuenta
  - Titular
  - Saldo actual

### 💰 Depositar
- Selecciona cuenta por número de cuenta
- Solicita monto a depositar (debe ser mayor a $0)
- Actualiza el saldo
- Registra el movimiento en el historial

### 💸 Retirar
- Selecciona cuenta por número de cuenta
- Solicita monto a retirar (debe ser mayor a $0)
- Valida que haya saldo suficiente
- Actualiza el saldo
- Registra el movimiento en el historial

### 🔄 Transferir
- Selecciona cuenta origen por número de cuenta
- Selecciona cuenta destino por número de cuenta
- Valida que origen y destino no sean la misma cuenta
- Solicita monto a transferir
- Valida que haya saldo suficiente en la cuenta origen
- Actualiza ambos saldos
- Registra el movimiento en el historial de ambas cuentas

### 📜 Historial de movimientos
- Selecciona cuenta por número de cuenta
- Muestra todos los movimientos de esa cuenta:
  - Tipo de movimiento (Depósito / Retiro / Transferencia enviada / Transferencia recibida)
  - Monto
  - Saldo resultante

### 🚪 Salir
- Finaliza la ejecución del programa
- Guarda automáticamente los datos en archivo JSON

---

## 🧠 Estructura de datos

Cada cuenta se representa como un diccionario con la siguiente estructura:
```python
{
    "numero_cuenta": 1001,
    "titular": "Owen Rojas",
    "saldo": 5000.0,
    "historial": [
        {
            "tipo": "Depósito",
            "monto": 1000.0,
            "saldo_resultante": 5000.0
        }
    ]
}
```

---

## 🧠 Estructura del programa

El sistema incluye:

- Menú interactivo en consola
- Uso de listas para almacenar cuentas
- Uso de diccionarios para representar cada cuenta
- Listas dentro de diccionarios para el historial de movimientos
- Persistencia de datos mediante archivos JSON
- Separación en módulos para mejor organización
- Funciones independientes para cada operación

---

## 🛠️ Tecnologías utilizadas

- Python 3
- JSON (para almacenamiento de datos)

---

## 📚 Conceptos aplicados

- Variables
- Listas
- Diccionarios
- Listas dentro de diccionarios
- Funciones (`def`)
- Condicionales (`if`, `elif`, `else`)
- Ciclos (`while`, `for`)
- Manejo de archivos (`json`)
- Validación de datos
- Modularización del código

---

## 📂 Estructura del proyecto
```
SimuladorBanco-py/
├── main.py            → Menú principal del sistema
├── funciones.py       → Lógica del programa (crear, mostrar, depositar, retirar, transferir, historial)
├── validaciones.py    → Funciones auxiliares de validación de entradas
├── data.json          → Almacenamiento de cuentas
└── README.md          → Documentación del proyecto
```

---

## 🚀 Cómo ejecutar

1. Clonar el repositorio:
```bash
   git clone https://github.com/owen-rodriguez-rojas/SimuladorBanco-py
```

2. Entrar al proyecto:
```bash
   cd SimuladorBanco-py
```

3. Ejecutar el programa:
```bash
   python main.py
```

---

## 💡 Pistas para el desarrollo

- El número de cuenta puede empezar en 1001 e incrementarse automáticamente igual que hiciste con los IDs.
- El saldo y los montos deben ser `float`, no `int`, para manejar centavos.
- Para validar montos usa una función auxiliar en `validaciones.py` similar a `insert_id_or_num` pero que acepte decimales. Investiga `float()` y cómo manejar excepciones con `try/except`.
- El historial es simplemente una lista de diccionarios dentro de cada cuenta. Cada vez que haya un movimiento, haces `append` de un nuevo diccionario al historial de esa cuenta.
- En la transferencia necesitas encontrar dos cuentas al mismo tiempo. Piensa cómo reutilizar tu lógica de búsqueda por ID.
- Reutiliza tu `validaciones.py` del ToDoList como base.

---

## 🎓 Aprendizajes esperados

Durante este proyecto desarrollarás habilidades como:

- Manejo de estructuras de datos anidadas (listas dentro de diccionarios)
- Relaciones entre entidades (movimiento pertenece a una cuenta)
- Validaciones más complejas (saldo suficiente, cuentas distintas)
- Manejo de números decimales
- Manejo básico de excepciones con `try/except`
- Lógica de negocio aplicada

---

## 🚀 Próximas mejoras
- Agregar fechas a los movimientos con `datetime`
- Agregar tipos de cuenta (ahorro, corriente)
- Agregar PIN de seguridad por cuenta
- Interfaz gráfica (Tkinter)
- Versión web (Flask o FastAPI)

---

## 🧑‍💻 Autor
- Owen Rojas
