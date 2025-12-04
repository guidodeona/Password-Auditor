import pandas as pd
from datetime import datetime

def generate_report(results, output_csv="audit_report.csv", output_html="audit_report.html"):
    """Genera reportes en formato CSV y HTML"""
    
    if not results:
        print("[WARN] No hay resultados para generar reporte")
        return
    
    # Crear DataFrame
    df = pd.DataFrame(results)
    
    # Guardar CSV
    df.to_csv(output_csv, index=False, encoding='utf-8-sig')
    print(f"[OK] Reporte CSV guardado en: {output_csv}")
    
    # Generar HTML
    html_content = generate_html_report(results)
    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"[OK] Reporte HTML guardado en: {output_html}")

def generate_html_report(results):
    """Genera un reporte HTML con estilo profesional"""
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Password Audit Report</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            min-height: 100vh;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        
        .header p {{
            opacity: 0.9;
            font-size: 1.1em;
        }}
        
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 30px;
            background: #f8f9fa;
        }}
        
        .stat-card {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        
        .stat-card h3 {{
            color: #667eea;
            font-size: 2em;
            margin-bottom: 5px;
        }}
        
        .stat-card p {{
            color: #666;
            font-size: 0.9em;
        }}
        
        .results {{
            padding: 30px;
        }}
        
        .password-card {{
            background: white;
            border: 2px solid #e9ecef;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            transition: all 0.3s ease;
        }}
        
        .password-card:hover {{
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            transform: translateY(-2px);
        }}
        
        .password-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
        }}
        
        .password-text {{
            font-family: 'Courier New', monospace;
            font-size: 1.2em;
            font-weight: bold;
        }}
        
        .badge {{
            padding: 8px 16px;
            border-radius: 20px;
            font-weight: bold;
            font-size: 0.9em;
        }}
        
        .badge-muy-debil {{
            background: #ff4444;
            color: white;
        }}
        
        .badge-debil {{
            background: #ff8800;
            color: white;
        }}
        
        .badge-media {{
            background: #ffbb33;
            color: white;
        }}
        
        .badge-fuerte {{
            background: #00C851;
            color: white;
        }}
        
        .badge-muy-fuerte {{
            background: #007E33;
            color: white;
        }}
        
        .info-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-top: 15px;
        }}
        
        .info-item {{
            background: #f8f9fa;
            padding: 10px;
            border-radius: 5px;
        }}
        
        .info-label {{
            font-size: 0.8em;
            color: #666;
            margin-bottom: 5px;
        }}
        
        .info-value {{
            font-weight: bold;
            color: #333;
        }}
        
        .recommendations {{
            margin-top: 15px;
            padding: 15px;
            background: #fff3cd;
            border-left: 4px solid #ffc107;
            border-radius: 5px;
        }}
        
        .recommendations h4 {{
            color: #856404;
            margin-bottom: 10px;
        }}
        
        .recommendations ul {{
            list-style: none;
            padding-left: 0;
        }}
        
        .recommendations li {{
            padding: 5px 0;
            color: #856404;
        }}
        
        .footer {{
            text-align: center;
            padding: 20px;
            background: #f8f9fa;
            color: #666;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔐 Password Audit Report</h1>
            <p>Análisis de Seguridad de Contraseñas</p>
            <p style="font-size: 0.9em; margin-top: 10px;">Generado: {timestamp}</p>
        </div>
        
        <div class="stats">
            <div class="stat-card">
                <h3>{len(results)}</h3>
                <p>Contraseñas Analizadas</p>
            </div>
            <div class="stat-card">
                <h3>{sum(1 for r in results if r.get('nivel') in ['Fuerte', 'Muy Fuerte'])}</h3>
                <p>Contraseñas Fuertes</p>
            </div>
            <div class="stat-card">
                <h3>{sum(1 for r in results if r.get('comun', False))}</h3>
                <p>Contraseñas Comprometidas</p>
            </div>
            <div class="stat-card">
                <h3>{sum(1 for r in results if r.get('nivel') in ['Muy Débil', 'Débil'])}</h3>
                <p>Requieren Atención</p>
            </div>
        </div>
        
        <div class="results">
            <h2 style="margin-bottom: 20px; color: #333;">Resultados Detallados</h2>
"""
    
    for result in results:
        nivel = result.get('nivel', 'Desconocido')
        badge_class = f"badge-{nivel.lower().replace(' ', '-')}"
        
        html += f"""
            <div class="password-card">
                <div class="password-header">
                    <span class="password-text">{result.get('password', 'N/A')}</span>
                    <span class="badge {badge_class}">{nivel}</span>
                </div>
                
                <div class="info-grid">
                    <div class="info-item">
                        <div class="info-label">Puntuación</div>
                        <div class="info-value">{result.get('score', 0)}/10</div>
                    </div>
                    <div class="info-item">
                        <div class="info-label">Tiempo de Crackeo</div>
                        <div class="info-value">{result.get('tiempo_crack_legible', 'N/A')}</div>
                    </div>
                    <div class="info-item">
                        <div class="info-label">Entropía</div>
                        <div class="info-value">{result.get('entropia', 0)} bits</div>
                    </div>
                    <div class="info-item">
                        <div class="info-label">Contraseña Común</div>
                        <div class="info-value">{'❌ Sí' if result.get('comun', False) else '✅ No'}</div>
                    </div>
                </div>
"""
        
        if result.get('recomendaciones'):
            html += f"""
                <div class="recommendations">
                    <h4>📋 Recomendaciones</h4>
                    <ul>
"""
            for rec in result.get('recomendaciones', []):
                html += f"                        <li>{rec}</li>\n"
            
            html += """
                    </ul>
                </div>
"""
        
        html += """
            </div>
"""
    
    html += """
        </div>
        
        <div class="footer">
            <p>🔐 Password Auditor v2.0 - Herramienta de Auditoría de Seguridad</p>
            <p>Desarrollado para análisis de seguridad y auditorías internas</p>
        </div>
    </div>
</body>
</html>
"""
    
    return html
