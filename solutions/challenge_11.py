from os import urandom
from random import randint
from challenge_6 import keysize_blocks
from challenge_8 import detect_encrypted
from challenge_9 import pad
from challenge_10 import encrypt_AES_ECB, encrypt_AES_CBC

def detect_ecb(plaintext, block_size):
	plaintext = keysize_blocks(block_size, plaintext)
	#print("Number of plaintext: ", len(plaintext))
	#print("Set number: ", len(set(plaintext)))
	if len(set(plaintext)) != len(plaintext):
		#probs ecb
		return True
	else:
		return False

def encryption_oracle(plain_bytes, block_size):
	key = urandom(block_size)
	append = urandom(randint(5,10))
	preppend = urandom(randint(5,10))
	plain_bytes = append + plain_bytes + preppend
	plain_bytes = pad(plain_bytes, block_size)
	print("Plainbyte length: ", len(plain_bytes))
	if randint(0,1):
		encrypted = encrypt_AES_ECB(plain_bytes, key)
		#print("Making ECB")
		return (0, encrypted)
	else:
		iv = urandom(block_size)
		encrypted = encrypt_AES_CBC(plain_bytes, iv, key, block_size)
		#print("Making CBC")
		return (1, encrypted)



if __name__ == '__main__':
	BLOCK_SIZE = 16
	plaintext = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA".encode('ascii')
	print(len(plaintext))
	for i in range(0, 10):
		encrypted = encryption_oracle(plaintext, BLOCK_SIZE)
		if encrypted[0] == 0 and detect_ecb(encrypted[1], BLOCK_SIZE):
			print("True")
		elif encrypted[0] == 1 and not detect_ecb(encrypted[1], BLOCK_SIZE):
			print("True CBC")
		else:
			print("FALSE")
		

