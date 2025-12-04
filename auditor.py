import os
import sys
import io

# Configurar codificación UTF-8 para Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from modules.evaluator import strength_score, classify, is_common_password
from modules.crack_time import estimate_crack_time, format_time
from modules.report import generate_report
from modules.pattern_detector import detect_patterns, calculate_entropy, get_charset_info
from modules.recommendations import get_recommendations, get_strength_emoji
from modules.password_generator import generate_password, generate_passphrase
from modules.pwned_checker import check_pwned_password, format_pwned_result

# Colores para terminal (compatible con Windows)
try:
    import colorama
    colorama.init()
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
except:
    RED = GREEN = YELLOW = BLUE = MAGENTA = CYAN = RESET = BOLD = ''

def print_banner():
    """Imprime el banner de la aplicación"""
    banner = f"""
{CYAN}{BOLD}
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║        🔐  PASSWORD AUDITOR v2.0  🔐                         ║
║                                                               ║
║        Herramienta Profesional de Auditoría de Seguridad      ║
║        Desarrollado para SOC, Blue Team y Pentesting          ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
{RESET}
"""
    print(banner)

def load_common_passwords():
    """Carga la lista de contraseñas comunes"""
    try:
        with open("data/common-passwords.txt", "r", encoding="utf8") as f:
            return [line.strip().lower() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"{YELLOW}[WARN] No se encontró el archivo de contraseñas comunes{RESET}")
        return []

def analyze_password(password, wordlist):
    """Analiza una contraseña y retorna un diccionario con todos los resultados"""
    
    # Análisis básico
    score = strength_score(password)
    classification = classify(score)
    
    # Tiempo de crackeo
    crack_seconds = estimate_crack_time(password)
    crack_time_readable = format_time(crack_seconds)
    
    # Verificar si es común
    is_common = is_common_password(password, wordlist)
    
    # Verificar contra Have I Been Pwned
    is_pwned, pwned_count = check_pwned_password(password)
    pwned_message = format_pwned_result(is_pwned, pwned_count)
    
    # Detectar patrones
    patterns = detect_patterns(password)
    
    # Calcular entropía
    entropy = calculate_entropy(password)
    
    # Información de charset
    charset_types = get_charset_info(password)
    
    # Ajustar clasificación si es común, pwned o tiene muchos patrones
    if is_common or is_pwned:
        classification = "Muy Débil"
        score = min(score, 1)
    elif len(patterns) >= 3:
        classification = "Débil"
        score = min(score, 3)
    
    # Generar recomendaciones
    recommendations = get_recommendations(password, score, patterns, is_common or is_pwned)
    
    return {
        "password": password,
        "score": score,
        "nivel": classification,
        "estimado_crack_segundos": int(crack_seconds),
        "tiempo_crack_legible": crack_time_readable,
        "comun": is_common,
        "pwned": is_pwned,
        "pwned_count": pwned_count,
        "pwned_message": pwned_message,
        "patrones": patterns,
        "entropia": entropy,
        "charset_types": charset_types,
        "recomendaciones": recommendations
    }

def print_analysis_result(result):
    """Imprime el resultado del análisis de forma visual"""
    
    emoji = get_strength_emoji(result['nivel'])
    
    # Color según nivel
    if result['nivel'] == "Muy Débil":
        color = RED
    elif result['nivel'] == "Débil":
        color = YELLOW
    elif result['nivel'] == "Media":
        color = YELLOW
    elif result['nivel'] == "Fuerte":
        color = GREEN
    else:
        color = GREEN
    
    print(f"\n{BOLD}{'='*70}{RESET}")
    print(f"{BOLD}Contraseña:{RESET} {CYAN}{result['password']}{RESET}")
    print(f"{BOLD}{'='*70}{RESET}")
    
    print(f"\n{BOLD}📊 Evaluación:{RESET}")
    print(f"  {emoji} Nivel: {color}{BOLD}{result['nivel']}{RESET}")
    print(f"  📈 Puntuación: {result['score']}/10")
    print(f"  🔢 Entropía: {result['entropia']} bits")
    print(f"  ⏱️  Tiempo estimado de crackeo: {BOLD}{result['tiempo_crack_legible']}{RESET}")
    
    if result['charset_types']:
        print(f"  🔤 Tipos de caracteres: {', '.join(result['charset_types'])}")
    
    if result['comun']:
        print(f"  {RED}{BOLD}[!] ALERTA: Contraseña encontrada en listas comunes{RESET}")
    
    # Mostrar resultado de Have I Been Pwned
    if result.get('pwned_count', -1) != -1:
        if result.get('pwned', False):
            print(f"  {RED}{BOLD}[!!!] CRITICO: {result['pwned_message']}{RESET}")
        else:
            print(f"  {GREEN}[OK] {result['pwned_message']}{RESET}")
    
    if result['patrones']:
        print(f"\n{BOLD}Patrones detectados:{RESET}")
        for pattern in result['patrones']:
            print(f"  [!] {pattern}")
    
    if result['recomendaciones']:
        print(f"\n{BOLD}💡 Recomendaciones:{RESET}")
        for rec in result['recomendaciones']:
            print(f"  {rec}")
    
    print(f"{BOLD}{'='*70}{RESET}\n")

def analyze_single_password():
    """Modo interactivo para analizar una sola contraseña"""
    print(f"\n{BOLD}{BLUE}=== Análisis de Contraseña Individual ==={RESET}\n")
    
    password = input(f"{BOLD}Ingresa la contraseña a analizar: {RESET}")
    
    if not password:
        print(f"{RED}Error: Debes ingresar una contraseña{RESET}")
        return
    
    wordlist = load_common_passwords()
    result = analyze_password(password, wordlist)
    print_analysis_result(result)
    
    # Preguntar si quiere guardar el reporte
    save = input(f"\n{BOLD}¿Guardar reporte? (s/n): {RESET}").lower()
    if save == 's':
        generate_report([result])

def analyze_batch_passwords():
    """Analiza múltiples contraseñas desde entrada manual"""
    print(f"\n{BOLD}{BLUE}=== Análisis por Lotes ==={RESET}\n")
    print("Ingresa las contraseñas (una por línea). Escribe 'FIN' para terminar:\n")
    
    passwords = []
    while True:
        pwd = input(f"{CYAN}> {RESET}")
        if pwd.upper() == 'FIN':
            break
        if pwd:
            passwords.append(pwd)
    
    if not passwords:
        print(f"{RED}No se ingresaron contraseñas{RESET}")
        return
    
    wordlist = load_common_passwords()
    results = []
    
    print(f"\n{BOLD}Analizando {len(passwords)} contraseñas...{RESET}\n")
    
    for pwd in passwords:
        result = analyze_password(pwd, wordlist)
        results.append(result)
        
        # Resumen corto
        emoji = get_strength_emoji(result['nivel'])
        print(f"{emoji} {pwd:30s} → {result['nivel']:15s} | {result['tiempo_crack_legible']}")
    
    # Generar reporte
    print(f"\n{BOLD}Generando reportes...{RESET}")
    generate_report(results)

def analyze_from_file():
    """Analiza contraseñas desde un archivo"""
    print(f"\n{BOLD}{BLUE}=== Análisis desde Archivo ==={RESET}\n")
    
    filename = input(f"{BOLD}Nombre del archivo (ej: passwords.txt): {RESET}")
    
    if not os.path.exists(filename):
        print(f"{RED}Error: El archivo '{filename}' no existe{RESET}")
        return
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            passwords = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"{RED}Error al leer el archivo: {e}{RESET}")
        return
    
    if not passwords:
        print(f"{RED}El archivo no contiene contraseñas{RESET}")
        return
    
    wordlist = load_common_passwords()
    results = []
    
    print(f"\n{BOLD}Analizando {len(passwords)} contraseñas del archivo...{RESET}\n")
    
    for pwd in passwords:
        result = analyze_password(pwd, wordlist)
        results.append(result)
        
        emoji = get_strength_emoji(result['nivel'])
        print(f"{emoji} {pwd:30s} → {result['nivel']:15s} | {result['tiempo_crack_legible']}")
    
    print(f"\n{BOLD}Generando reportes...{RESET}")
    generate_report(results)

def generate_secure_password():
    """Genera contraseñas seguras"""
    print(f"\n{BOLD}{BLUE}=== Generador de Contraseñas Seguras ==={RESET}\n")
    
    print("Selecciona el tipo de contraseña:")
    print(f"  {CYAN}1.{RESET} Contraseña alfanumérica con símbolos (recomendado)")
    print(f"  {CYAN}2.{RESET} Contraseña alfanumérica sin símbolos")
    print(f"  {CYAN}3.{RESET} Passphrase (frase de contraseña)")
    print(f"  {CYAN}4.{RESET} Personalizada")
    
    choice = input(f"\n{BOLD}Opción: {RESET}")
    
    if choice == '1':
        length = int(input(f"{BOLD}Longitud (recomendado 16-20): {RESET}") or "16")
        password = generate_password(length, True, True, True, True)
    elif choice == '2':
        length = int(input(f"{BOLD}Longitud (recomendado 16-20): {RESET}") or "16")
        password = generate_password(length, True, True, True, False)
    elif choice == '3':
        num_words = int(input(f"{BOLD}Número de palabras (recomendado 4-6): {RESET}") or "4")
        password = generate_passphrase(num_words)
    elif choice == '4':
        length = int(input(f"{BOLD}Longitud: {RESET}") or "16")
        use_upper = input(f"{BOLD}¿Incluir MAYÚSCULAS? (s/n): {RESET}").lower() == 's'
        use_lower = input(f"{BOLD}¿Incluir minúsculas? (s/n): {RESET}").lower() == 's'
        use_digits = input(f"{BOLD}¿Incluir números? (s/n): {RESET}").lower() == 's'
        use_symbols = input(f"{BOLD}¿Incluir símbolos? (s/n): {RESET}").lower() == 's'
        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
    else:
        print(f"{RED}Opción inválida{RESET}")
        return
    
    print(f"\n{GREEN}{BOLD}✅ Contraseña generada:{RESET}")
    print(f"\n{CYAN}{BOLD}    {password}{RESET}\n")
    
    # Analizar la contraseña generada
    analyze = input(f"{BOLD}¿Analizar esta contraseña? (s/n): {RESET}").lower()
    if analyze == 's':
        wordlist = load_common_passwords()
        result = analyze_password(password, wordlist)
        print_analysis_result(result)

def run_demo():
    """Ejecuta una demostración con contraseñas de ejemplo"""
    print(f"\n{BOLD}{BLUE}=== Modo Demostración ==={RESET}\n")
    
    demo_passwords = [
        "123456",
        "password",
        "Guido2024!",
        "Hola123",
        "UltraSecurePass!2025",
        "qwerty123",
        "Admin@2024",
        "MyP@ssw0rd!SecureAndLong2024"
    ]
    
    wordlist = load_common_passwords()
    results = []
    
    print(f"{BOLD}Analizando {len(demo_passwords)} contraseñas de ejemplo...{RESET}\n")
    
    for pwd in demo_passwords:
        result = analyze_password(pwd, wordlist)
        results.append(result)
        
        emoji = get_strength_emoji(result['nivel'])
        print(f"{emoji} {pwd:35s} → {result['nivel']:15s} | {result['tiempo_crack_legible']}")
    
    print(f"\n{BOLD}Generando reportes...{RESET}")
    generate_report(results)
    
    print(f"\n{GREEN}✅ Demostración completada. Revisa los archivos audit_report.csv y audit_report.html{RESET}")

def show_menu():
    """Muestra el menú principal"""
    print(f"\n{BOLD}{MAGENTA}╔════════════════════════════════════════╗{RESET}")
    print(f"{BOLD}{MAGENTA}  ║          MENÚ PRINCIPAL                ║{RESET}")
    print(f"{BOLD}{MAGENTA}  ╚════════════════════════════════════════╝{RESET}\n")
    
    print(f"  {CYAN}1.{RESET} 🔍 Analizar una contraseña")
    print(f"  {CYAN}2.{RESET} 📋 Analizar múltiples contraseñas (manual)")
    print(f"  {CYAN}3.{RESET} 📁 Analizar contraseñas desde archivo")
    print(f"  {CYAN}4.{RESET} 🎲 Generar contraseña segura")
    print(f"  {CYAN}5.{RESET} 🎯 Ejecutar demostración")
    print(f"  {CYAN}6.{RESET} ❌ Salir")
    
    print()

def main():
    """Función principal con menú interactivo"""
    print_banner()
    
    while True:
        show_menu()
        choice = input(f"{BOLD}Selecciona una opción: {RESET}")
        
        if choice == '1':
            analyze_single_password()
        elif choice == '2':
            analyze_batch_passwords()
        elif choice == '3':
            analyze_from_file()
        elif choice == '4':
            generate_secure_password()
        elif choice == '5':
            run_demo()
        elif choice == '6':
            print(f"\n{GREEN}{BOLD}¡Hasta luego! 👋{RESET}\n")
            break
        else:
            print(f"{RED}Opción inválida. Por favor selecciona 1-6.{RESET}")
        
        input(f"\n{BOLD}Presiona Enter para continuar...{RESET}")
        
        # Limpiar pantalla (opcional)
        # os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{YELLOW}Programa interrumpido por el usuario{RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{RED}Error inesperado: {e}{RESET}")
        sys.exit(1)
