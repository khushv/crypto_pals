import sys
from base64 import b64decode
from os import urandom
from challenge_6 import keysize_blocks
from challenge_7 import decrypt_AES_ECB_bytes
from challenge_9 import pad
from challenge_10 import encrypt_AES_ECB
from challenge_11 import detect_ecb


to_decrypt = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg" \
"aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq" \
"dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg" \
"YnkKUm9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg" \
"aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq" \
"dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg" \
"YnkK"

fake_string = "ZmFrZSBzdHJpbmcKYmxhaAo="



def ecb_oracle(plain_bytes, block_size):
	if isinstance(plain_bytes, str):
		plain_bytes = plain_bytes.encode('ascii') 
	#secret_string = b64decode(fake_string)
	secret_string = b64decode(to_decrypt)
	plain_bytes += secret_string
	plain_bytes = pad(plain_bytes, block_size)
	return encrypt_AES_ECB(plain_bytes, en_key)


def find_letter(target_block, input, decoded_key, encryption_oracle, block_size):
	#import pdb; pdb.set_trace()
	letter_dict = {}
	# watch out, hardcoding blocksize here
	input += decoded_key
	input = input[-(block_size-1):]
	for i in range(32, 127):
		value = chr(i)
		plaintext = input + value
		encrypted_input = encryption_oracle(plaintext, block_size)[:BLOCK_SIZE]
		letter_dict[encrypted_input] = value
	for i in [1,2,3,4,5,6,7,8,9,10]:
		value = chr(i)
		plaintext = input + value
		encrypted_input = encryption_oracle(plaintext, block_size)[:BLOCK_SIZE]
		letter_dict[encrypted_input] = value
	return letter_dict[target_block]


def byte_at_ecb(secret_key_len, oracle_function=None):
	# set key to zero 
	decoded_key = ""
	initial_length = secret_key_len
	
	while initial_length:
		print("Length ", initial_length)
		initial_length -= 1
		my_input = "A" * initial_length
		#print("Initial length" , initial_length)
		print("Input: ", my_input)
		encrypted = ecb_oracle(my_input, BLOCK_SIZE)
		encrypted_blocks = keysize_blocks(BLOCK_SIZE, encrypted)
		#print(encrypted_blocks)
		block_to_use = (secret_key_len // BLOCK_SIZE) - 1
		print("Block to use: ", block_to_use)
		try:
			x = find_letter(encrypted_blocks[block_to_use], my_input, decoded_key, ecb_oracle, BLOCK_SIZE)
			decoded_key += x
		except: 
			print("Finished decrypting or key lookup error")
			break
		print("Key so far: ", decoded_key)
	
	
if __name__ == '__main__':
	en_key = sys.argv[1].encode('utf-8', 'surrogateescape')
	BLOCK_SIZE = 16
	
	# calculate block size, ignoring above where we don't program own encrypting function/oracle
	token = 0
	first_calc = False
	length = len(ecb_oracle("A"*token, BLOCK_SIZE))
	while not first_calc:
		token += 1
		if len(ecb_oracle("A"*token, BLOCK_SIZE)) != length:
			block_size = len(ecb_oracle("A"*token, BLOCK_SIZE)) - length
			break
	print("BLOCK SIZE: ", block_size)

	
	# calculate how long secret information is:
	num_blocks_req = len(ecb_oracle("", BLOCK_SIZE)) // BLOCK_SIZE
	print("Will require at least ", num_blocks_req, " worth of blocks")
	initial_length = num_blocks_req * BLOCK_SIZE 
	a = byte_at_ecb(initial_length, None)



"""
run in bash first:
key=`dd if=/dev/urandom bs=16 count=1`
python challenge_12.py key
dont forget to change key size


Feed identical bytes of your-string to the function 1 at a time --- start with 1 byte ("A"), then "AA", then "AAA" and so on. Discover the block size of the cipher. You know it, but do this step anyway.
->Length of block size is 16

Detect that the function is using ECB. You already know, but do this step anyways.
->Oracle function detects duplicate blocks. Is ECB!

Knowing the block size, craft an input block that is exactly 1 byte short (for instance, if the block size is 8 bytes, make "AAAAAAA"). Think about what the oracle function is going to put in that last byte position.

Make a dictionary of every possible last byte by feeding different strings to the oracle; for instance, "AAAAAAAA", "AAAAAAAB", "AAAAAAAC", remembering the first block of each invocation.
Match the output of the one-byte-short input to one of the entries in your dictionary. You've now discovered the first byte of unknown-string.
Repeat for the next byte.
"""
