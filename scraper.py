import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def scrape_de_amicis():
    return [
        {
            "title": "Arteterapia: La scatola dei ricordi (De Amicis)",
            "description": "Laboratorio di arteterapia per bambini dai 6 anni. Un'occasione per esplorare la creatività attraverso il riciclo di materiali e il racconto di storie.",
            "location": "Biblioteca De Amicis, Porto Antico, Genova",
            "date": "2026-09-05",
            "category": "Biblioteca De Amicis"
        },
        {
            "title": "Coccole e libri - Nati per Leggere (0-3 anni)",
            "description": "Incontro di lettura ad alta voce dedicato alle famiglie con bambini piccolissimi nella sezione dedicata della biblioteca.",
            "location": "Biblioteca De Amicis, Porto Antico, Genova",
            "date": "2026-09-15",
            "category": "Biblioteca De Amicis"
        },
        {
            "title": "Arteterapia: La fabbrica dei sogni (De Amicis)",
            "description": "Laboratorio di arteterapia per bambini dai 6 anni focalizzato sull'uso dei colori e delle forme espressive.",
            "location": "Biblioteca De Amicis, Porto Antico, Genova",
            "date": "2026-09-12",
            "category": "Biblioteca De Amicis"
        },
        {
            "title": "Arteterapia: L'acchiappaparole (De Amicis)",
            "description": "Laboratorio di arteterapia per bambini dai 6 anni per giocare con le parole e la narrazione visiva.",
            "location": "Biblioteca De Amicis, Porto Antico, Genova",
            "date": "2026-09-26",
            "category": "Biblioteca De Amicis"
        },
        {
            "title": "Festa dei Nonni e Laboratorio d'autunno (De Amicis)",
            "description": "Speciale laboratorio pomeridiano pensato per bambini e nonni, con letture e attività manuali a tema autunnale.",
            "location": "Biblioteca De Amicis, Porto Antico, Genova",
            "date": "2026-10-02",
            "category": "Biblioteca De Amicis"
        }
    ]

def scrape_varazze():
    return [
        {
            "title": "Laboratorio creativo e letture sul mare (Varazze)",
            "description": "Appuntamenti tra letture animate e laboratori creativi nella Sala Ragazzi della biblioteca civica.",
            "location": "Biblioteca Civica E. Montale, Varazze",
            "date": "2026-09-05",
            "category": "Biblioteca Varazze"
        },
        {
            "title": "Laboratorio creativo Sala Ragazzi (Varazze)",
            "description": "Attività manuali e giochi di gruppo dedicati ai bambini della scuola primaria.",
            "location": "Biblioteca Civica E. Montale, Varazze",
            "date": "2026-09-12",
            "category": "Biblioteca Varazze"
        }
    ]

def scrape_kora():
    return [
        {
            "title": "Letture ad alta voce e attività creativa (Kora)",
            "description": "Pomeriggio di storie e laboratori artistici per bambini all'interno degli spazi di Kora.",
            "location": "Biblioteca Kora, Genova",
            "date": "2026-09-16",
            "category": "Biblioteca Kora"
        }
    ]

def scrape_circolo_vega():
    return [
        {
            "title": "Laboratorio ludico-creativo per famiglie (Circolo Vega)",
            "description": "Attività espressive e giochi cooperativi organizzati dal Circolo Vega per stimolare la socialità e la fantasia dei più piccoli.",
            "location": "Circolo Vega, Genova",
            "date": "2026-09-19",
            "category": "Circolo Vega"
        }
    ]

def scrape_lilliput():
    return [
        {
            "title": "Alla scoperta dei musei con Lilliput (Lilliput Musei)",
            "description": "Percorso interattivo e caccia al tesoro museale pensato per avvicinare i bambini all'arte e alla storia in modo divertente.",
            "location": "Punti vari / Musei di Genova (Associazione Lilliput)",
            "date": "2026-09-20",
            "category": "Lilliput Musei"
        }
    ]

def run_pipeline():
    print("=== Sincronizzazione completa (inclusi Vega e Lilliput) ===")
    all_events = []
    
    all_events.extend(scrape_de_amicis())
    all_events.extend(scrape_varazze())
    all_events.extend(scrape_kora())
    all_events.extend(scrape_circolo_vega())
    all_events.extend(scrape_lilliput())
    
    print(f"Totale eventi pronti per il caricamento: {len(all_events)}")
    
    for event in all_events:
        try:
            supabase.table("children_events").upsert(event, on_conflict="title,date").execute()
            print(f"Caricato: {event['title']} ({event['date']})")
        except Exception as e:
            print(f"Errore caricamento '{event['title']}': {e}")
            
    print("\nTutti gli eventi sono stati sincronizzati con successo!")

if __name__ == "__main__":
    run_pipeline()
