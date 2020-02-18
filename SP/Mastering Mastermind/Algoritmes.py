import time
import math
def algoritme1(geheime_code, feedback, combinaties):
    '''Dit algortime is gebaseerd op de simple strategie'''

    print('\nDe computer heeft gekozen voor algoritme 1.\n')
    poging = 1

    while len(combinaties) > 1:
        eerstegok = combinaties[0]

        print('In poging '+str(poging)+' gokt de computer dat de code '+str(eerstegok[0])+', '+str(eerstegok[1])+', '+str(eerstegok[2])+', '+str(eerstegok[3])+' is.')

        if eerstegok == geheime_code:
            break
        else:
            terug = feedback(geheime_code, eerstegok)

            opslag = []

            for code in combinaties: #Kijkt of de feedback van de code hetzelfde is als de feedback van elke andere combinatie
                x = feedback(eerstegok, code)
                if x == terug:
                    opslag.append(code)

            combinaties = opslag
            poging += 1
        time.sleep(3)
    return combinaties[0], poging


def algoritme2(geheime_code, feedback, combinaties):
    '''Dit algortime is gebaseerd op de worstcase strategie'''

    print('\nDe computer heeft gekozen voor algoritme 2.\nDe computer is de code aan het raden. Even geduld aub.')
    poging = 1

    while len(combinaties) > 1:
        antwoorden = [(0,0), (0,1), (0,2), (0,3), (0,4), (1,0), (1,1), (1,2), (1,3), (2,0), (2,1), (2,2), (3,0), (4,0)]
        bestworstcase = [1000, 'combo']

        for i in combinaties:
            uitkomst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for y in combinaties:
                x = feedback(y, i)
                for z in range(0,len(uitkomst)):
                    if x == antwoorden[z]:
                        uitkomst[z] += 1

            if max(uitkomst) < bestworstcase[0]:
                bestworstcase = max(uitkomst), i

        opslag = []

        eerstegok = bestworstcase[1]

        print('In poging ' + str(poging) + ' gokt de computer dat de code ' + str(eerstegok[0]) + ', ' + str(eerstegok[1]) + ', ' + str(eerstegok[2]) + ', ' + str(eerstegok[3]) + ' is.')

        if eerstegok == geheime_code:
            return eerstegok, poging

        terug = feedback(geheime_code, eerstegok)

        for code in combinaties:
            x = feedback(eerstegok, code)
            if x == terug:
                opslag.append(code)

        combinaties = opslag
        poging += 1
        time.sleep(3)
    return combinaties[0], poging

def algoritme3(geheime_code, feedback, combinaties):
    '''In dit algoritme pakt het algoritme niet (zoals bij de worstcase strategie) het grootste getal uit de lijst en slaat die op, maar het middelste getal'''

    print('\nDe computer heeft gekozen voor algoritme 3.\nDe computer is de code aan het raden. Even geduld aub.')
    poging = 0

    while len(combinaties) > 1:
        antwoorden = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (3, 0), (4, 0)]
        bestworstcase = [1000, 'combo']
        eindlijst = []

        for i in combinaties:
            uitkomst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            bestcaseaantal = 0
            for y in combinaties:
                x = feedback(y, i)
                for z in range(0, len(uitkomst)):
                    if x == antwoorden[z]:
                        uitkomst[z] += 1
            uitkomst.sort()
            while 0 in uitkomst:
                uitkomst.remove(0)

            if len(uitkomst) % 2 != 0:
                middelste = int((len(uitkomst)-1)/2)
                maxi = uitkomst[middelste]
            else:
                middelste = (len(uitkomst)-1)/2
                if middelste > 0:
                    mid = uitkomst[math.floor(middelste)], uitkomst[math.ceil(middelste)]
                    maxi = max(mid)

            if maxi <= bestworstcase[0] and bestworstcase[0] != 0:
                bestworstcase = maxi, i
                bestcaseaantal+=1
                eindlijst.append(i)

        if bestcaseaantal == len(combinaties)-1:
            for code in eindlijst:
                if code == geheime_code:
                    poging+=1
                    print('In poging ' + str(poging) + ' gokt de computer dat de code ' + str(code[0]) + ', ' + str(code[1]) + ', ' + str(code[2]) + ', ' + str(code[3]) + ' is.')
                    return code, poging

        opslag = []

        eerstegok = bestworstcase[1]
        poging+=1
        print('In poging ' + str(poging) + ' gokt de computer dat de code ' + str(eerstegok[0]) + ', ' + str(eerstegok[1]) + ', ' + str(eerstegok[2]) + ', ' + str(eerstegok[3]) + ' is.')

        terug = feedback(geheime_code, eerstegok)

        for code in combinaties:
            x = feedback(eerstegok, code)
            if x == terug:
                opslag.append(code)

        combinaties = opslag
        time.sleep(3)
    return combinaties[0], poging