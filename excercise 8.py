#1

import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    database="airports",
    user="nirajan",
    password="pass_word"
)



try:
    cursor = connection.cursor(dictionary=True)

    ident = input("Enter the ICAO code of the airport: ").upper()

    query = "SELECT name, municipality FROM airports WHERE ident = %s"
    cursor.execute(query, (ident,))
    result = cursor.fetchone()

    if result:
        print(f"Airport Name: {result['name']}\nLocation (Town): {result['municipality']}")
    else:
        print(f"No airport found with ICAO code {ident}.")
finally:
    cursor.close()
    connection.close()

print()

#2






import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    database="airports",
    user="nirajan",
    password="pass_word"
)


cursor = connection.cursor(dictionary=True)



country_code = input("Enter the country code : ").upper()


query = """
    SELECT type, COUNT(*) as airport_count
    FROM airports
    WHERE iso_country = %s
    GROUP BY type
    ORDER BY type
"""


cursor.execute(query, (country_code,))
results = cursor.fetchall()


if results:
    print(f"Airports in country {country_code}:")
    for row in results:
        print(f"Airport Type: {row['type']}, Count: {row['airport_count']}")
else:
    print(f"No airports found for country code {country_code}.")


cursor.close()
connection.close()