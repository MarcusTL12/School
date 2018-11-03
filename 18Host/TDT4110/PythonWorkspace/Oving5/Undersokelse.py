import ConsoleUtil as cu


def les_ja_nei(spm):
	while True:
		ans = input(spm)
		if ans.lower() == "ja":
			return 1
		elif ans.lower() == "nei":
			return 0
		elif ans.lower() == "hade":
			return -1



def survey():
	print("\nVelkommen til spørreundersøkelsen!\n")

	kjonn = input("Hvilket kjønn er du? [f/m]: ")
	alder = cu.cin_I("Hvor gammel er du?: ")

	if alder < 18 or alder > 27:
		print("Du kan dessverre ikke ta denne undersøkelsen")
		return (False,)

	fag = les_ja_nei("Tar du et eller flere fag? [ja/nei]: ")

	if fag == -1:
		return False
	elif fag == 0:
		return (True, kjonn, alder, 0)

	medlem_ITGK = les_ja_nei("Tar virkelig du ITGK? [ja/nei]: " if alder >= 22 else "Tar du ITGK? [ja/nei]: ")

	if medlem_ITGK == -1:
		return False
	
	timer_lekser = cu.cin_I("Hvor mange timer bruker du daglig (i snitt) på lekser?: ")

	return (True, kjonn, alder, 1, medlem_ITGK, timer_lekser)


def run():
	amt_ans = 0
	amt_f = 0
	amt_m = 0
	acc_age = 0
	amt_fag = 0
	amt_itgk = 0
	amt_h = 0
	while True:
		result = survey()
		if result == False:
			break
		elif result[0]:
			amt_ans += 1
			if result[1].lower() == "f":
				amt_f += 1
			elif result[1].lower() == "m":
				amt_m += 1
			acc_age += result[2]
			amt_fag += result[3]
			if result[3] != 0:
				amt_itgk += result[4]
				amt_h += result[5]
	
	print("Resultat av undersøkelse:")
	print("Antall svar:".ljust(45) + str(amt_ans))
	print("Antall kvinner:".ljust(45) + str(amt_f))
	print("Antall menn:".ljust(45) + str(amt_m))
	print("Gjennomsnittlig alder:".ljust(45) + format(acc_age / amt_ans, '.2f'))
	print("Antall personer som tar fag:".ljust(45) + str(amt_fag))
	print("Antall personer som tar ITGK:".ljust(45) + str(amt_itgk))
	print("Antall timer i snitt brukt på lekser:".ljust(45) + format(amt_h / amt_ans, '.2f'))


'''
h)
Nei, det vil ikke være mulig å hente ut svarene etter at programmet er avsluttet.
alle variable i et program vil være lagret i programmets tildelte minneområde i RAM
(med mindre de tar så stor plass at operativsystemet vil tildele plass på systemharddisken
	for å emulere større minne, men dette er en veldig treg løsning som sjeldent er et problem
	og ville uansett ikke løst problemet med dataen)
og når programmet avsluttes vil dette minne bli satt som fritt minne til andre programmer.
Det er da ingen måte å vite hvor i minne dataene ligger og selv om en hadde hatt tilgang til
pekeren er det ingen forsikring om dataen er blitt overskrevet og om en har lov til å lese fra det stedet i minne.
For å kunne hente ut data etter et program er avsluttet må det skrives til en fil på harddisken.
'''