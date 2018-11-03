

def find_substrings(sub, sup):
	indices = []
	for i in range(len(sup) - len(sub) + 1):
		found = True
		for j in range(len(sub)):
			if sub.lower()[j] != sup.lower()[i + j]:
				found = False
				break
		if found:
			indices.append(i)
	return indices


def replace(sup, sub, wht):
	indices = find_substrings(sub, sup)
	ret = ""
	lastindex = 0
	for i in indices:
		ret += sup[lastindex : i]
		ret += wht
		lastindex = i + len(wht) - len(sub)
	
	return ret


def a():
	print(find_substrings("iS", "Is this the real life? Is this just fantasy?"))
	print(find_substrings("oo", "Never let you go let me go. Never let me go ooo"))


def b():
	print(replace("Is this the real life? Is this just fantasy?", "iS", "cool"))
	print(replace("Never let you goooo let me goo. Never let me goo oooo", "oo", "cool"))


