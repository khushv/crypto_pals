"""
Detect single-character XOR
One of the 60-character strings in this file has been encrypted by single-character XOR.

Find it.
"""

from challenge_3 import xor_brute


if __name__ == '__main__':
#	with open("4.txt") as f:
#		read_data = f.readline()
	lines = [line.rstrip('\n') for line in open('4.txt')]
	bruteforce_xor = [xor_brute(line, 2) for line in lines]
	print(sorted(bruteforce_xor), "\n\n")

	#Character count, bit xor'd
	#24, 53, bytearray(b'Now that the party is jumping\n'
