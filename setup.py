import nltk
import ssl
try:
    nltk.download('wordnet')
    nltk.download('omw')  # Dieser Befehl lädt das deutsche WordNet (GermaNet)
    nltk.download('deu_lexicon')  # Dieser Befehl lädt ein deutsches Lexikon
    print("fertig")
except:
    # Umgehen der Zertifikatverifizierung (nicht empfohlen für produktive Umgebungen)
    ssl._create_default_https_context = ssl._create_unverified_context
    nltk.download('wordnet')
    nltk.download('omw')  # Dieser Befehl lädt das deutsche WordNet (GermaNet)
    nltk.download('deu_lexicon')  # Dieser Befehl lädt ein deutsches Lexikon
    print("fertig")