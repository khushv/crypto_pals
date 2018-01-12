import base64
from binascii import unhexlify
from collections import Counter

def hex_file_to_bytes(filename):
	with open(filename) as f:
		data = [unhexlify(line.strip("\n")) for line in f]
	return data


def count_blocks(cipher_bytes, block_size=16):
	chopped = [cipher_bytes[i*block_size:(i+1)*block_size] for i in range(len(cipher_bytes)//block_size)]
	chopped_counted = Counter(chopped)
	return sum(chopped_counted.values())


def get_all_blocks(cipher_bytes, block_size=16):
	result = {}
	for byte_string in cipher_bytes:
		result[byte_string] = count_blocks(byte_string)
	return result


if __name__ == '__main__':
	x = hex_file_to_bytes("8.txt")
	print(len(x))
	a = count_blocks(x[0])
	b = get_all_blocks(x)
	print(b.values())


