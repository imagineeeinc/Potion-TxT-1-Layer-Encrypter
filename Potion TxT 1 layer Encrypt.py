'''This can be used for hash table used encryption and remove all the letters for needed ones
	    
		num = 1
		let = 0
	    for x in range(len(endata)):
		let = let+num
		letter = endata[let]

        if letter == "H":
			encrydata = encrydata + "s"
		elif letter == "e":
			encrydata = encrydata + "V"
		elif letter == "l":
			encrydata = encrydata + "O"
		elif letter == "o":
			encrydata = encrydata + "L"
		else:
			encrydata = encrydata + letter'''

from time import sleep

def startpro():
	global checkforen
	global intext

	print ("If you want to 'Encrypt'")
	print ("Type 'en'")
	print (" ")
	print ("If you want 'De-encrypt'")
	print ("Then Type 'de'")
	print (" ")
	print ("To Exit Press 'Ctrl+C' to close the program")
	print (">")
	checkforen = input()
	checkfor()

def checkfor():
	if checkforen == "en":
		starten()
	elif checkforen == "de":
		startde()
	else:
		print ("not right command")
		startpro()

def starten():
	global endata

	print("Please Enter The Text")
	print (">")
	intext = input()
	print ("Encrypting...")
	endata = intext
	encode()

def encode():
	global output
	global encrydata
	num = 1
	let = len(endata)
	encrydata = ""

	for x in range(len(endata)):
		let = let-num
		letter = endata[let:let+1]
		encrydata = encrydata + letter
	output = encrydata
	output = output+"%ΩΘϠএনক্রিপ্টϠΘΩ%"
	finishen()


def startde():
	global dedata
	print("Please Enter The Encrypted TxT")
	print (">")
	intext = input()
	dedata = intext
	if "%ΩΘϠএনক্রিপ্টϠΘΩ%" in dedata:
	    print ("Decrypting...")
	    dedata = dedata.replace('%ΩΘϠএনক্রিপ্টϠΘΩ%','')
	    decode()
	else:
		print ("This Encrypted text is not encrypted in Potion TxT Encrypter")
		startpro()

def decode():
	global output
	global decrydata
	num = 1
	let = len(dedata)
	encrydata = ""

	for x in range(len(dedata)):
		let = let-num
		letter = dedata[let:let+1]
		encrydata = encrydata + letter
	output = encrydata
	finishde()


def finishen():
	print ("Here is your encrypted txt:")
	print (output)
	sleep(8)
	startpro()

def finishde():
	print ("Here is your decrypted txt:")
	print (output)
	sleep(8)
	startpro()

print ("Welcome To Potion TxT 1 Layer Encrypt")
print (" ")
startpro()

