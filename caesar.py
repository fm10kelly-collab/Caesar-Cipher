def shift_letter(letter, key):
	if letter.isupper():
		start = ord("A")
	elif letter.islower():
		start = ord("a")
	else:
		return letter
	position = ord(letter) - start
	new_position = (position + key) % 26
	return chr(start + new_position)

def encrypt(message, key):
	result = ""
	for letter in message:
		result+= shift_letter(letter, key)
	return result

def decrypt(message, key):
	return encrypt(message, -key)

def brute_force(message):
	for key in range(1, 26):
		print("Key", key, ":", decrypt(message, key))

while True:
	print("1) Encrypt 2) Decrypt 3) Crack 4) Quit")
	choice = input("Choose: ")
	if choice == "1":
		message = input("Mesage: ")
		key = int(input("Key: "))
		print("Encrypted:", encrypt(message, key))
	elif choice == "2":
		message = input("Message: ")
		key - int(input("Key: "))
		print("Decrypted:", decrypt(message, key))
	elif choice == "3":
		brute_force(input("Message: "))
	elif choice == "4":
		break
