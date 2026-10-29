# master.py
# IS-118 Gruppeoppgave 2 (gruppe 4) - Del 2: Interaktiv historie
#
# Du er Erling, prosjektleder. Du tar tre valg (A eller B) som avgjør
# hvordan det går med teamet. Koden følger beslutningstreet fra del 1:
#   A gir +1 poeng, B gir +0 poeng
#   3 poeng = norming-fasen, 1-2 poeng = delvis løst, 0 poeng = forsinket
#
# Kjør i terminalen med:  python master.py
 

def hent_valg():
    # Spør helt til brukeren skriver A eller B (store eller små bokstaver)
    while True:
        svar = input("Hva velger du? (A/B): ").strip().upper()
        if svar == "A" or svar == "B":
            return svar
        print("Ugyldig svar. Du må skrive A eller B.")


# Poengene starter på 0
poeng = 0

# ---------- INNLEDNING ----------
print()
print("--- Innledning ---")
print("Du er Erling, prosjektleder for kommunens nye medborgerportal.")
print("Teamet er i storming-fasen, og prototypen skal være klar om tre uker.")
print("Dine valg avgjør om teamet holder sammen og kommer videre.")

# ---------- KONFLIKT 1: Silje og Elias ----------
print()
print("--- Konflikt 1: Silje og Elias ---")
print("Silje og Elias er uenige om teknologi og design. Uenigheten har")
print("blitt en personkonflikt, og resten av teamet blir revet med.")
print()
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
print("--- Konflikt 2: Hamdi og Hallgeir ---")
print("Du merker en kjølig stemning i gangene. Ingen krangler, men noe")
print("ulmer mellom Hamdi og Hallgeir. Hamdi vil ha en kontrollert løsning")
print("på kommunens plattform, mens Hallgeir vil ha et åpent system.")
print()
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
print("--- Konflikt 3: Motivasjon ---")
print("Motivasjonen i teamet er lav etter konfliktene. Du husker at")
print("bestefaren din sa at trivsel er nøkkelen på en arbeidsplass.")
print("Det står ikke trivsel på noen av nøklene dine, så du må skape den")
print("selv. Men prototypen nærmer seg, og sosial tid tar tid fra arbeidet.")
print()
print("A: Sosial teamaktivitet (escape room i arbeidstiden)")
print("B: Kun saklig fokus på prosjektets fremdrift")

valg3 = hent_valg()  # Lagrer valget

# Konsekvens av valget (A gir +1 poeng)
if valg3 == "A":
    poeng = poeng + 1
    print("Teamet løser oppgavene sammen og blir mer motivert.")
else:
    print("Teamet føler seg presset og mister motivasjonen.")

# ---------- RESULTAT ----------
print()
print("--- Resultat ---")
print("Du fikk", poeng, "av 3 poeng.")
print()

# Tre mulige utfall, avhengig av poengsummen
if poeng == 3:
    print("SLUTT 1: Norming-fasen - Bra jobba!")
    print("Konfliktene er løst og stormen er over. Teamet går videre til")
    print("norming-fasen, der de kan jobbe trygt og effektivt.")
elif poeng == 1 or poeng == 2:
    print("SLUTT 2: Delvis løst - Ok jobba!")
    print("Teamet nærmer seg norming-fasen, men relasjonene er fortsatt")
    print("sårbare, og det kan dukke opp flere problemer på veien.")
else:
    print("SLUTT 3: Prosjektet forsinkes - Dårlig jobba!")
    print("Teamet sitter fast i storming-fasen. Konfliktene ble ikke")
    print("håndtert godt nok, og prototypen blir forsinket.")
print()