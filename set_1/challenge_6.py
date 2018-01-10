import base64
from challenge_3 import xor_brute_bytes
from challenge_5 import text_to_bytes, repeating_key_xor, xor_bytes
from hex_to_base64 import string_to_bytearray


def base64_file_to_bytes(filename):
	with open(filename) as f:
		data = f.read().replace('\n', '')
	return base64.b64decode(data)


def mod_ham(x, y):
	return sum(bin(i ^ j).count('1') for (i, j) in zip(x, y))


def likely_candidate(text, min=2, max=50, num_results=3):
	result = {}
	for i in range(min, max):
        # calculate hamming distance and divide by keysize
		result[i] = (mod_ham(text[0:i], text[i:2 * i])/i)
    # returns keysize with smallest normalised hamming distance
	print(result)
	return sorted(result, key=result.get)[:num_results]


def likely_candidate_mod(text, min=2, max=50, num_results=5):
	result = {}
	result2 = {}
	for i in range(min, max):
		# calculate hamming distance and divide by keysize
		first_block = mod_ham(text[0:i], text[i:2*i])/i
		second_block = mod_ham(text[2*i:3*i], text[3*i:4*i])/i
		third_block = mod_ham(text[4*i:5*i], text[5*i:6*i])/i
		result2[i] = (first_block + second_block + third_block)/3     
		result[i] = (mod_ham(text[0:i], text[i:2 * i])/i)
	# returns keysize with smallest normalised hamming distance
	#print(result)
	print(result2)
	return sorted(result2, key=result.get)[:num_results]
	
	
	
def keysize_blocks(keysize, ciphertext):
	return [ciphertext[i:i+keysize] for i in range(0, len(ciphertext), keysize)]


def transpose_block(keysize, ciphertext):
	transposed = []
	for i in range(0, keysize):
		transposed.append(ciphertext[i:len(ciphertext):keysize])
	return transposed


def bruteforce_column(column_cipher, results):
	#print("*********")
	#print("Column ciphertext: ", column_cipher)
	x = xor_brute_bytes(column_cipher, results)
	#print(x)
	return [chr(element[1]) for element in x]


def bruteforce_per_keysize(keysize, ciphertext, results=5):
	#print(keysize)
	transposed_blocks = transpose_block(keysize, ciphertext)
	#print(transposed_blocks)
	possible_key =  [""] * results
	#print("length of array: ", len(possible_key))
	for column in transposed_blocks:
		possible_chars = bruteforce_column(column, results)
		#print("Possible chars: ", possible_chars)
		for poss_char in range(results):
			possible_key[poss_char] += possible_chars[poss_char]
	return  possible_key



def bruteforce(keysizes, ciphertext, results):
	#keysizes = [29]
	possible_keys = []
	for size in keysizes:
		possible_keys.extend(bruteforce_per_keysize(size, ciphertext, results))
	return possible_keys


def decrypt_xor(key, ciphertext):
	#print("Ciphertext: ", ciphertext)
	decrypted = bytearray()
	key_len = len(key)
	pointer = 0
	for character in ciphertext:
		decrypt_key = ord((key[pointer%key_len]))
		if character == decrypt_key:
			x = character
		else:
			x = character ^ decrypt_key
		#print(chr(character), "-", character, " xors with ", decrypt_key, chr(decrypt_key), "equals ", x, " in chr() ", chr(x))
		decrypted.append(x)
		pointer += 1
	return decrypted
 
if __name__ == '__main__':
	a = text_to_bytes('this is a test')
	b = text_to_bytes('wokka wokka!!!')

	# print(mod_ham(a,b))

	crypt_bytes = base64_file_to_bytes('6.txt')
	x = likely_candidate_mod(crypt_bytes, 3, 30, 30)
	print(x)
	
	#problem with bruteforce method
	answers = bruteforce(x, crypt_bytes, 15)
	#print("Possible keys:" , answers)
	
	#print(decrypt_xor(answers[0], crypt_bytes))
	#for answer in answers:
	#	print(decrypt_xor(answer, crypt_bytes))
	





