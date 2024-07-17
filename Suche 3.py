import os
import re
from tkinter import filedialog
from collections import defaultdict
from nltk.corpus import wordnet
import nltk
import ssl

'''# Umgehen der Zertifikatverifizierung (nicht empfohlen für produktive Umgebungen)
ssl._create_default_https_context = ssl._create_unverified_context
nltk.download('wordnet')
nltk.download('omw')  # Dieser Befehl lädt das deutsche WordNet (GermaNet)
nltk.download('deu_lexicon')  # Dieser Befehl lädt ein deutsches Lexikon'''

def list_synonyms(word):
    synonyms = set()
    for synset in wordnet.synsets(word):
        for lemma in synset.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)

def is_text_file(file_name):
    text_extensions = {'.txt', '.rtf', '.md', '.html', '.xml', '.csv'}
    _, ext = os.path.splitext(file_name)
    return ext.lower() in text_extensions

def search_files_for_words(path, words):
    results = defaultdict(list)
    word_synonyms = defaultdict(list)
    
    for word in words:
        synonyms = list_synonyms(word)
        word_synonyms[word] = synonyms + [word]  # Include the word itself as a synonym
    
    for root, _, files in os.walk(path):
        for file in files:
            if is_text_file(file):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    for line_num, line in enumerate(f, 1):
                        for word, synonyms in word_synonyms.items():
                            pattern = r'\b({})\b'.format('|'.join(map(re.escape, synonyms)))
                            matches = re.findall(pattern, line, flags=re.IGNORECASE)
                            if matches:
                                results[word].append((file_path, line_num, line.strip()))
                            
    return results, word_synonyms

if __name__ == "__main__":
    path = filedialog.askdirectory()
    words = input("Geben Sie die Wörter (getrennt durch Leerzeichen) ein, nach denen gesucht werden soll: ").strip().split()
    
    if not os.path.isdir(path):
        print("Der angegebene Pfad existiert nicht oder ist kein Verzeichnis.")
    else:
        results, word_synonyms = search_files_for_words(path, words)
        
        if not results:
            print("Keine Ergebnisse gefunden.")
        else:
            for word, occurrences in results.items():
                print(f"\nWort: {word}")
                print(f"   Synonyme: {', '.join(word_synonyms[word])}")
                for occurrence in occurrences:
                    print(f"   Datei: {occurrence[0]}")
                    print(f"   Zeile {occurrence[1]}: {occurrence[2]}")
