import json

def load_synonyms(file_path):
    """Lädt Synonyme aus einer JSON-Datei."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Datei '{file_path}' nicht gefunden.")
        return {}
    except json.JSONDecodeError:
        print(f"Fehler beim Lesen der JSON-Datei '{file_path}'.")
        return {}

def find_synonyms(word, synonyms_dict):
    """Findet Synonyme für ein gegebenes Wort."""
    word_lower = word.lower()
    for key, synonyms in synonyms_dict.items():
        key_lower = key.lower()
        synonyms_lower = [syn.lower() for syn in synonyms]
        if word_lower == key_lower or word_lower in synonyms_lower:
            return [key] + synonyms
    return []

def main():
    # Lade die Synonyme
    synonyms_dict = load_synonyms('synonyme.json')
    
    if not synonyms_dict:
        print("Es wurden keine Synonyme geladen.")
        return
    
    # Wort, nach dem gesucht wird
    search_word = input("Geben Sie ein Wort ein: ").strip()
    
    # Finde Synonyme
    synonyms = find_synonyms(search_word, synonyms_dict)
    
    if synonyms:
        print(f"Synonyme für '{search_word}': {', '.join(synonyms)}")
    else:
        print(f"Keine Synonyme für '{search_word}' gefunden.")

if __name__ == "__main__":
    main()
