apoeng = 0
# Poengene starter på 0
poeng = 0

print("Du er Erling, prosjektleder for et prosjekt.")
print("Du må ta noen valg for å håndtere ulike konflikter.")
print()


# KONFLIKT 1
print("KONFLIKT 1: Silje og Elias")
print("Silje og Elias har en konflikt. Konflikten har gått fra en sakskonflikt til en personkonflikt og påvirker de andre i teamet. Erling står ovenfor to valg" \
"")
print()
print("A: Individuelle samtaler")
print("   Løser både saks- og personkonflikt (+1)")
print()
print("B: Ta opp i plenum")
print("   Løser sak, men ikke personkonflikt (+0)")
print()

valg = input("Hva velger du? A eller B: ").upper()

while valg != "A" and valg != "B":
    print("Ugyldig svar! Du må velge A eller B.")
    valg = input("Hva velger du? A eller B: ").upper()

if valg == "A":
    poeng = poeng + 1
elif valg == "B":
    poeng = poeng + 0


# KONFLIKT 2
print()
print("KONFLIKT 2: Hamdi og Hallgeir")
print("Det har oppstått en ny konflikt.")
print()
print("A: Møte med Hamdi og Hallgeir")
print("   Felles enighet (+1)")
print()
print("B: Ignorere og håpe at det går over")
print("   Skaper frustrasjon (+0)")
print()

valg = input("Hva velger du? A eller B: ").upper()

while valg != "A" and valg != "B":
    print("Ugyldig svar! Du må velge A eller B.")
    valg = input("Hva velger du? A eller B: ").upper()

if valg == "A":
    poeng = poeng + 1
elif valg == "B":
    poeng = poeng + 0


# KONFLIKT 3
print()
print("KONFLIKT 3: Motivasjon")
print("Teamet begynner å miste motivasjonen.")
print()
print("A: Sosial teamaktivitet")
print("   Mer motivert team (+1)")
print()
print("B: Kun saklig fokus på prosjektets fremdrift")
print("   Teamet mister motivasjon (+0)")
print()

valg = input("Hva velger du? A eller B: ").upper()

while valg != "A" and valg != "B":
    print("Ugyldig svar! Du må velge A eller B.")
    valg = input("Hva velger du? A eller B: ").upper()

if valg == "A":
    poeng = poeng + 1
elif valg == "B":
    poeng = poeng + 0


# SLUTT
print()
print("==============================")
print("SPILLET ER FERDIG!")
print("Du fikk", poeng, "poeng.")
print("==============================")
print()

if poeng == 3:
    print("NORMING-FASEN")
    print("Du har håndtert alle konfliktene godt!")

elif poeng == 1 or poeng == 2:
    print("DELVIS LØST")
    print("Noen av konfliktene er løst, men ikke alle.")

elif poeng == 0:
    print("PROSJEKTET FORSINKES")
    print("Konfliktene ble ikke håndtert godt nok.")
