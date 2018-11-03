

import binascii
import random


def toHex(word):
	return int(str(binascii.hexlify(word), 'ascii'), 16)
 

def toString(word):
	return str(binascii.unhexlify(hex(word)[2:]), 'ascii')


def encrypt(message, key):
	return toHex(bytes(message, encoding = 'ascii')) ^ toHex(bytes(key, encoding = 'ascii'))


def decrypt(code, key):
	return toString(code ^ toHex(bytes(key, encoding = 'ascii')))


def a():
	message = "hei"
	key = "abc"
	code = encrypt(message, key)
	print(code)


def b():
	code = 10236822292578194418270355906139225094292945080430361
	key = "dvovLc>r?JsF8sCqMAju_w"
	print(decrypt(code, key))


def c():
	message = input("Hva er meldingen? ")
	key = ""
	for i in range(len(message)):
		key += chr(random.randint(48, 122))

	code = encrypt(message, key)

	print(key)

	print(code)

	print(decrypt(code, key))
