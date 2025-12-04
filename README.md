# 🔐 Password Auditor v2.0 – Evaluador Profesional de Seguridad de Contraseñas

## 📌 Descripción

**Password Auditor v2.0** es una herramienta profesional desarrollada en Python para analizar la fortaleza de contraseñas, detectar vulnerabilidades, patrones comunes y verificar si han sido comprometidas en brechas de seguridad. Diseñada para auditorías de seguridad, equipos SOC, Blue Team y profesionales de ciberseguridad.

## ✨ Características Principales

### 🔍 Análisis Avanzado

- **Evaluación de fortaleza** con sistema de puntuación 0-10
- **Detección de patrones** (secuencias, teclado, repeticiones, años)
- **Cálculo de entropía** de Shannon
- **Estimación de tiempo de crackeo** con GPUs modernas (10B intentos/seg)
- **Verificación contra listas** de contraseñas comunes
- **🆕 Verificación contra Have I Been Pwned** - Comprueba si la contraseña ha sido comprometida en brechas conocidas
- **Análisis de charset** (tipos de caracteres utilizados)

### 📊 Reportes Profesionales

- **Reportes CSV** para análisis en Excel/Pandas
- **Reportes HTML interactivos** con diseño profesional y estadísticas
- **Visualización en tiempo real** con colores y formato
- **Recomendaciones personalizadas** para cada contraseña

### 🎲 Generador de Contraseñas

- **Contraseñas criptográficamente seguras** usando `secrets`
- **Passphrases** con palabras aleatorias
- **Personalización completa** de longitud y caracteres
- **Análisis automático** de contraseñas generadas

### 🚀 Modos de Operación

1. **Análisis individual** - Analiza una contraseña con detalles completos
2. **Análisis por lotes** - Múltiples contraseñas desde entrada manual
3. **Análisis desde archivo** - Procesa archivos con listas de contraseñas
4. **Generador de contraseñas** - Crea contraseñas seguras
5. **Modo demostración** - Ejemplos predefinidos para pruebas

## 🛠 Tecnologías

- **Python 3.7+**
- **Pandas** - Procesamiento de datos y reportes CSV
- **Colorama** - Colores en terminal (Windows/Linux/Mac)
- **Requests** - Verificación contra Have I Been Pwned API
- **Secrets** - Generación criptográficamente segura
- **Regex** - Detección de patrones

## 📦 Instalación

```bash
# Clonar el repositorio
git clone https://github.com/guidodeona/Password-Auditor.git
cd Password-Auditor

# Instalar dependencias
pip install -r requirements.txt
```

## ▶️ Uso

### Modo Interactivo (Recomendado)

```bash
python auditor.py
```

El programa mostrará un menú interactivo con todas las opciones disponibles.

### Ejemplos de Uso

#### 1. Analizar una contraseña

```
Opción: 1
Ingresa la contraseña: MyP@ssw0rd2024!
```

**Resultado:**

```
======================================================================
Contraseña: MyP@ssw0rd2024!
======================================================================

Evaluación:
  Nivel: Fuerte
  Puntuación: 8/10
  Entropía: 67.42 bits
  Tiempo estimado de crackeo: 2 años
  Tipos de caracteres: minúsculas, MAYÚSCULAS, números, símbolos
  [OK] No encontrada en brechas conocidas

Recomendaciones:
  ✅ Contraseña robusta. Considera usar un gestor de contraseñas
======================================================================
```

#### 2. Generar contraseña segura

```
Opción: 4
Tipo: 1 (alfanumérica con símbolos)
Longitud: 16
```

#### 3. Analizar desde archivo

Crea un archivo `passwords.txt` con una contraseña por línea:

```
Password123
Admin@2024
SecurePass!
```

Luego:

```
Opción: 3
Archivo: passwords.txt
```

## 🔒 Verificación de Contraseñas Comprometidas

Password Auditor v2.0 incluye integración con **Have I Been Pwned API** para verificar si tus contraseñas han sido expuestas en brechas de seguridad conocidas.

### ¿Cómo funciona?

- Usa **k-anonymity** para proteger tu privacidad
- Solo envía los primeros 5 caracteres del hash SHA-1
- No envía la contraseña completa a ningún servidor
- Verifica contra una base de datos de más de 800 millones de contraseñas comprometidas

### Niveles de Alerta

- **CRITICO**: Aparece más de 1,000,000 veces
- **MUY ALTO**: Aparece más de 100,000 veces
- **ALTO**: Aparece más de 10,000 veces
- **MEDIO**: Aparece más de 1,000 veces
- **BAJO**: Aparece menos de 1,000 veces
- **OK**: No encontrada en brechas

## 📈 Niveles de Clasificación

| Puntuación | Nivel         | Descripción                          |
| ---------- | ------------- | ------------------------------------ |
| 0-2        | 🔴 Muy Débil  | Contraseña extremadamente vulnerable |
| 3-4        | 🟠 Débil      | Fácil de crackear, requiere mejoras  |
| 5-6        | 🟡 Media      | Aceptable pero mejorable             |
| 7-8        | 🟢 Fuerte     | Buena seguridad                      |
| 9-10       | 💚 Muy Fuerte | Excelente seguridad                  |

## 📁 Estructura del Proyecto

```
password-auditor/
├── auditor.py                 # Programa principal
├── requirements.txt           # Dependencias
├── README.md                  # Documentación
├── GUIA_USUARIO.md           # Guía completa de usuario
├── .gitignore                # Archivos ignorados por Git
├── data/
│   └── common-passwords.txt   # Lista de contraseñas comunes
└── modules/
    ├── evaluator.py          # Evaluación de fortaleza
    ├── crack_time.py         # Estimación de tiempo de crackeo
    ├── report.py             # Generación de reportes
    ├── pattern_detector.py   # Detección de patrones
    ├── recommendations.py    # Sistema de recomendaciones
    ├── password_generator.py # Generador de contraseñas
    └── pwned_checker.py      # Verificación contra HIBP
```

## 🎯 Casos de Uso

- **Auditorías de seguridad internas**
- **Evaluación de políticas de contraseñas**
- **Entrenamiento de usuarios en seguridad**
- **Análisis forense de credenciales**
- **Generación de contraseñas para nuevos sistemas**
- **Compliance y reportes de seguridad**
- **Verificación de contraseñas comprometidas**

## 🔒 Mejores Prácticas

1. **Longitud mínima**: 12-16 caracteres
2. **Diversidad**: Usa mayúsculas, minúsculas, números y símbolos
3. **Evita patrones**: No uses secuencias, fechas o palabras comunes
4. **Única por servicio**: Nunca reutilices contraseñas
5. **Gestor de contraseñas**: Usa herramientas como Bitwarden, 1Password o KeePass
6. **Autenticación multifactor**: Siempre que sea posible
7. **Verifica brechas**: Usa la función de verificación contra HIBP regularmente

## 🚀 Próximas Mejoras

- [ ] Análisis de fuerza con zxcvbn
- [ ] Soporte para múltiples idiomas
- [ ] Exportación a JSON y XML
- [ ] Modo CLI no interactivo
- [ ] Análisis de políticas corporativas
- [ ] Dashboard web con Flask
- [ ] Historial de auditorías

## 👨‍💻 Autor

Desarrollado para proyectos de ciberseguridad y auditorías de seguridad.

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso educativo y profesional.

## 🙏 Agradecimientos

- **Have I Been Pwned** por proporcionar la API de verificación de contraseñas comprometidas
- Comunidad de seguridad por las mejores prácticas y recomendaciones

---

**⚠️ Disclaimer**: Esta herramienta está diseñada para auditorías de seguridad legítimas. El uso indebido de esta herramienta es responsabilidad del usuario. Las contraseñas analizadas no se almacenan ni se envían a terceros (excepto los primeros 5 caracteres del hash SHA-1 a Have I Been Pwned para verificación).
