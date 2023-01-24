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

print("Mocninátor")
print("==========")
a = int(input("Zadejte základ mocniny: "))
n = int(input("Zadejte exponent: "))
result = a
for i in range(n - 1):
    result = result * a

print("Výsledek: %d" % (result))
print("Děkuji za použití mocninátoru")