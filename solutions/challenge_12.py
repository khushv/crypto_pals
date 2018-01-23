import sys
from base64 import b64decode
from os import urandom
from challenge_6 import keysize_blocks
from challenge_7 import decrypt_AES_ECB_bytes
from challenge_9 import pad
from challenge_10 import encrypt_AES_ECB
from challenge_11 import detect_ecb


to_decrypt = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg"
"aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq"
"dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg"
"YnkK"

fake_string = "ZmFrZSBzdHJpbmcK"



def ecb_oracle(plain_bytes, block_size=16):
	if isinstance(plain_bytes, str):
		plain_bytes = plain_bytes.encode('ascii') 
	secret_string = b64decode(fake_string)
	plain_bytes += secret_string
	plain_bytes = pad(plain_bytes, block_size)	
	return encrypt_AES_ECB(plain_bytes, en_key)


def find_letter(target_block, input, encryption_oracle):
	import pdb; pdb.set_trace()
	letter_dict = {}
	for i in range(32, 127):
		value = chr(i)
		plaintext = input + value
		encrypted_input = encryption_oracle(plaintext)[:16]
		letter_dict[encrypted_input] = value
	print(len(letter_dict))
	return letter_dict[target_block]

if __name__ == '__main__':
	#setup
	BLOCK_SIZE = 16
	key_size = BLOCK_SIZE # can also be 24, 32
	en_key = sys.argv[1].encode('utf-8', 'surrogateescape')
	"""	
	#sanity check
	test_input = "A" * 16 + "A" * 15 + "A"
	encrypted = ecb_oracle(test_input, BLOCK_SIZE)
	decrypted = decrypt_AES_ECB_bytes(encrypted[:16], key)
	print("Does input: ", test_input, " match decrypted output: ", 
		decrypted.decode('ascii'), " ?")
	"""
	my_input = "A" * 16 + "A" * 15 
	print("Input: ", my_input)
	print("Length: ", len(my_input))	
	encrypted = ecb_oracle(my_input, BLOCK_SIZE)
	encrypted_blocks = keysize_blocks(BLOCK_SIZE, encrypted)
	print("Encrypted string: ", encrypted_blocks)
	print("Encrypted length: ", len(encrypted))
	x = find_letter(encrypted_blocks[0], "A"*15, ecb_oracle)
	print(x)



"""
run in bash first:
key=`dd if=/dev/urandom bs=16 count=1`
python challenge_12.py key
dont forget to change key size


Feed identical bytes of your-string to the function 1 at a time --- start with 1 byte ("A"), then "AA", then "AAA" and so on. Discover the block size of the cipher. You know it, but do this step anyway.

Length of block size is 16


Detect that the function is using ECB. You already know, but do this step anyways.

Oracle function detects duplicate blocks. Is ECB!


Knowing the block size, craft an input block that is exactly 1 byte short (for instance, if the block size is 8 bytes, make "AAAAAAA"). Think about what the oracle function is going to put in that last byte position.


Make a dictionary of every possible last byte by feeding different strings to the oracle; for instance, "AAAAAAAA", "AAAAAAAB", "AAAAAAAC", remembering the first block of each invocation.
Match the output of the one-byte-short input to one of the entries in your dictionary. You've now discovered the first byte of unknown-string.
Repeat for the next byte.
"""
