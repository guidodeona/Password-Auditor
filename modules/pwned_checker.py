import hashlib
import requests

def check_pwned_password(password):
    """
    Verifica si una contraseña ha sido comprometida usando la API de Have I Been Pwned
    Usa k-anonymity: solo envía los primeros 5 caracteres del hash SHA-1
    
    Returns:
        tuple: (is_pwned: bool, count: int)
        - is_pwned: True si la contraseña fue encontrada en brechas
        - count: Número de veces que apareció en brechas (0 si no fue encontrada)
    """
    
    # Calcular SHA-1 hash de la contraseña
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    
    # Tomar los primeros 5 caracteres del hash
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]
    
    try:
        # Hacer request a la API de HIBP
        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        response = requests.get(url, timeout=3)
        
        if response.status_code == 200:
            # Buscar el sufijo en la respuesta
            hashes = response.text.splitlines()
            
            for hash_line in hashes:
                hash_suffix, count = hash_line.split(':')
                if hash_suffix == suffix:
                    return True, int(count)
            
            # No se encontró en las brechas
            return False, 0
        else:
            # Error en la API, asumir que no está comprometida
            return False, -1
            
    except requests.exceptions.RequestException:
        # Error de conexión, asumir que no está comprometida
        return False, -1
    except Exception:
        # Cualquier otro error
        return False, -1

def format_pwned_result(is_pwned, count):
    """
    Formatea el resultado de la verificación de forma legible
    
    Args:
        is_pwned: Si la contraseña fue encontrada
        count: Número de veces que apareció
        
    Returns:
        str: Mensaje formateado
    """
    if count == -1:
        return "No se pudo verificar (sin conexión)"
    elif is_pwned:
        if count > 1000000:
            return f"CRITICO: Aparece {count:,} veces en brechas"
        elif count > 100000:
            return f"MUY ALTO: Aparece {count:,} veces en brechas"
        elif count > 10000:
            return f"ALTO: Aparece {count:,} veces en brechas"
        elif count > 1000:
            return f"MEDIO: Aparece {count:,} veces en brechas"
        else:
            return f"BAJO: Aparece {count:,} veces en brechas"
    else:
        return "No encontrada en brechas conocidas"
