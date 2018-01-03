"""Find key for single character XOR'd message"""
"""By using character frequency"""
"""http://cryptopals.com/sets/1/challenges/3"""

from hex_to_base64 import string_to_bytearray
from binascii import unhexlify

def xor_single(sample, xor_char):
	in_bytes = unhexlify(sample)
	output = bytearray()
	for i in in_bytes:
		output.append(i^xor_char)
	return output


def xor_single_bytes(sample, xor_char):
	output = bytearray()
	for i in sample:
		output.append(i^xor_char)
	return output

def character_frequency(bytearray_sample):
	start_upper = ord("A")
	end_upper = ord("Z")

	start_lower = ord("a")
	end_lower = ord("z")

	char_freq_dict = {}
	for i in bytearray_sample:
		add_to_dict(start_upper, end_upper, i, char_freq_dict)
		add_to_dict(start_lower, end_lower, i, char_freq_dict)
	return char_freq_dict

def add_to_dict(lower, upper, letter, letter_dict):
	if lower <= letter <= upper:
		dict_value = chr(letter).lower()
		# replace below with defaultdict
		if dict_value in letter_dict:
			letter_dict[dict_value] += 1
		else:
			letter_dict[dict_value] = 1


def etaoin_frequency(chars_dict):
	if not chars_dict:
		return "10000000"
	else:
		total_chars = sum(chars_dict.values())
		frequency = {}
		for key, value  in chars_dict.items():
			frequency[key] = value / total_chars

		x = sorted(k for k,v in frequency.items())
		x_string = ''.join(x)
		#blahblah = my_levenshtein("etaoinshrdlucmfgypwbvkxjqz", x_string)
		#only returning total number of chars, overcomplicating problem
		return total_chars


def my_levenshtein(s1, s2):
	if len(s1) < len(s2):
		return my_levenshtein(s2, s1)

	# len(s1) >= len(s2)
	if len(s2) == 0:
		return len(s1)

	previous_row = range(len(s2) + 1)
	for i, c1 in enumerate(s1):
		current_row = [i + 1]
		for j, c2 in enumerate(s2):
			insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
			deletions = current_row[j] + 1	   # than s2
			substitutions = previous_row[j] + (c1 != c2)
			current_row.append(min(insertions, deletions, substitutions))
		previous_row = current_row

	return previous_row[-1]


def xor_brute(text, cut=5):
	list_chars = []
	for i in range(0, 255):
		xord = xor_single(text, i)
		xord_freq = character_frequency(xord)
		if xord_freq:
			lev = etaoin_frequency(xord_freq)
			#add to list, the char count, xor_bit and the string
			list_chars.append((lev, i, xord))
	sorted_char_freq = sorted(list_chars, reverse=True)
	return sorted_char_freq[:cut] # add top 5 for less text


def xor_brute_bytes(text, cut=5):
	list_chars = []
	for i in range(0, 255):
		xord = xor_single_bytes(text, i)
		xord_freq = character_frequency(xord)
		if xord_freq:
			lev = etaoin_frequency(xord_freq)
			#add to list, the char count, xor_bit and the string
			list_chars.append((lev, i, xord))
	sorted_char_freq = sorted(list_chars, reverse=True)
	return sorted_char_freq[:cut] # add top 5 for less text



if __name__ == '__main__':

	a = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
	print(xor_brute(a))
