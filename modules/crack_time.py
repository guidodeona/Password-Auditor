import math

CHARSETS = {
    "lower": 26,
    "lower_upper": 52,
    "lower_upper_digits": 62,
    "full": 94
}

def estimate_crack_time(password, attempts_per_second=1e10):
    """
    Estima el tiempo de crackeo en segundos
    Asume 10 mil millones de intentos por segundo (GPU moderna)
    """
    length = len(password)

    # Detección del charset usado
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    # Determinar tamaño del charset
    charset_size = 0
    if has_symbol:
        charset_size = 94  # ASCII completo
    elif has_digit:
        if has_upper and has_lower:
            charset_size = 62  # alphanumeric
        elif has_upper or has_lower:
            charset_size = 36  # letters + digits
        else:
            charset_size = 10  # solo dígitos
    elif has_upper and has_lower:
        charset_size = 52  # letras mixtas
    elif has_upper or has_lower:
        charset_size = 26  # solo letras
    else:
        charset_size = 10  # fallback

    if charset_size == 0:
        return 0

    # Calcular combinaciones totales
    total_combinations = charset_size ** length

    # Tiempo promedio (mitad del espacio de búsqueda)
    seconds = (total_combinations / 2) / attempts_per_second

    return seconds

def format_time(seconds):
    """Convierte segundos a formato legible"""
    if seconds < 1:
        return "Instantáneo"
    elif seconds < 60:
        return f"{int(seconds)} segundos"
    elif seconds < 3600:
        minutes = int(seconds / 60)
        return f"{minutes} minuto{'s' if minutes != 1 else ''}"
    elif seconds < 86400:
        hours = int(seconds / 3600)
        return f"{hours} hora{'s' if hours != 1 else ''}"
    elif seconds < 31536000:
        days = int(seconds / 86400)
        return f"{days} día{'s' if days != 1 else ''}"
    elif seconds < 31536000000:
        years = int(seconds / 31536000)
        return f"{years} año{'s' if years != 1 else ''}"
    else:
        return "Millones de años"
