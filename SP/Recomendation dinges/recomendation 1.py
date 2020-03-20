import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Onjuist1!',
    database = 'spopdracht'
)
cursor = db.cursor()
cursor.execute('DROP TABLE IF EXISTS vergelijkbaar')
query = 'CREATE TABLE vergelijkbaar (product_id varchar(255) primary key, product_1 varchar(255) not null, product_2 varchar(255) not null, product_3 varchar(255) not null, product_4 varchar(255) not null)'
cursor.execute(query)

def lookalikes(zoek_naam, naam, id_lijst):
    if ' ' in zoek_naam:
        zoekenop = naam.split(' ')[0]
    else:
        zoekenop = naam[:len(zoek_naam) // 2]

    opzoeken = """SELECT id,
        (SELECT GROUP_CONCAT(id SEPARATOR ', ')
        FROM products
        WHERE name LIKE %s
        AND name != %s) as lookalikes
        FROM products
        WHERE name = %s"""
    """Bron van de regel opzoeken: https://stackoverflow.com/questions/28383546/retrieve-all-ids-where-name-like-current-name-in-one-query/28383840"""
    cursor.execute(opzoeken, ('%' + zoekenop + '%', naam, naam))

    records = cursor.fetchall()
    ids = records[0][1]
    p_id = records[0][0]

    lijst = []
    if ids != None:
        id_split = str(ids).split(', ')
        for i in id_split:
            lijst.append(i)
    if len(lijst) >= 4:
        for i in range(0, 4):
            id_lijst.append(lijst[i])
    else:
        lookalikes(zoekenop, naam, id_lijst)
    return id_lijst, p_id

cursor = db.cursor()

query = "SELECT name FROM products"

cursor.execute(query)

result = cursor.fetchall()

final_result = [list(i) for i in result]

for i in final_result:
    productnaam = i[0]

    id_lijst = []

    einde = lookalikes(productnaam, productnaam, id_lijst)

    product_1 = einde[0][0]
    product_2 = einde[0][1]
    product_3 = einde[0][2]
    product_4 = einde[0][3]
    product_id = einde[1]

    try:
        cursor = db.cursor()

        query = 'INSERT INTO vergelijkbaar (product_id, product_1, product_2, product_3, product_4) VALUES (%s, %s, %s, %s, %s)'

        cursor.execute(query, (product_id, product_1, product_2, product_3, product_4))

        db.commit()
    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    print(cursor.rowcount, 'record inserted')