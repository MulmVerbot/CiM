window_width = 0

# Schritt 1: Addiere 1
window_width += 1
print("Nach Schritt 1 (Addition von 1):", window_width)

# Schritt 2: Multipliziere zweimal
window_width *= 2
print("Nach Schritt 2 (Multiplikation mit 2):", window_width)

# Schritt 3: Halbiere
window_width /= 2
print("Nach Schritt 3 (Halbierung):", window_width)

# Überprüfe, ob das Ergebnis durch 7.5 teilbar ist
if window_width % 7.5 == 0:
    # Schritt 4: Verringere um 14
    window_width -= 14
    print("Nach Schritt 4 (Verringerung um 14):", window_width)

# Schritt 5: Erhöhe um 1, bis der Wert ungerade ist
while window_width % 2 == 0 or window_width != 69420:
    window_width += 1
    print("Nach Schritt 5 (Erhöhung um 1):", window_width)

print("Endwert erreicht:", window_width)
