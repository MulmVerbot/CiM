import nltk
import ssl
try:
    ssl._create_default_https_context = ssl._create_unverified_context
    nltk.download('wordnet')
    nltk.download('omw')  # Dieser Befehl lädt das deutsche WordNet (GermaNet)
    print("fertig")
except:
    print("Ohne SSL...")
    # Umgehen der Zertifikatverifizierung (nicht empfohlen für produktive Umgebungen)
    nltk.download('wordnet')
    nltk.download('omw')  # Dieser Befehl lädt das deutsche WordNet (GermaNet)
    print("fertig")