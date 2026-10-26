# Du er Erling, prosjektleder. Du tar tre valg (A eller B) som avgjør
# hvordan det går med teamet. Koden følger beslutningstreet fra del 1:
#   A gir +1 poeng, B gir +0 poeng
#   3 poeng = norming-fasen, 1-2 poeng = delvis løst, 0 poeng = forsinket


def hent_valg():
    # Spør helt til brukeren skriver A eller B (store eller små bokstaver)
    while True:
        svar = input("Hva velger du? (A/B): ").strip().upper()
        if svar == "A" or svar == "B":
            return svar
        print("Ugyldig svar. Du må skrive A eller B.")


# Poengene starter på 0
poeng = 0

# ---------- INTRODUKSJON ----------
print("Du er Erling, prosjektleder for kommunens nye medborgerportal.")
print("Teamet er i storming-fasen, og prototypen skal være klar om tre uker.")

# ---------- KONFLIKT 1: Silje og Elias ----------
print()
print("KONFLIKT 1: Silje og Elias")
print("Uenigheten om teknologi og design har blitt en personkonflikt.")
print("A: Individuelle samtaler")
print("B: Ta opp i plenum")

valg1 = hent_valg()  # Lagrer valget

# Konsekvens av valget (A gir +1 poeng)
if valg1 == "A":
    poeng = poeng + 1
    print("Du tar dem hver for seg. Både saks- og personkonflikt løses.")
else:
    print("Saken løses, men ikke personkonflikten.")

# ---------- KONFLIKT 2: Hamdi og Hallgeir ----------
print()
print("KONFLIKT 2: Hamdi og Hallgeir")
print("Hamdi vil ha en kontrollert løsning på kommunens plattform,")
print("mens Hallgeir vil ha et åpent system for spontane innspill.")
print("A: Møte med Hamdi og Hallgeir")
print("B: Ignorer og håp at det går over")

valg2 = hent_valg()  # Lagrer valget

# Konsekvens av valget (A gir +1 poeng)
if valg2 == "A":
    poeng = poeng + 1
    print("På møtet blir de enige om en løsning. Felles enighet!")
else:
    print("Uenigheten forsvinner ikke, og det skaper frustrasjon.")

# ---------- KONFLIKT 3: Motivasjon ----------
print()
print("KONFLIKT 3: Motivasjon")
print("Teamet er sliten, og prototypen nærmer seg.")
print("Hvordan holder du motivasjonen oppe?")
print("A: Sosial teamaktivitet (escape room i arbeidstiden)")
print("B: Kun saklig fokus på prosjektets fremdrift")

valg3 = hent_valg()  # Lagrer valget

# Konsekvens av valget (A gir +1 poeng)
if valg3 == "A":
    poeng = poeng + 1
    print("Teamet løser oppgavene sammen og blir mer motivert.")
else:
    print("Teamet føler seg presset og mister motivasjonen.")

# ---------- SLUTT ----------
print()
print("SPILLET ER FERDIG!")
print("Du fikk", poeng, "av 3 poeng.")
print()

# Tre mulige utfall, avhengig av poengsummen
if poeng == 3:
    print("SLUTT 1: Norming-fasen - Bra jobba!")
    print("Tilliten er gjenopprettet, og teamet går videre til norming-fasen.")
elif poeng == 1 or poeng == 2:
    print("SLUTT 2: Delvis løst - Ok jobba!")
    print("Noen konflikter er løst, men relasjonene er fortsatt sårbare.")
else:
    print("SLUTT 3: Prosjektet forsinkes - Dårlig jobba!")
    print("Konfliktene ble ikke håndtert godt nok.")
    print("Teamet mister samholdet, og prototypen blir forsinket.")