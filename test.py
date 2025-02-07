from database import create_database, add_transaction, get_transactions

create_database()  # Erstellt die Tabelle

# Test-Daten hinzufügen
add_transaction("2025-02-07", 50.00, "Lebensmittel", "Ausgabe")
add_transaction("2025-02-07", 1000.00, "Gehalt", "Einnahme")

# Daten ausgeben
for row in get_transactions():
    print(row)
