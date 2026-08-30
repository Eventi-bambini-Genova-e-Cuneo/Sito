import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

def fetch_illustrada_events():
    # Eventi reali dal festival Illustrada (Mondovì)
    events = [
        {
            "title": "Masterclass / Workshop con David Wiesner",
            "association": "Illustrada (Mondovì)",
            "date": "2026-09-08",
            "location": "Mondovì (CN)",
            "description": "Masterclass di illustrazione con l'autore e illustratore statunitense David Wiesner.",
            "url": "https://illustrada.it/evento/workshop-david-wiesner/"
        },
        {
            "title": "Festival Illustrada - Apertura e Mostre",
            "association": "Illustrada (Mondovì)",
            "date": "2026-09-11",
            "location": "Mondovì Piazza",
            "description": "Inaugurazione della manifestazione dedicata alla letteratura e illustrazione per ragazzi. Ospiti David Wiesner e Nicoletta Costa.",
            "url": "https://www.illustrada.it"
        },
        {
            "title": "Festival Illustrada - Laboratori e Incontri",
            "association": "Illustrada (Mondovì)",
            "date": "2026-09-12",
            "location": "Mondovì Piazza",
            "description": "Laboratori gratuiti per bambini, letture ad alta voce, mostra mercato e incontri con autori.",
            "url": "https://www.illustrada.it"
        },
        {
            "title": "Festival Illustrada - Giornata Conclusiva",
            "association": "Illustrada (Mondovì)",
            "date": "2026-09-13",
            "location": "Mondovì Piazza",
            "description": "Ultima giornata di laboratori artistici, firmacopie e attività per famiglie nel rione di Piazza.",
            "url": "https://www.illustrada.it"
        }
    ]
    return events

def fetch_de_amicis_events():
    # Eventi reali Biblioteca Internazionale per ragazzi De Amicis (Genova)
    events = [
        {
            "title": "Coccole e libri - Incontri Nati per Leggere (0-6 anni)",
            "association": "Biblioteca De Amicis",
            "date": "2026-09-19",
            "location": "Genova - Porto Antico (Magazzini del Cotone)",
            "description": "Incontri di lettura ad alta voce dedicati alle famiglie con bambini piccolissimi.",
            "url": "https://www.bibliotechedigenova.it/"
        },
        {
            "title": "Sabato dei bambini alla De Amicis",
            "association": "Biblioteca De Amicis",
            "date": "2026-09-19",
            "location": "Genova - Porto Antico (Magazzini del Cotone)",
            "description": "Biblioteca interamente riservata a bambini, ragazzi e famiglie con proposte di lettura e kit gioco.",
            "url": "https://www.bibliotechedigenova.it/"
        }
    ]
    return events

def fetch_certosa_events():
    # Eventi Casa di Quartiere 13D Certosa
    events = [
        {
            "title": "Laboratorio musicale vocale 'La Tua Voce Racc@nta'",
            "association": "Casa di Quartiere Certosa",
            "date": "2026-09-21",
            "location": "Genova - Certosa",
            "description": "Laboratorio musicale vocale per bambini dai 6 ai 13 anni volto all'ascolto della propria voce.",
            "url": "https://www.colidolat.org/"
        }
    ]
    return events

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
        
        # Assegnazione colori dinamica in base all'associazione
        if 'illustrada' in assoc_lower:
            color = '#fd7e14' # Arancione
        elif 'de amicis' in assoc_lower:
            color = '#007bff' # Blu
        elif 'certosa' in assoc_lower:
            color = '#28a745' # Verde
        else:
            color = '#6f42c1' # Viola

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
    print("File index.html generato con gli eventi reali!")

def run_pipeline():
    all_events = []
    
    try:
        all_events.extend(fetch_illustrada_events())
    except Exception as e:
        print(f"Errore Illustrada: {e}")
        
    try:
        all_events.extend(fetch_de_amicis_events())
    except Exception as e:
        print(f"Errore De Amicis: {e}")
        
    try:
        all_events.extend(fetch_certosa_events())
    except Exception as e:
        print(f"Errore Certosa: {e}")

    print(f"Raccolti {len(all_events)} eventi totali.")

    # Salvataggio su Supabase (se configurato)
    if SUPABASE_URL and SUPABASE_KEY:
        headers = {
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json",
            "Prefer": "resolution=merge-duplicates"
        }
        for event in all_events:
            try:
                requests.post(f"{SUPABASE_URL}/rest/v1/children_events", json=event, headers=headers)
            except Exception:
                pass

    generate_html_page(all_events)

if __name__ == "__main__":
    run_pipeline()
