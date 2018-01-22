import sys
from base64 import b64decode
from os import urandom
from challenge_9 import pad
from challenge_10 import encrypt_AES_ECB
from challenge_11 import detect_ecb


to_decrypt = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg"
"aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq"
"dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg"
"YnkK"

fake_string = "ZmFrZSBzdHJpbmcK"



def ecb_oracle(plain_bytes, key, block_size):
	if isinstance(plain_bytes, str):
		plain_bytes = plain_bytes.encode('ascii') 
	#import pdb; pdb.set_trace()
	secret_string = b64decode(fake_string)
	plain_bytes += secret_string
	plain_bytes = pad(plain_bytes, block_size)
	print("Length of plaintext: ", len(plain_bytes))
	return encrypt_AES_ECB(plain_bytes, key)

if __name__ == '__main__':
	#setup
	BLOCK_SIZE = 16
	key_size = 16 # 24 or 32
	my_input = "A" * 32
	key = sys.argv[1].encode('utf-8', 'surrogateescape')
	encrypted_string = ecb_oracle(my_input, key, BLOCK_SIZE)
	print("Length of encrypted: ", len(encrypted_string))
	value = detect_ecb(encrypted_string, BLOCK_SIZE)
	print("ECB mode detected: ", value)


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
