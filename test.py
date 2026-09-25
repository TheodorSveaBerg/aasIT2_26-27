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


### oppg 7

from random import randint
1 = [randint(1,9) for _ in range(100)]


