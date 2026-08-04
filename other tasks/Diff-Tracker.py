import json
import os

# Name der Speicherdatei
SPEICHER_DATEI = "pokemon_booster_tracker.json"

# Sprach-Multiplikatoren (Wertstabilität)
SPRACH_FAKTOREN = {
    "1": ("Japanisch (JPN)", 1.2),
    "2": ("Englisch (ENG)", 1.0),
    "3": ("Deutsch (GER)", 0.8),
    "4": ("Sonstige (ITA/ESP/FRA)", 0.6)
}

# Zustands-Multiplikatoren (nur für Einzelkarten)
ZUSTANDS_FAKTOREN = {
    "1": ("Graded / Perfekt (PSA 10 / Black Label)", 2.5),
    "2": ("Near Mint (NM) - Wie neu", 1.0),
    "3": ("Excellent / Light Played (EX/LP) - Leichte Spuren", 0.7),
    "4": ("Played / Poor (PL/PO) - Deutliche Spuren / Beschädigt", 0.3)
}

def daten_laden():
    if os.path.exists(SPEICHER_DATEI):
        with open(SPEICHER_DATEI, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def daten_speichern(daten):
    with open(SPEICHER_DATEI, "w", encoding="utf-8") as f:
        json.dump(daten, f, indent=4, ensure_ascii=False)

def kauf_bewertung(typ, preis, seltenheit_oder_hype, sprach_faktor, zustand_faktor, booster_anzahl=1):
    if preis <= 0:
        return "Sofort zuschlagen! (Kostenlos)"

    if typ == "Set":
        # Bei Sets berechnen wir den Score basierend auf dem Preis pro Booster
        preis_pro_booster = preis / booster_anzahl
        # Ein durchschnittlicher fairer Boosterpreis liegt bei ca. 4.0€ - 4.5€ (angepasst durch Hype & Sprache)
        score = (seltenheit_oder_hype * 4.5 * sprach_faktor) / preis_pro_booster
        grenzwert = 1.0
    else:
        # Einzelkarten-Formel
        score = (seltenheit_oder_hype * 15 * sprach_faktor * zustand_faktor) / preis
        grenzwert = 0.8

    if score >= (grenzwert * 1.3):
        return "✅ Kaufen (Absolutes Schnäppchen!)"
    elif score >= grenzwert:
        return "🟡 Überlegen (Fairer Preis)"
    else:
        return "❌ Nicht kaufen (Zu teuer für diesen Zustand/Sprache/Boosterpreis)"

def artikel_hinzufuegen_oder_editieren(daten, existierender_key=None):
    if existierender_key:
        print(f"\n--- EINTRAG BEARBEITEN: {existierender_key} ---")
        altes_objekt = daten[existierender_key]
        typ = altes_objekt["typ"]
        vorgabe_name = altes_objekt["name"]
    else:
        print("\n--- NEUEN ARTIKEL TRACKEN ---")
        print("Typ auswaehlen:\n1. Einzelkarte (Single)\n2. Set / OVP")
        typ_wahl = input("Auswahl (1-2): ").strip()
        typ = "Einzelkarte" if typ_wahl == "1" else "Set"
        vorgabe_name = ""

    # Name eingeben
    name_prompt = f"Name des {typ}s [Aktuell: {vorgabe_name}]: " if existierender_key else f"Name des {typ}s: "
    name_input = input(name_prompt).strip()
    name = name_input if name_input or not existierender_key else vorgabe_name

    # Sprache auswählen
    print("\nSprache auswaehlen:")
    for key, (lang, _) in SPRACH_FAKTOREN.items():
        print(f"{key}. {lang}")
    sprach_wahl = input("Auswahl (1-4): ").strip()
    sprache, s_faktor = SPRACH_FAKTOREN.get(sprach_wahl, (altes_objekt["sprache"], 1.0) if existierender_key else ("Englisch (ENG)", 1.0))

    # Zustand oder Booster-Anzahl abfragen
    zustand, z_faktor = "OVP / Versiegelt", 1.0
    booster_anzahl = 1
    
    if typ == "Einzelkarte":
        print("\nZustand auswaehlen:")
        for key, (zust, _) in ZUSTANDS_FAKTOREN.items():
            print(f"{key}. {zust}")
        zustand_wahl = input("Auswahl (1-4): ").strip()
        zustand, z_faktor = ZUSTANDS_FAKTOREN.get(zustand_wahl, (altes_objekt["zustand"], 1.0) if existierender_key else ("Near Mint (NM) - Wie neu", 1.0))
    else:
        # NEU: Booster-Anzahl abfragen bei Sets
        try:
            booster_vorgabe = altes_objekt.get("booster_anzahl", 36) if existierender_key else 36
            booster_input = input(f"Anzahl der Booster im Set (z.B. Display=36, ETB=9) [Aktuell: {booster_vorgabe}]: ").strip()
            booster_anzahl = int(booster_input) if booster_input else booster_vorgabe
            if booster_anzahl <= 0: booster_anzahl = 1
        except ValueError:
            print("⚠️ Ungültige Booster-Anzahl, verwende Standard (36).")
            booster_anzahl = 36

    # Preis und Hype eingeben
    try:
        preis_vorgabe = altes_objekt["preis"] if existierender_key else 0.0
        preis_input = input(f"Gesamt-Preis (€) [Aktuell: {preis_vorgabe}]: ").strip()
        preis = float(preis_input) if preis_input else preis_vorgabe

        hype_vorgabe = altes_objekt["bewertung"] if existierender_key else 3
        hype_prompt = "Seltenheit (1-5)" if typ == "Einzelkarte" else "Hype des Sets (1-5)"
        hype_input = input(f"{hype_prompt} [Aktuell: {hype_vorgabe}]: ").strip()
        hype = int(hype_input) if hype_input else hype_vorgabe
    except ValueError:
        print("⚠️ Fehler: Ungültige Zahlenwerte! Vorgang abgebrochen.")
        return

    # Neuberechnung
    empfehlung = kauf_bewertung(typ, preis, hype, s_faktor, z_faktor, booster_anzahl)
    print(f"\n📊 Analyse-Ergebnis: {empfehlung}")

    # Alten Eintrag löschen bei Bearbeitung
    if existierender_key:
        del daten[existierender_key]

    # Speichern
    if typ == "Set":
        neuer_key = f"[{typ}] {name} ({sprache}) - {booster_anzahl} Booster"
    else:
        neuer_key = f"[{typ}] {name} ({sprache}) - {zustand}"
        
    daten[neuer_key] = {
        "name": name,
        "typ": typ,
        "sprache": sprache,
        "zustand": zustand,
        "booster_anzahl": booster_anzahl,
        "preis": preis,
        "bewertung": hype,
        "empfehlung": empfehlung
    }
    daten_speichern(daten)
    print(f"💾 Erfolgreich gespeichert unter: {neuer_key}")

def liste_anzeigen(daten):
    print("\n--- DEINE TRACKING-LISTE ---")
    if not daten:
        print("Noch keine Artikel in der Datenbank.")
        return []

    schluessel_liste = list(daten.keys())
    for index, key in enumerate(schluessel_liste, start=1):
        info = daten[key]
        print(f"\n[{index}] 📌 {key}")
        print(f"    Gesamtpreis: {info['preis']} €")
        if info["typ"] == "Set":
            # Berechnet den Preis pro Booster live für die Anzeige
            p_pro_b = info['preis'] / info['booster_anzahl']
            print(f"    -> Preis pro Booster: {p_pro_b:.2f} €")
        print(f"    Stufe: {info['bewertung']}/5 | Empfehlung: {info['empfehlung']}")
    
    return schluessel_liste

def eintrag_bearbeiten(daten):
    schluessel_liste = liste_anzeigen(daten)
    if not schluessel_liste: return
    try:
        wahl = int(input("\nWelche Nummer moechtest du bearbeiten? (0 zum Abbrechen): "))
        if wahl == 0: return
        if 1 <= wahl <= len(schluessel_liste):
            artikel_hinzufuegen_oder_editieren(daten, existierender_key=schluessel_liste[wahl - 1])
        else:
            print("⚠️ Ungültige Nummer.")
    except ValueError:
        print("⚠️ Bitte eine Zahl eingeben.")

# NEU: Funktion zum Löschen von Einträgen
def eintrag_loeschen(daten):
    schluessel_liste = liste_anzeigen(daten)
    if not schluessel_liste: return
    try:
        wahl = int(input("\nWelche Nummer moechtest du LÖSCHEN? (0 zum Abbrechen): "))
        if wahl == 0: return
        if 1 <= wahl <= len(schluessel_liste):
            geloeschter_key = schluessel_liste[wahl - 1]
            del daten[geloeschter_key]
            daten_speichern(daten)
            print(f"🗑️ '{geloeschter_key}' wurde erfolgreich gelöscht.")
        else:
            print("⚠️ Ungültige Nummer.")
    except ValueError:
        print("⚠️ Bitte eine Zahl eingeben.")

def main():
    daten = daten_laden()
    while True:
        print("\n=== POKÉMON TRACKER V3 (MIT BOOSTER-KALKULATOR) ===")
        print("1. Neuen Artikel bewerten & speichern")
        print("2. Gespeicherte Artikel anzeigen")
        print("3. Bestehenden Artikel bearbeiten / updaten")
        print("4. Artikel aus der Datenbank löschen")
        print("5. Beenden")
        
        auswahl = input("Auswahl (1-5): ").strip()
        
        if auswahl == "1":
            artikel_hinzufuegen_oder_editieren(daten)
        elif auswahl == "2":
            liste_anzeigen(daten)
        elif auswahl == "3":
            eintrag_bearbeiten(daten)
        elif auswahl == "4":
            eintrag_loeschen(daten)
        elif auswahl == "5":
            print("Tracker geschlossen. Viel Erfolg beim Sammeln!")
            break
        else:
            print("⚠️ Ungültige Auswahl.")

if __name__ == "__main__":
    main()
