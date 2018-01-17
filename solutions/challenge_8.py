import base64
from challenge_6 import mod_ham
from binascii import unhexlify
from collections import Counter

def hex_file_to_bytes(filename):
	with open(filename) as f:
		data = [unhexlify(line.strip("\n")) for line in f]
	return data


def count_unique_blocks(cipher_bytes, block_size=16):
	chopped = [cipher_bytes[i*block_size:(i+1)*block_size] for i in range(len(cipher_bytes)//block_size)]
	return len(set(chopped))


def detect_encrypted(cipher_bytes, block_size=16):
	result = {}
	for byte_string in cipher_bytes:
		result[byte_string] = count_unique_blocks(byte_string)
	return [(count_unique_blocks(byte_string), byte_string) for byte_string in cipher_bytes] #result


if __name__ == '__main__':
	x = hex_file_to_bytes("8.txt")
	a = count_unique_blocks(x[0])
	#print(a)
	b = detect_encrypted(x)
	print(sorted(b)[:3])
	# line with least amount of blocks has been encrypted


