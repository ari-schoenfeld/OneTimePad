# #!
import sys
import numpy as np

def convert(plain_text):
	#converts plain text to ASCII and then separates
	#into single digits per array entry, padding with
	#leading zeros if necessary
	counter = 0
	num_array = np.ones(len(plain_text))
	for i in plain_text:
		num_array[counter] = ord(i)
		counter += 1

	num_array = num_array.astype(int)

	sep_array = np.ones(3*len(num_array))
	counter = 0
	#need to implement less hardcoded version
	for i in num_array:
		if numDigits(i) == 3:
			sep_array[counter]   = i/100%10
			sep_array[counter+1] = i/10%10
			sep_array[counter+2] = i%10
		elif numDigits(i) == 2:
			sep_array[counter]   = 0
			sep_array[counter+1] = i/10%10
			sep_array[counter+2] = i%10
		else: #one digit
			sep_array[counter]   = 0
			sep_array[counter+1] = 0
			sep_array[counter+2] = i%10
		counter += 3

	sep_array = sep_array.astype(int)
	return(sep_array)

def encrypt(converted_array, pad):
	length = len(converted_array)
	final_array = []
	for i in range (0, length):
		final_array.append((converted_array[i] + pad[i])%10)

	return final_array

def decrypt(encrypted_array, pad):
	length = len(encrypted_array)
	decrypted = []
	for i in range(0, length, 3):
		value = ((encrypted_array[i] - pad[i] + 10)%10) * 100
		value += ((encrypted_array[i+1] - pad[i+1] + 10)%10) * 10
		value += ((encrypted_array[i+2] - pad[i+2] + 10)%10)
		decrypted.append(value)

	return decrypted

def numDigits(x):
	#returns the number of digits in the base 10 representation of x
	if(x == 0):
		return 1
	if(x < 0):
		x *= -1
	counter = 0
	while x != 0:
		x //= 10
		counter += 1


	return counter

def main():
	if(len(sys.argv) != 4):
		sys.exit("Error: incorrect number of arguments")

	#get message
	try:
		message = open(sys.argv[2])
	except IOError:
		sys.exit("Error: cannot open message")
	except:
		sys.exit("Error")

	#get pad
	try:
		pad = open(sys.argv[3])
	except IOError:
		sys.exit("Error: cannot open pad")
	except:
		sys.exit("Error")

	#read information from files and close files
	try:
		plain_text = message.read()
		pad_list = pad.read()
	except:
		sys.exit("Error: cannot read from files")

	message.close()
	pad.close()

	#gather numbers from pad and store in array with
	#only single digit numbers in each entry
	pad_array = []
	for i in pad_list:
		if (ord(i) > 47) and (ord(i) < 58):
			pad_array.append(int(i))

	if(sys.argv[1] == "encrypt"):

		num_array = convert(plain_text)
		#check if pad is long enough for message
		if len(pad_array) < len(num_array):
			sys.exit("Error: pad is shorter than numeric version of message")

		final = encrypt(num_array, pad_array)

		#create encrypted message file
		file_name = "encrypted_" + sys.argv[2]
		final_message = ""
		for i in final:
			final_message += str(i)
		final_message += "\n"

		outfile = open(file_name, "w+")
		outfile.write(final_message)
		outfile.close()

	elif(sys.argv[1] == "decrypt"):
		#build array of encrypted message
		#one digit per array entry
		en_message = []
		for i in plain_text:
			#only take numbers
			if (ord(i) > 47) and (ord(i) < 58):
				en_message.append(int(i))

		if len(pad_array) < len(en_message):
			sys.exit("Error: pad is shorter than numeric version of message")
		decrypted = decrypt(en_message, pad_array)

		#create decrypted message file
		file_name = "decrypted_" + sys.argv[2]
		final_message = ""
		for i in decrypted:
			final_message += chr(i)

		outfile = open(file_name, "w+")
		outfile.write(final_message)
		outfile.close()

	else:
		print("Error: incorrect command, must be \"encrypt\" or \"decrypt\"")


if __name__ == "__main__":
	main()

