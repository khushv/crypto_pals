import base64
from challenge_3 import xor_brute_bytes
from challenge_5 import text_to_bytes
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
	return sorted(result, key=result.get)[:num_results]


def keysize_blocks(keysize, ciphertext):
	return [ciphertext[i:i+keysize] for i in range(0, len(ciphertext), keysize)]


def transpose_block(keysize, ciphertext):
	transposed = []
	for i in range(0, keysize):
		transposed.append(ciphertext[i:len(ciphertext):keysize])
	return transposed


def bruteforce_text(ciphertext):
	# find candidates
	candidate = likely_candidate(crypt_bytes)
	print("Likely candidates: ", candidate)
	blocksize = candidate[0]
	to_xor = transpose_block(blocksize, crypt_bytes)
	print("# of transposed blocks: ", len(to_xor))

	possible_key = ["", "", ""]
	for column in to_xor:
		print("Xor'ing string of length: ", len(column)) 
		column_xor = sorted(xor_brute_bytes(column, 3))
		for num in range(0, len(column_xor)):
			print(column_xor[num][1])
			possible_key[num] += chr(column_xor[num][1])
	print(possible_key)


if __name__ == '__main__':
	a = text_to_bytes('this is a test')
	b = text_to_bytes('wokka wokka!!!')

	# print(mod_ham(a,b))

	crypt_bytes = base64_file_to_bytes('6.txt')
	print(len(crypt_bytes))
	"""	
	candidate = likely_candidate(crypt_bytes)
	blocks = keysize_blocks(6, crypt_bytes)
	to_xor = transpose_block(3, crypt_bytes)
	bruteforce_xor = xor_brute(to_xor[0], 2)
	print(sorted(bruteforce_xor), "\n\n")
	"""
	bruteforce_text(crypt_bytes)









"""
Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.
Now transpose the blocks: make a block that is the first byte of every block, and a block that is the second byte of every block, and so on.
Solve each block as if it was single-character XOR. You already have code to do this.
For each block, the single-byte XOR key that produces the best looking histogram is the repeating-key XOR key byte for that block. Put them together and you have the key.
"""

