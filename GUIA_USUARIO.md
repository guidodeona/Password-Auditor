# 📖 Guía de Usuario - Password Auditor v2.0

## 🎯 Inicio Rápido

### 1. Instalación

```bash
cd password-auditor
pip install -r requirements.txt
```

### 2. Ejecutar el programa

```bash
python auditor.py
```

## 📋 Funcionalidades Detalladas

### 🔍 Opción 1: Analizar una Contraseña Individual

Esta opción te permite analizar una sola contraseña en detalle.

**Pasos:**

1. Selecciona opción `1` del menú principal
2. Ingresa la contraseña que deseas analizar
3. Revisa el análisis completo que incluye:
   - Nivel de seguridad (Muy Débil a Muy Fuerte)
   - Puntuación (0-10)
   - Entropía en bits
   - Tiempo estimado de crackeo
   - Patrones detectados
   - Recomendaciones personalizadas
4. Opcionalmente guarda el reporte

**Ejemplo:**

```
Ingresa la contraseña a analizar: MyP@ssw0rd2024!
```

### 📋 Opción 2: Análisis por Lotes (Manual)

Analiza múltiples contraseñas ingresándolas manualmente.

**Pasos:**

1. Selecciona opción `2`
2. Ingresa cada contraseña en una línea nueva
3. Escribe `FIN` cuando termines
4. El programa analizará todas las contraseñas
5. Se generarán reportes CSV y HTML automáticamente

**Ejemplo:**

```
> Password123
> Admin@2024
> SecurePass!
> FIN
```

### 📁 Opción 3: Análisis desde Archivo

Procesa un archivo de texto con múltiples contraseñas.

**Pasos:**

1. Crea un archivo `.txt` con una contraseña por línea
2. Selecciona opción `3`
3. Ingresa el nombre del archivo (ej: `passwords.txt`)
4. El programa procesará todas las contraseñas
5. Se generarán reportes automáticamente

**Formato del archivo:**

```
Password1
Password2
Password3
```

**Archivo de ejemplo incluido:** `example_passwords.txt`

### 🎲 Opción 4: Generador de Contraseñas Seguras

Genera contraseñas criptográficamente seguras.

**Tipos disponibles:**

#### 1. Alfanumérica con símbolos (Recomendado)

- Incluye: A-Z, a-z, 0-9, símbolos especiales
- Longitud recomendada: 16-20 caracteres
- Ejemplo: `K9#mP@2xL$5nQ!8w`

#### 2. Alfanumérica sin símbolos

- Incluye: A-Z, a-z, 0-9
- Útil para sistemas que no aceptan símbolos
- Ejemplo: `Km9P2xL5nQ8wR3t`

#### 3. Passphrase

- Palabras aleatorias separadas por guiones
- Fácil de recordar, difícil de crackear
- Ejemplo: `Casa-Monte-Flor-Rio-847`

#### 4. Personalizada

- Tú decides qué incluir
- Máxima flexibilidad

**Después de generar:**

- Puedes analizar la contraseña generada
- Copia y guarda en un gestor de contraseñas

### 🎯 Opción 5: Modo Demostración

Ejecuta un análisis con contraseñas de ejemplo predefinidas.

**Útil para:**

- Conocer las capacidades del programa
- Entender los diferentes niveles de seguridad
- Ver ejemplos de reportes generados

**Contraseñas de ejemplo incluidas:**

- Muy débiles: `123456`, `password`
- Débiles: `qwerty123`, `Hola123`
- Medias: `Guido2024!`, `Admin@2024`
- Fuertes: `UltraSecurePass!2025`, `MyP@ssw0rd!SecureAndLong2024`

## 📊 Interpretación de Resultados

### Niveles de Seguridad

| Emoji | Nivel      | Tiempo de Crackeo | Acción Recomendada        |
| ----- | ---------- | ----------------- | ------------------------- |
| 🔴    | Muy Débil  | Segundos/Minutos  | ⚠️ CAMBIAR INMEDIATAMENTE |
| 🟠    | Débil      | Horas/Días        | ⚠️ Mejorar urgentemente   |
| 🟡    | Media      | Semanas/Meses     | ⚠️ Considerar mejorar     |
| 🟢    | Fuerte     | Años              | ✅ Aceptable              |
| 💚    | Muy Fuerte | Décadas+          | ✅ Excelente              |

### Patrones Comunes Detectados

- **Secuencia numérica**: 123, 234, 345, etc.
- **Secuencia alfabética**: abc, bcd, xyz, etc.
- **Patrón de teclado**: qwerty, asdfgh, etc.
- **Caracteres repetidos**: aaa, 111, etc.
- **Años**: 2024, 2023, 1990, etc.
- **Palabras comunes**: password, admin, user, etc.
- **Nombres comunes**: maria, juan, pedro, etc.

### Entropía

La entropía mide la aleatoriedad de la contraseña:

- **< 30 bits**: Muy débil
- **30-50 bits**: Débil
- **50-70 bits**: Media
- **70-90 bits**: Fuerte
- **> 90 bits**: Muy fuerte

## 📄 Reportes Generados

### CSV (audit_report.csv)

- Formato tabular para análisis en Excel
- Incluye todas las métricas
- Fácil de importar en otras herramientas

**Columnas:**

- password
- score
- nivel
- estimado_crack_segundos
- tiempo_crack_legible
- comun
- entropia
- patrones
- recomendaciones

### HTML (audit_report.html)

- Reporte visual profesional
- Diseño moderno con colores
- Estadísticas resumidas
- Tarjetas individuales por contraseña
- Recomendaciones destacadas

**Secciones:**

1. **Header**: Título y fecha
2. **Estadísticas**: Resumen general
3. **Resultados Detallados**: Análisis individual
4. **Footer**: Información del programa

## 💡 Mejores Prácticas

### ✅ Hacer

1. **Usar contraseñas largas** (mínimo 12 caracteres)
2. **Combinar tipos de caracteres** (mayúsculas, minúsculas, números, símbolos)
3. **Usar contraseñas únicas** para cada servicio
4. **Usar un gestor de contraseñas** (Bitwarden, 1Password, KeePass)
5. **Habilitar 2FA** siempre que sea posible
6. **Cambiar contraseñas comprometidas** inmediatamente
7. **Revisar reportes regularmente** para auditorías

### ❌ Evitar

1. **Información personal** (nombre, fecha de nacimiento, etc.)
2. **Palabras del diccionario** sin modificaciones
3. **Secuencias simples** (123456, abcdef, etc.)
4. **Patrones de teclado** (qwerty, asdfgh, etc.)
5. **Reutilizar contraseñas** entre servicios
6. **Compartir contraseñas** por email o mensajes
7. **Escribir contraseñas** en papel o archivos sin cifrar

## 🔧 Solución de Problemas

### Error: "No se encontró el archivo de contraseñas comunes"

**Solución:** Asegúrate de que existe el archivo `data/common-passwords.txt`

### Error: "El archivo 'X' no existe"

**Solución:** Verifica la ruta y nombre del archivo de contraseñas

### Los colores no se muestran correctamente

**Solución:** Asegúrate de tener instalado `colorama`:

```bash
pip install colorama
```

### Error al generar reportes HTML

**Solución:** Verifica que tienes permisos de escritura en el directorio

## 🎓 Casos de Uso Prácticos

### 1. Auditoría de Seguridad Interna

```
1. Recopilar contraseñas de usuarios (con autorización)
2. Guardarlas en un archivo .txt
3. Usar opción 3 para analizar desde archivo
4. Revisar reporte HTML para identificar vulnerabilidades
5. Generar plan de acción basado en recomendaciones
```

### 2. Evaluación de Política de Contraseñas

```
1. Generar contraseñas de ejemplo con opción 4
2. Analizar con opción 1
3. Verificar que cumplan con la política corporativa
4. Ajustar requisitos según resultados
```

### 3. Capacitación de Usuarios

```
1. Ejecutar modo demostración (opción 5)
2. Mostrar diferencias entre contraseñas débiles y fuertes
3. Enseñar a interpretar reportes
4. Practicar generación de contraseñas seguras
```

### 4. Análisis Forense

```
1. Analizar contraseñas encontradas en incidentes
2. Identificar patrones comunes
3. Generar reportes para documentación
4. Recomendar mejoras de seguridad
```

## 📞 Soporte

Para reportar problemas o sugerir mejoras:

- Revisa la documentación completa en `README.md`
- Verifica que tienes la última versión
- Asegúrate de tener todas las dependencias instaladas

## 🔄 Actualizaciones

**Versión actual: 2.0**

### Novedades v2.0:

- ✨ Interfaz interactiva mejorada
- 🔍 Detección avanzada de patrones
- 📊 Reportes HTML profesionales
- 🎲 Generador de contraseñas seguras
- 📈 Cálculo de entropía
- 💡 Recomendaciones personalizadas
- 🎨 Colores y emojis en terminal
- 📁 Análisis desde archivos

---

**¡Gracias por usar Password Auditor v2.0!** 🔐
