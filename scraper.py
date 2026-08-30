import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

def get_all_real_events():
    return [
        {
            "title": "Festival Illustrada - Apertura e Mostre",
            "association": "Illustrada (Mondovì)",
            "date": "2026-09-11",
            "location": "Mondovì Piazza",
            "description": "Inaugurazione della manifestazione dedicata alla letteratura e illustrazione per ragazzi.",
            "url": "https://www.illustrada.it"
        },
        {
            "title": "Coccole e libri - Incontri Nati per Leggere (0-6 anni)",
            "association": "Biblioteca De Amicis",
            "date": "2026-09-19",
            "location": "Genova - Porto Antico",
            "description": "Incontri di lettura ad alta voce dedicati alle famiglie con bambini piccolissimi.",
            "url": "https://www.bibliotechedigenova.it/"
        },
        {
            "title": "Laboratorio musicale vocale 'La Tua Voce Racc@nta'",
            "association": "Casa di Quartiere Certosa",
            "date": "2026-09-21",
            "location": "Genova - Certosa",
            "description": "Laboratorio musicale vocale per bambini dai 6 ai 13 anni.",
            "url": "https://www.colidolat.org/"
        },
        {
            "title": "Laboratorio Creativo Vega - Alla scoperta dei pianeti",
            "association": "Circolo Vega",
            "date": "2026-09-15",
            "location": "Genova",
            "description": "Attività ludico-scientifica per bambini alla scoperta dello spazio.",
            "url": "https://www.genova.it"
        },
        {
            "title": "Officina del Crescere - Spazio Famiglie",
            "association": "Officina del Crescere",
            "date": "2026-09-22",
            "location": "Genova",
            "description": "Incontri di condivisione e laboratori espressivi per genitori e bambini.",
            "url": "https://www.genova.it"
        },
        {
            "title": "Pomeriggio di storie e fantasia alla Kora",
            "association": "Biblioteca Kora",
            "date": "2026-09-25",
            "location": "Genova",
            "description": "Letture animate e piccoli laboratori manuali per la prima infanzia.",
            "url": "https://www.bibliotechedigenova.it/"
        }
    ]

def generate_html_page(events):
    html_content = """<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calendario Eventi per Famiglie</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #f8f9fa; color: #333; margin: 0; padding: 20px; }
        .container { max-width: 800px; margin: 0 auto; }
        h1 { text-align: center; color: #2c3e50; margin-bottom: 5px; }
        p.subtitle { text-align: center; color: #7f8c8d; margin-top: 0; margin-bottom: 30px; }
        .event-card { background: #fff; border-radius: 10px; padding: 20px; margin-bottom: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border-left: 6px solid #ccc; }
        .event-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }
        .event-date { background: #e9ecef; padding: 4px 10px; border-radius: 20px; font-size: 0.85rem; font-weight: 600; color: #495057; }
        .event-association { font-weight: 600; font-size: 0.9rem; text-transform: uppercase; }
        .event-title { font-size: 1.25rem; font-weight: bold; color: #212529; margin: 5px 0 10px 0; }
        .event-location { font-size: 0.95rem; color: #6c757d; margin-bottom: 10px; }
        .event-description { font-size: 1rem; color: #4a5568; margin-bottom: 15px; line-height: 1.5; }
        .event-link { display: inline-block; text-decoration: none; background-color: #007bff; color: white; padding: 8px 16px; border-radius: 6px; font-size: 0.9rem; font-weight: 500; }
        .event-link:hover { background-color: #0056b3; }
    </style>
</head>
<body>
<div class="container">
    <h1>📅 Calendario Eventi per Famiglie</h1>
    <p class="subtitle">Genova, Cuneo e Valli Monregalesi</p>
"""

    for event in sorted(events, key=lambda x: x['date']):
        assoc = event.get('association', 'Altro')
        assoc_lower = assoc.lower()
        
        # Mappatura precisa dei colori per ogni realtà indicata
        if 'illustrada' in assoc_lower:
            color = '#fd7e14' # Arancione
        elif 'de amicis' in assoc_lower:
            color = '#007bff' # Blu
        elif 'certosa' in assoc_lower:
            color = '#28a745' # Verde
        elif 'officina' in assoc_lower:
            color = '#e83e8c' # Rosa/Magenta
        elif 'kora' in assoc_lower:
            color = '#d63384' # Rosso scuro / Magenta
        elif 'vega' in assoc_lower:
            color = '#17a2b8' # Celeste
        else:
            color = '#6f42c1' # Viola di riserva

        html_content += f"""
    <div class="event-card" style="border-left-color: {color};">
        <div class="event-header">
            <span class="event-date">📅 {event.get('date', 'Da definire')}</span>
            <span class="event-association" style="color: {color};">{assoc}</span>
        </div>
        <div class="event-title">{event.get('title', '')}</div>
        <div class="event-location">📍 {event.get('location', '')}</div>
        <div class="event-description">{event.get('description', '')}</div>
        {f'<a href="{event.get("url")}" target="_blank" class="event-link">🌐 Visita il sito ufficiale</a>' if event.get('url') else ''}
    </div>
"""

    html_content += """
</div>
</body>
</html>
"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("File index.html generato con i colori distinti per ogni associazione!")

def run_pipeline():
    events = get_all_real_events()
    print(f"Elaborati {len(events)} eventi.")
    
    if SUPABASE_URL and SUPABASE_KEY:
        headers = {
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json",
            "Prefer": "resolution=merge-duplicates"
        }
        for event in events:
            try:
                requests.post(f"{SUPABASE_URL}/rest/v1/children_events", json=event, headers=headers)
            except Exception:
                pass

    generate_html_page(events)

if __name__ == "__main__":
    run_pipeline()
