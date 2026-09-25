### oppg 5

#a)
"""
spør brukeren om å inputte navn
spør brukeren om å inputte alder
definerer resultat som en kombinasjon av navn, alder of @gmail.com
printer ut resultat
"""

navn = input("ditt navn")
alder = input("Din alder")
resultat = f"{navn}.{alder}.@gmail.com"
print(resultat)


 ### oppg 6

 #En metode er å bruke hashtag for å kunne skrive fritt uten at det skal gjøre noe med koden din. Du kan også bruke flere hashtags
 #til å sortere overskrifter. Du skriver bare inn normalt her hvor du forklarer hva du vil gjøre med koden din.

"""
 en annen metode er tripel apostrof for å danne en slags boble
 hvor all teksten blir samlet  uten at du må lage et nytt tegn for hver inje
 som man må med hashtag. Du bruker denne vanligvis til å skrive de forsjelige
 kode linjene dine om til tekst linjer som da forklarer den linjen de representerer.
 """

#Ikke noe under her ble jeg ferdig med men hvis halv poeng eller noe sånt finnes kan det være relevant
"""
### oppg 7
#Legg sammen alle tallene med for løkke og finn ut når de blir hundre med while

from random import randint
1 = [randint(1,9) for _ in range(100)] #Den blir sinna på at det ikke står 1 == som forvirrer meg litt
prev = randint
for i in range(100):

    randint == prev + randint
print(randint)


### oppg 8
#Hva er feil, forklar forsjellen på hard- og mykkode , rett det og skriv det om til mykkode.

sirkel = {"s1":4,
          "s2":7
          "s3:5"
          ""}
a1 = 3.14 * sirkel[s1]**2 #Kan heller bare legge til pi med bruk av import
a2 = 3.14 * sirkel[s2]**2 #Verken s1, s2, eller s3 er definert
a3 = 3.14 * sirkel[s3]**2

if a1 > a2 and a1 > a3:
    print("{a1} er størst")
else a2 > a3:              #Ser at a2 og a3 ikk er definert her men er det over. Har ingen anelse hvorfor :(
    print("{a2} er størst"). #Ganske sikker på at man ikke kan bruke else to ganger på rad som det.
else a3 > a2:
    print("{a3} er størst")


from math import pi
def sirkel():
    sirkel = 3.14 * **2
    return sirkel()
"""
#programmet mitt for en eller annen grunn driver bare å skriker om at 1 = [randint....] brude ha ==
#Selv om jeg har lagd det til dokumentasjonsstreng, jeg tenker også at det ikke er noe særlig tid igjen
#Så null vits å fikse.

#På minnelse til megselv GJØR ALLE OPPGAVENE

### oppg 9 
#Utvid programmet fra forsje oppg
#Beskriv 3 nye funksjoner som du ønsker å legge til programmet
#Utvid koden sånn at den inkluderer disse 3 nye funksjonene