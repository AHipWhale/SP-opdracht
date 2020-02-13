import random
print('Welkom bij het spel Mastermind')

def gespeeld():
    J=['j', 'n']
    spel = input('Heb je het spel al eerder gespeeld? J/N: ').lower()
    opnieuw(J, spel, 'Heb je het spel al eerder gespeel? J/N: ')
    if spel == 'n':
        spelregels=input('Wil je de spelregels weten? J/N: ').lower()
        opnieuw(J, spelregels, 'Wil je de spelregels weten? J/N: ')
        if spelregels == 'j':
            print('Dit zijn de spelregels van Mastermind:')

def gamemode():
    mode=['m','r']
    keuze= input('Wil je een code maken of een code raden? M/R: ').lower()
    opnieuw(mode, keuze, 'Wil je een code maken of een code raden? M/R: ')
    if keuze == 'm':
        print('Je hebt gekozen om een code te maken. De computer gaat de code proberen te raden.')
        return 'maken'
    else:
        print('Je hebt gekozen om de code (die de computer heeft gegenereerd) te raden.')
        return 'raden'

def gamemode_keuze():
    if gamemode() == 'maken':
        code_maken(kleuren)
    else:
        code_raden()

kleuren = ['zwart', 'wit', 'rood', 'geel', 'blauw', 'groen']

def code_maken(kleuren):
    print('\nKies een code van 4 kleuren. De kleuren waar je uit kunt kiezen is: zwart, wit, rood, geel, blauw en groen.')
    kleur1 = input('Voer kleur 1 in: ').lower()
    if kleur1 not in kleuren:
        kleur1 = opnieuw(kleuren, kleur1, 'Voer kleur 1 in: ')
    kleur2 = input('Voer kleur 2 in: ').lower()
    if kleur2 not in kleuren:
        kleur2 = opnieuw(kleuren, kleur2, 'Voer kleur 2 in: ')
    kleur3 = input('Voer kleur 3 in: ').lower()
    if kleur3 not in kleuren:
        kleur3 = opnieuw(kleuren, kleur3, 'Voer kleur 3 in: ')
    kleur4 = input('Voer kleur 4 in: ').lower()
    if kleur4 not in kleuren:
        kleur4 = opnieuw(kleuren, kleur4, 'Voer kleur 4 in: ')

def code_raden():
    input('Klik op enter om het spel te beginnen.')
    kleuren = ['zwart', 'wit', 'rood', 'geel', 'blauw', 'groen']
    kleur1 = kleuren[random.randint(0,5)]
    kleur2 = kleuren[random.randint(0,5)]
    kleur3 = kleuren[random.randint(0,5)]
    kleur4 = kleuren[random.randint(0,5)]
    gekozenkleuren = [kleur1, kleur2, kleur3, kleur4]
    print(gekozenkleuren)

    print('\nDe computer heeft een code gegenereerd.\nDoe je eerste poging. De kleuren waar je uit kunt kiezen is: zwart, wit, rood, geel, blauw en groen.')

    poging = 1

    keuze = raden_keuze(kleuren)
    while True:
        if keuze == gekozenkleuren:
            print('Gefeliciteerd! Je hebt de code in '+str(poging)+' keer geraden')
            break
        elif poging >= 10:
            print('Helaas. Je hebt de code niet in 10 keer kunnen kraken.')
            break
        else:
            terug = feedback(gekozenkleuren, keuze)
            print('Je hebt '+str(terug[0])+' kleuren op de goede plek en '+str(terug[1])+' kleuren zitten in de code maar niet op de goede plek.')
            print('\nJe hebt ' + str(poging) + ' poging(en) gedaan. Je hebt nog ' + str(10 - poging) + ' poging(en) om de code goed te raden.')
            poging += 1
            keuze = raden_keuze(kleuren)

def feedback(gekozenkleuren, keuze):
    kleuren = gekozenkleuren
    index=0
    goed = 0
    goedeplek = 0
    for i in kleuren:
        if i == keuze[index]:
            goed+=1
            kleuren[index]='niks'
            index += 1
        else:
            index+=1
    index=0
    for i in range(len(kleuren)):
        if keuze[index] in kleuren:
            goedeplek+=1
            kleuren[index]='nada'
            index += 1
        else:
            index+=1
    return goed, goedeplek

def raden_keuze(lijst,):
    keuze1 = input('Voer kleur 1 in: ').lower()
    if keuze1 not in lijst:
        keuze1 = opnieuw(lijst, keuze1, 'Voer kleur 1 in: ')
    keuze2 = input('Voer kleur 2 in: ').lower()
    if keuze2 not in lijst:
        keuze2 = opnieuw(lijst, keuze2, 'Voer kleur 2 in: ')
    keuze3 = input('Voer kleur 3 in: ').lower()
    if keuze3 not in lijst:
        keuze3 = opnieuw(lijst, keuze3, 'Voer kleur 3 in: ')
    keuze4 = input('Voer kleur 4 in: ').lower()
    if keuze4 not in lijst:
        keuze4 = opnieuw(lijst, keuze4, 'Voer kleur 4 in: ')
    return [keuze1, keuze2, keuze3, keuze4]

def opnieuw(lijst, test, Input):
    while test not in lijst:
        print('Dit is geen geldig antwoord. Probeer nog eens')
        test=input(Input).lower()
    return test

def go():
    gespeeld()
    gamemode_keuze()
code_raden()

combo=[]

for i in kleuren:
    for x in kleuren:
        for y in kleuren:
            for z in kleuren:
                combo.append([i,x,y,z])