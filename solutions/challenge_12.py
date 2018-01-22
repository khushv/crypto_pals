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
	return encrypt_AES_ECB(plain_bytes, key)

if __name__ == '__main__':
	#setup
	BLOCK_SIZE = 16
	key_size = 16 # 24 or 32
	my_input = "A" * 33
	key = sys.argv[1].encode('utf-8', 'surrogateescape')
	encrypted_string = ecb_oracle(my_input, key, BLOCK_SIZE)
	


"""
run in bash first:
key=`dd if=/dev/urandom bs=16 count=1`
python challenge_12.py key
dont forget to change key size
"""
