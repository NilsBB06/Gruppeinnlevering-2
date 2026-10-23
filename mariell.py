Valg =[]


print ("Konflikt 1: Silje og Elias \n"
"A: Individuelle samtaler: Løser både sak og personkonflikt +1 \n"
"B: Ta opp i plenum: Løser sak, men ikke personkonflikt +0")
poeng = 0
def hent_valg():
    while True:
        Valg1 = input("Velg A eller B: ") .upper()
        if Valg1 in ["A", "B"]:
            return Valg1
        else:
            print("Ugyldig valg. Vennligst velg A eller B.")
Valg1 = hent_valg()
if Valg1 == "A":
    poeng += 1
elif Valg1 == "B":
    poeng += 0
print ("Konflikt 2: Hamdi og Hallgeir \n"
       "A: Møte med Hamdi og Hallgeir: De kommer til en felles enighet +1 \n" \
       "B: Ignorer og håp at det går over: Skaper frustrasjon +0 \n")
def hent_valg():
    while True:
        Valg1 = input("Velg A eller B: ") .upper()
        if Valg1 in ["A", "B"]:
            return Valg1
        else:
            print("Ugyldig valg. Vennligst velg A eller B.")
Valg1 = hent_valg()
if Valg1 == "A":
    poeng += 1
elif Valg1 == "B":
    poeng += 0
print ("Konflikt 3: Motivasjon \n"
       "A: Sosial teamaktitivitet: Øker motivasjonen +1 \n" \
       "B: Kun saklig fokus på på prosjektets fremdrift: Teamet mister motivasjon +0 \n")
def hent_valg():
    while True:
        Valg1 = input("Velg A eller B: ") .upper()
        if Valg1 in ["A", "B"]:
            return Valg1
        else:
            print("Ugyldig valg. Vennligst velg A eller B.")
Valg1 = hent_valg()
if Valg1 == "A":
    poeng += 1
elif Valg1 == "B":
    poeng += 0

print (" Sluttresultat: " + str(poeng) + " poeng \n")