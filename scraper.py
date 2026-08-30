import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

def load_events_from_json():
    try:
        with open("events.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Errore nella lettura del file events.json: {e}")
        return []

def generate_html_page(events):
    html_content = """<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calendario Eventi per Famiglie</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #f0f2f5; color: #3c4043; margin: 0; padding: 20px; }
        .container { max-width: 900px; margin: 0 auto; background: white; padding: 30px; border-radius: 12px; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
        h1 { color: #1a73e8; margin-bottom: 5px; font-size: 1.8rem; display: flex; align-items: center; gap: 10px; }
        p.subtitle { color: #5f6368; margin-top: 0; margin-bottom: 30px; font-size: 1rem; }
        .calendar-list { display: flex; flex-direction: column; gap: 12px; }
        .event-card { display: flex; background: #fff; border: 1px solid #dadce0; border-radius: 8px; overflow: hidden; box-shadow: 0 1px 2px rgba(0,7,12,0.05); transition: all 0.2s ease; }
        .event-card:hover { box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
        .event-date-box { background: #f8f9fa; min-width: 110px; padding: 15px; display: flex; flex-direction: column; align-items: center; justify-content: center; border-right: 1px solid #dadce0; text-align: center; }
        .event-day { font-size: 1.4rem; font-weight: bold; color: #202124; }
        .event-month { font-size: 0.85rem; text-transform: uppercase; font-weight: 600; color: #5f6368; }
        .event-details { padding: 15px 20px; flex-grow: 1; display: flex; flex-direction: column; justify-content: center; border-left: 6px solid #dadce0; }
        .event-header-line { display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px; }
        .event-association { font-size: 0.75rem; text-transform: uppercase; font-weight: bold; letter-spacing: 0.5px; }
        .event-title { font-size: 1.15rem; font-weight: 600; color: #202124; margin-bottom: 6px; text-decoration: none; }
        .event-title:hover { color: #1a73e8; text-decoration: underline; }
        .event-location { font-size: 0.85rem; color: #5f6368; margin-bottom: 6px; }
        .event-description { font-size: 0.95rem; color: #3c4043; line-height: 1.4; }
    </style>
</head>
<body>
<div class="container">
    <h1>📅 Calendario Eventi per Famiglie</h1>
    <p class="subtitle">Genova, Cuneo e Valli Monregalesi — Gestito tramite eventi condivisi</p>
    <div class="calendar-list">
"""

    months_map = {
        "01": "GEN", "02": "FEB", "03": "MAR", "04": "APR", 
        "05": "MAG", "06": "GIU", "07": "LUG", "08": "AGO", 
        "09": "SET", "10": "OTT", "11": "NOV", "12": "DIC"
    }

    for event in sorted(events, key=lambda x: x.get('date', '')):
        assoc = event.get('association', 'Altro')
        assoc_lower = assoc.lower()
        
        # Mappatura colori in stile Google Calendar
        if 'illustrada' in assoc_lower:
            color = '#f29900' # Arancione Google
        elif 'de amicis' in assoc_lower:
            color = '#1a73e8' # Blu Google
        elif 'certosa' in assoc_lower:
            color = '#34a853' # Verde Google
        elif 'officina' in assoc_lower:
            color = '#e52592' # Rosa
        elif 'kora' in assoc_lower:
            color = '#9334e6' # Viola
        elif 'vega' in assoc_lower:
            color = '#00acc1' # Cyan
        else:
            color = '#70757a' # Grigio scuro

        date_str = event.get('date', '')
        try:
            parts = date_str.split('-')
            year, month, day = parts[0], parts[1], parts[2]
            month_name = months_map.get(month, 'MES')
        except:
            day, month_name = "--", "ND"

        title = event.get('title', '')
        url = event.get('url', '')
        title_html = f'<a href="{url}" target="_blank" class="event-title">{title}</a>' if url else f'<div class="event-title">{title}</div>'

        html_content += f"""
        <div class="event-card">
            <div class="event-date-box">
                <span class="event-day">{day}</span>
                <span class="event-month">{month_name}</span>
            </div>
            <div class="event-details" style="border-left-color: {color};">
                <div class="event-header-line">
                    <span class="event-association" style="color: {color};">{assoc}</span>
                </div>
                {title_html}
                <div class="event-location">📍 {event.get('location', '')}</div>
                <div class="event-description">{event.get('description', '')}</div>
            </div>
        </div>
"""

    html_content += """
    </div>
</div>
</body>
</html>
"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Pagina generata in stile Google Calendar!")

def run_pipeline():
    events = load_events_from_json()
    generate_html_page(events)

if __name__ == "__main__":
    run_pipeline()
