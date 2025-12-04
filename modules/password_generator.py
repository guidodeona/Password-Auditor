import secrets
import string

def generate_password(length=16, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    """Genera una contraseña segura usando secrets (criptográficamente seguro)"""
    
    if length < 8:
        length = 8
    
    # Construir el conjunto de caracteres
    charset = ""
    if use_lower:
        charset += string.ascii_lowercase
    if use_upper:
        charset += string.ascii_uppercase
    if use_digits:
        charset += string.digits
    if use_symbols:
        charset += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    if not charset:
        charset = string.ascii_letters + string.digits
    
    # Generar contraseña
    password = ''.join(secrets.choice(charset) for _ in range(length))
    
    # Asegurar que tenga al menos un carácter de cada tipo seleccionado
    if use_lower and not any(c.islower() for c in password):
        password = secrets.choice(string.ascii_lowercase) + password[1:]
    if use_upper and not any(c.isupper() for c in password):
        password = secrets.choice(string.ascii_uppercase) + password[1:]
    if use_digits and not any(c.isdigit() for c in password):
        password = secrets.choice(string.digits) + password[1:]
    if use_symbols and not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        password = secrets.choice("!@#$%^&*()_+-=[]{}|;:,.<>?") + password[1:]
    
    # Mezclar para evitar patrones predecibles
    password_list = list(password)
    for i in range(len(password_list)):
        j = secrets.randbelow(len(password_list))
        password_list[i], password_list[j] = password_list[j], password_list[i]
    
    return ''.join(password_list)

def generate_passphrase(num_words=4, separator="-"):
    """Genera una passphrase usando palabras aleatorias"""
    # Lista de palabras comunes en español
    words = [
        "arbol", "casa", "perro", "gato", "sol", "luna", "mar", "rio",
        "monte", "valle", "flor", "rosa", "cielo", "nube", "viento", "fuego",
        "agua", "tierra", "piedra", "roca", "playa", "bosque", "selva", "campo",
        "ciudad", "pueblo", "calle", "camino", "puente", "torre", "castillo", "palacio"
    ]
    
    selected_words = [secrets.choice(words) for _ in range(num_words)]
    
    # Capitalizar aleatoriamente algunas palabras
    selected_words = [word.capitalize() if secrets.randbelow(2) else word for word in selected_words]
    
    # Agregar un número aleatorio
    passphrase = separator.join(selected_words) + str(secrets.randbelow(1000))
    
    return passphrase
