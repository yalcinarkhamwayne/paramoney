import mysql.connector

# Datenbank-Verbindungsdaten
DB_CONFIG = {
    "host": "192.168.1.100",  # IP deines Unraid-Servers
    "user": "finanzuser",
    "password": "meinpasswort",
    "database": "finanzen"
}

def create_database():
    """Erstellt die Tabelle, falls sie nicht existiert."""
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transaktionen (
            id INT AUTO_INCREMENT PRIMARY KEY,
            datum DATE NOT NULL,
            betrag DECIMAL(10,2) NOT NULL,
            kategorie VARCHAR(255) NOT NULL,
            typ ENUM('Einnahme', 'Ausgabe') NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_transaction(datum, betrag, kategorie, typ):
    """Fügt eine Transaktion in die MariaDB ein."""
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    sql = "INSERT INTO transaktionen (datum, betrag, kategorie, typ) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (datum, betrag, kategorie, typ))
    conn.commit()
    conn.close()

def get_transactions():
    """Liest alle Transaktionen aus der MariaDB."""
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT datum, betrag, kategorie, typ FROM transaktionen ORDER BY datum DESC")
    data = cursor.fetchall()
    conn.close()
    return data
