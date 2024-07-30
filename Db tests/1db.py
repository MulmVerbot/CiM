import mysql.connector
from mysql.connector import errorcode

try:
    # Verbindung zur Datenbank herstellen
    connection = mysql.connector.connect(
        host='rdbms.strato.de',
        user='dbu2812181',
        password='Dings75724!',
        database='dbs13142641'
    )

    # Cursor erstellen
    cursor = connection.cursor()

    # SQL-Abfrage vorbereiten
    add_data = ("INSERT INTO deine_tabelle "
                "(spalte1, spalte2, spalte3) "
                "VALUES (%s, %s, %s)")

    # Beispiel-Daten
    data = ('wert1', 'wert2', 'wert3')

    # SQL-Abfrage ausführen
    cursor.execute(add_data, data)

    # Änderungen in der Datenbank bestätigen
    connection.commit()

    print("Daten erfolgreich eingefügt.")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Etwas ist mit deinem Benutzername oder Passwort schiefgelaufen")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Die Datenbank existiert nicht")
    else:
        print(err)
else:
    # Verbindung und Cursor schließen
    cursor.close()
    connection.close()
