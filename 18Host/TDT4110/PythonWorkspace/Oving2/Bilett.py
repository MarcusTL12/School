import ConsoleUtil as cu

def c():
	fullpris = 440
	minipris = 199

	days = cu.cin_I("Dager til du skal reise? ")
	if days >= 14:
		print("Minipris" + str(minipris) + ",- kan ikke refunderes/endres")
		ans = input("Ønskes dette (J/N)?")
		if ans.lower() == "j":
			print("Takk for pengene, god reise!")
			return
	
	age = cu.cin_I("Skriv inn din alder: ")
	if age < 16:
		print("Prisen på biletten blir: " + str(fullpris * 0.5) + ",-")
		return
	elif age >= 60:
		print("Prisen på biletten blir: " + str(fullpris * 0.75) + ",-")
		return
	else:
		ans = input("Er du student/militær i uniform (J/N)?")
		if ans.lower() == "j":
			print("Prisen på biletten blir: " + str(fullpris * 0.75) + ",-")
			return
	
	print("Prisen på biletten blir: " + str(fullpris) + ",-")
