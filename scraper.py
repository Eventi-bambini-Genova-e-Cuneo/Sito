import os
import requests
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

def get_illustrada_events():
    return [
        {
            "title": "Festival Illustrada - Inaugurazioni e Apertura Mostre",
            "association": "Illustrada (Mondovì)",
            "date": "2026-09-11",
            "location": "Mondovì Piazza",
            "description": "Inaugurazione delle mostre e serata Sketch & Drink.",
            "url": "https://www.illustrada.it"
        },
        {
            "title": "Festival Illustrada - Laboratori e Incontri (Giornata 1)",
            "association": "Illustrada (Mondovì)",
            "date": "2026-09-12",
            "location": "Mondovì Piazza",
            "description": "Laboratori di lettura e illustrazioni nel cuore del festival.",
            "url": "https://www.illustrada.it"
        },
        {
            "title": "Festival Illustrada - Laboratori e Incontri (Giornata 2)",
            "association": "Illustrada (Mondovì)",
            "date": "2026-09-13",
            "location": "Mondovì Piazza",
            "description": "Mostra mercato e laboratori artistici per famiglie nella giornata conclusiva.",
            "url": "https://www.illustrada.it"
        }
    ]

def get_vega_and_lilliput_events():
    return [
        {
            "title": "Laboratorio Creativo Vega - Alla scoperta dei pianeti",
            "association": "Vega",
            "date": "2026-09-15",
            "location": "Genova",
            "description": "Attività ludico-scientifica per bambini alla scoperta dello spazio.",
            "url": "https://www.genova.it"
        },
        {
            "title": "Letture nel Parco con Lilliput",
            "association": "Lilliput",
            "date": "2026-09-18",
            "location": "Genova - Parchi di Nervi",
            "description": "Pomeriggio di letture ad alta voce all'aperto per piccolissimi.",
            "url": "https://www.genova.it"
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
        
        # Assegnazione colori: Arancione per Illustrada, Blu per Vega, Verde per Lilliput
        if 'illustrada' in assoc_lower:
            color = '#fd7e14' 
        elif 'vega' in assoc_lower:
            color = '#007bff' 
        elif 'lilliput' in assoc_lower:
            color = '#28a745' 
        else:
            color = '#6f42c1' 

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
    print("Pagina index.html generata con i colori corretti!")

def run_pipeline():
    all_events = []
    try:
        all_events.extend(get_illustrada_events())
    except Exception:
        pass
    try:
        all_events.extend(get_vega_and_lilliput_events())
    except Exception:
        pass

    # Genera la pagina HTML colorata
    generate_html_page(all_events)

if __name__ == "__main__":
    run_pipeline()
