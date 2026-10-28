poeng = 0
print()
print("---Innledning---\n")
print("Erling er prosjektleder. Teamet han leder har konflikter." \
    "\nErling må ta gode valg for å sørge for at teamet ikke går i oppløsning," \
    "\nat de får levert ting på tiden, og at prosjektet blir godt gjennomført." \
    "\nDu må hjelpe Erling med å ta gode valg\n")
print("---Konflikt 1---\n")
print("Silje og Elias er uenige i en sak. Det har utviklet seg" \
      "til en personkonflikt. De samarbeider ikke godt lengre," \
        "og resten av teamet blir revet med i konflikten.")
print(".")
konflikt_1 = input("Hva skal Erling gjøre?" \
                   "\n1: Ta konflikten opp i plenum." \
                    "\n2: Ta individuelle samtaler med Silje og Elias." \
                    "\nSkriv tall 1 eller 2...")
while konflikt_1 not in ["1" , "2"]:
    print("Prøv igjen din nisse")
    konflikt_1 = input("Hva skal Erling gjøre?")
if konflikt_1 == "1" :
    poeng += 2
elif konflikt_1 == "2" :
    poeng += 3
print()
print("---Konflikt 2---\n")
print("Erling merker en sur stemning når han går i gangene. Han hører ingen krangling," \
    "\nser ingen åpenbare konflikter, men føler en kjølig atmosfære. Noen timer inn i" \
    "\narbeidsdagen merker han at noe ulmer mellom Hallgeir og Hamdi. De har uenigheter." \
    "\nDet er ikke uvanlig med litt uenigheter, men Erling blir engstelig.")
print(".")
konflikt_2 = input("Hva skal Erling gjøre?" \
                    "\n1: Snakke med Hallgeir og Hamdi så de finner enighet" \
                    "\n2: Ignorere problemet, teamet må ha rom til sparring" \
                    "\nSkriv tall 1 eller 2...")
while konflikt_2 not in ["1" , "2"]:
    print("Prøv igjen da vennen...")
    konflikt_2 = input("Hva skal Erling gjøre?")
if konflikt_2 == "1" :
    poeng += 3
elif konflikt_2 == "2" :
    poeng += 0
print()
print("---Konflikt 3---\n")
print("Erling merker at motivasjonen på teamet er lavt etter konfliktene. Erling husker tilbake" \
    "\npå sin bestefar som sa at trivsel er nøkkelen på arbeidsplassen. Han ser ned på nøkkelknipet sitt..." \
    "\nDet står ikke trivsel på noen av de tre nøkklene han har, så han må skape trivselen selv i så fall." \
    "\nGruppen skal ha klar en prototype om kort tid, og en sosial kveld vil ta mye tid fra prosjektet")
print(".")
konflikt_3 = input("Hva skal Erling gjøre?" \
                   "\n1: Inviter hele teamet på Escape room for en kveld med problemløsing og relasjonsbygging" \
                    "\n2: Sett opp et møte om tidsfrister, felles mål og videre fremdrift. Bestill lunsj til møtet" \
                        "\nSkriv tall 1 eller 2...")
while konflikt_3 not in ["1" , "2"]:
    print("Kan du ikke tallene høyere enn 0?")
    konflikt_3 = input("Hva skal Erling gjøre?")
if konflikt_3 == "1" :
    poeng += 1
elif konflikt_3 == "2" :
    poeng += 3
print()
print("---Resultat---")
print("Erling prøvde sitt beste...")
if poeng <= 3 :
    print("Teamet sitter fast i storming-fasen. Det er storm i gangene, på kontorene, alle krangler," \
          "\nHallgeir gråter, Silje dro hjem og Erling gruer seg til en vanskelig telefonsamtale.")
elif poeng >= 7 :
    print("Konfliktene er løst, stormen er over, fuglene synger og sola skinner." \
          "\nTeamet kommer seg videre til norming fasen hvor de kan jobbe trygt, godt og effektivt.")
else:
    print("Teamet har startet relasjonsbygging og løsing av konflikter. De nærmer seg norming-fasen," \
          "\nmen Erling ser ikke bort ifra at det kan oppstå neon flere problemer før de kommer seg dit.")
print()
