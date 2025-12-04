import re

def detect_patterns(password):
    """Detecta patrones comunes en contraseñas"""
    patterns = []
    
    # Secuencias numéricas
    if re.search(r'(012|123|234|345|456|567|678|789|890)', password):
        patterns.append("Secuencia numérica")
    
    # Secuencias alfabéticas
    if re.search(r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)', password.lower()):
        patterns.append("Secuencia alfabética")
    
    # Patrones de teclado
    keyboard_patterns = [
        'qwerty', 'asdfgh', 'zxcvbn', 'qwertz', 'azerty',
        '1qaz', '2wsx', '3edc', '4rfv', '5tgb'
    ]
    for pattern in keyboard_patterns:
        if pattern in password.lower():
            patterns.append(f"Patrón de teclado ({pattern})")
    
    # Repeticiones
    if re.search(r'(.)\1{2,}', password):
        patterns.append("Caracteres repetidos")
    
    # Años comunes
    if re.search(r'(19\d{2}|20\d{2})', password):
        patterns.append("Año detectado")
    
    # Palabras comunes
    common_words = ['password', 'pass', 'admin', 'user', 'root', 'test', 'demo', 'welcome']
    for word in common_words:
        if word in password.lower():
            patterns.append(f"Palabra común ({word})")
    
    # Nombres comunes
    common_names = ['maria', 'juan', 'pedro', 'ana', 'jose', 'luis', 'carlos', 'laura']
    for name in common_names:
        if name in password.lower():
            patterns.append(f"Nombre común ({name})")
    
    return patterns

def calculate_entropy(password):
    """Calcula la entropía de Shannon de una contraseña"""
    from collections import Counter
    import math
    
    if not password:
        return 0
    
    # Contar frecuencia de cada carácter
    counter = Counter(password)
    length = len(password)
    
    # Calcular entropía
    entropy = 0
    for count in counter.values():
        probability = count / length
        entropy -= probability * math.log2(probability)
    
    # Entropía total
    total_entropy = entropy * length
    
    return round(total_entropy, 2)

def get_charset_info(password):
    """Obtiene información sobre el conjunto de caracteres usado"""
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)
    
    charset_types = []
    if has_lower:
        charset_types.append("minúsculas")
    if has_upper:
        charset_types.append("MAYÚSCULAS")
    if has_digit:
        charset_types.append("números")
    if has_symbol:
        charset_types.append("símbolos")
    
    return charset_types
