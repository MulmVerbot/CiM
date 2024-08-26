import subprocess
import sys
import os

def run_main():
    # Pfad zur main.py Datei im selben Verzeichnis
    script_path = os.path.join(os.path.dirname(__file__), "main.py")
    
    # Überprüfen, ob die Datei existiert
    if not os.path.exists(script_path):
        print(f"Die Datei {script_path} existiert nicht.")
        return
    
    # Python-Befehl zur Ausführung des Scripts
    command = [sys.executable, script_path]
    
    try:
        # Ausführen des Befehls mit verstecktem Terminalfenster
        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
            creationflags=subprocess.CREATE_NO_WINDOW  # Versteckt das Terminalfenster
        )
        print(result.stdout)  # Ausgabe des Scripts anzeigen
    except subprocess.CalledProcessError as e:
        print(f"Fehler beim Ausführen von {script_path}: {e}")
        print(e.stderr)  # Fehlerausgabe anzeigen

if __name__ == "__main__":
    run_main()
