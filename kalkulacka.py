"""
    _____ _______         _                      _
   |_   _|__   __|       | |                    | |
     | |    | |_ __   ___| |___      _____  _ __| | __  ___ ____
     | |    | | '_ \ / _ \ __\ \ /\ / / _ \| '__| |/ / / __|_  /
    _| |_   | | | | |  __/ |_ \ V  V / (_) | |  |   < | (__ / /
   |_____|  |_|_| |_|\___|\__| \_/\_/ \___/|_|  |_|\_(_)___/___|
                     ___
                    |  _|___ ___ ___
                    |  _|  _| -_| -_|  LICENCE
                    |_| |_| |___|___|

     PROGRAMOVÁNÍ  <>  DESIGN  <>  PRÁCE/PODNIKÁNÍ  <>  HW A SW

   Tento zdrojový kód pochází z IT sociální sítě WWW.ITNETWORK.CZ

   Můžete ho upravovat a používat jak chcete, musíte však zmínit
   odkaz na http://www.itnetwork.cz
"""

print("Vítejte v kalkulačce")
pokracovat = "ano"
while (pokracovat == "ano"):
    a = float(input("Zadejte první číslo:"))
    b = float(input("Zadejte druhé číslo:"))
    print("Vyberte jednu z požadovaných operací:")
    print("1 - sčítání")
    print("2 - odčítání")
    print("3 - násobení")
    print("4 - dělení")
    operace = int(input(""))

    if (operace == 1):
        vysledek = a + b
    elif (operace == 2):
        vysledek = a - b
    elif (operace == 3):
        vysledek = a * b
    elif (operace == 4):
        vysledek = a / b
    if operace > 0 and operace < 5:
        print("výsledek: %f" % (vysledek))
    else:
        print("Chybná volba")
    pokracovat = input("Přejete si zadat další příklad? [ano/ne]")
print("Děkuji za použití kalkulačky!")
