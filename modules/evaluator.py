import re

def strength_score(password):
    """Calcula un score de fortaleza de 0-10 basado en múltiples criterios"""
    score = 0

    # Longitud (0-3 puntos)
    length = len(password)
    if length >= 16:
        score += 3
    elif length >= 12:
        score += 2
    elif length >= 8:
        score += 1

    # Tipos de caracteres (0-4 puntos)
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=\[\]\\/'`~;]", password):
        score += 1

    # Diversidad de caracteres (0-2 puntos)
    unique_chars = len(set(password))
    if unique_chars >= length * 0.8:  # 80% de caracteres únicos
        score += 2
    elif unique_chars >= length * 0.6:  # 60% de caracteres únicos
        score += 1

    # Bonus por longitud extrema (0-1 punto)
    if length >= 20:
        score += 1

    return min(score, 10)  # Máximo 10 puntos

def classify(score):
    """Clasifica la contraseña en 5 niveles según el score"""
    if score <= 2:
        return "Muy Débil"
    elif score <= 4:
        return "Débil"
    elif score <= 6:
        return "Media"
    elif score <= 8:
        return "Fuerte"
    else:
        return "Muy Fuerte"

def is_common_password(password, wordlist):
    """Verifica si la contraseña está en la lista de contraseñas comunes"""
    return password.lower() in wordlist

