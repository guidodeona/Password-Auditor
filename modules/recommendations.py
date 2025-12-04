def get_recommendations(password, score, patterns, is_common):
    """Genera recomendaciones personalizadas para mejorar la contraseña"""
    recommendations = []
    
    # Longitud
    if len(password) < 8:
        recommendations.append("❌ Aumenta la longitud a mínimo 12 caracteres")
    elif len(password) < 12:
        recommendations.append("⚠️ Considera usar al menos 12-16 caracteres")
    
    # Complejidad
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)
    
    if not has_lower:
        recommendations.append("❌ Agrega letras minúsculas")
    if not has_upper:
        recommendations.append("❌ Agrega letras MAYÚSCULAS")
    if not has_digit:
        recommendations.append("❌ Agrega números")
    if not has_symbol:
        recommendations.append("⚠️ Agrega símbolos especiales (!@#$%^&*)")
    
    # Patrones detectados
    if patterns:
        recommendations.append(f"❌ Evita patrones predecibles: {', '.join(patterns)}")
    
    # Contraseña común
    if is_common:
        recommendations.append("❌ Esta contraseña está en listas de contraseñas filtradas. CÁMBIALA INMEDIATAMENTE")
    
    # Recomendaciones positivas
    if score >= 5 and not is_common and not patterns:
        recommendations.append("✅ Contraseña robusta. Considera usar un gestor de contraseñas")
    
    if not recommendations:
        recommendations.append("✅ Contraseña aceptable, pero siempre se puede mejorar")
    
    return recommendations

def get_strength_emoji(classification):
    """Retorna un emoji según la clasificación"""
    emojis = {
        "Muy Débil": "🔴",
        "Débil": "🟠",
        "Media": "🟡",
        "Fuerte": "🟢",
        "Muy Fuerte": "💚"
    }
    return emojis.get(classification, "⚪")
