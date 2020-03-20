import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '***',
    database = 'spopdracht'
)

eenid = set()
dict = {}

cursor = db.cursor(buffered=True)
cursor.execute('DROP TABLE IF EXISTS collab')
query = 'CREATE TABLE collab (profile_id varchar(255) primary key, product_1 varchar(255) not null, product_2 varchar(255) not null, product_3 varchar(255) not null, product_4 varchar(255) not null)'
cursor.execute(query)

def tweedekans(vergelijkbareproducten):
    cursor = db.cursor(buffered=True)
    cursor.execute("select profid from sessions where segment = (%s)", (seg_aud[0],))
    terug6 = cursor.fetchmany(100)
    for i in terug6:
        filter = i[0].strip('\r')
        cursor.execute("select prodid from profiles_previously_viewed where profid = (%s)", (filter,))
        terug7 = cursor.fetchall()
        for z in terug7:
            filter2 = z[0].strip('\r')
            vergelijkbareproducten.append(filter2)
            if len(vergelijkbareproducten) >= 4:
                return vergelijkbareproducten


cursor.execute("select profid from sessions WHERE segment NOT IN ('Bouncer') AND segment NOT IN ('')")
resultaat = cursor.fetchmany(10)
for i in resultaat:
    eenid.add(i[0])

for id in eenid:
    zoek = "select segment from sessions WHERE profid = (%s) AND segment NOT IN ('Bouncer') AND segment NOT IN ('')"
    cursor.execute(zoek, (id,))
    terug = cursor.fetchall()
    browser = 0
    judger = 0
    comparer = 0
    leaver = 0
    buyer = 0
    fun_shopper = 0

    for i in terug:
        if i == ('BROWSER',):
            browser += 1
        elif i == ('JUDGER',):
            judger += 1
        elif i == ('COMPARER',):
            comparer += 1
        elif i == ('LEAVER',):
            leaver += 1
        elif i == ('BUYER',):
            buyer += 1
        elif i == ('FUN_SHOPPER',):
            fun_shopper += 1

    segment = ['browser', 'judger', 'comparer', 'leaver', 'buyer', 'fun_shopper']
    hoeveel = [browser, judger, comparer, leaver, buyer, fun_shopper]
    meeste = max(hoeveel)
    index = hoeveel.index(meeste)

    uitvoeren = "select prodid from profiles_previously_viewed where profid = (%s)"
    cursor.execute(uitvoeren, (id,))
    terug2 = cursor.fetchall()

    mannen = 0
    vrouwen = 0
    kinderen = 0
    volwassenen = 0
    null = 0

    if len(terug2) == 0:
        audience = 'N/A'
    else:
        for i in terug2:
            zonder_r= i[0].strip('\r')
            target = "select targetaudience from products where id = (%s)"
            cursor.execute(target, (zonder_r,))
            terug3 = cursor.fetchall()[0][0]
            if terug3 == 'Mannen':
                mannen += 1
            elif terug3 == 'Vrouwen':
                vrouwen += 1
            elif terug3 == 'Kinderen':
                kinderen += 1
            elif terug3 == 'Volwassenen':
                volwassenen += 1
            elif terug3 == 'null':
                null += 1

        totaal_audience = ['mannen', 'vrouwen', 'kinderen', 'volwassenen', 'N/A']
        hoeveel_audience = [mannen, vrouwen, kinderen, volwassenen, null]
        meeste_audience = max(hoeveel_audience)
        index_audience = hoeveel_audience.index(meeste_audience)
        audience = totaal_audience[index_audience]
    dict.update({id: [segment[index], audience]})


for id in eenid:
    """Deze funtie zoek naar alle profid's die hetzelfde segment en geslagt hebben."""
    overeenkomende_ids = []
    seg_aud = dict[id]
    for id2 in dict:
        seg_aud_2 = dict[id2]
        if seg_aud == seg_aud_2:
            overeenkomende_ids.append(id2)
    overeenkomende_ids.remove(id)

    productlijst = [] #weg
    vergelijkbareproducten = []
    if overeenkomende_ids != [] and seg_aud[1] != 'N/A':                            #overeenkomsten dinges weg!!!!!!!!
        code = "select prodid from profiles_previously_viewed where profid = (%s)"
        cursor.execute(code, (id,))
        terug4 = cursor.fetchall()
        for i in terug4:
            terug4 = i[0].strip('\r')
            productlijst.append(terug4)
        for i in overeenkomende_ids:
            tussenstop = []
            cursor.execute("select prodid from profiles_previously_viewed where profid = (%s)",(i,))
            terug5 = cursor.fetchall()
            for i in terug5:
                terug5 = i[0].strip('\r')
                tussenstop.append(terug5)
            for i in tussenstop:
                if i in productlijst:
                    for z in tussenstop:
                        vergelijkbareproducten.append(z)
                    vergelijkbareproducten.remove(i)
    if len(vergelijkbareproducten) < 4:
        tweedekans(vergelijkbareproducten)

    cursor = db.cursor()

    laatse_execute = ("insert into collab (profile_id, product_1, product_2, product_3, product_4) values (%s, %s, %s, %s, %s)")
    cursor.execute(laatse_execute, (id, vergelijkbareproducten[0], vergelijkbareproducten[1], vergelijkbareproducten[2], vergelijkbareproducten[3]))

    db.commit()
