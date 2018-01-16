from Cryptodome.Cipher import AES
from challenge_5 import xor_bytes
from challenge_6 import keysize_blocks
from challenge_7 import decrypt_AES_ECB_bytes
from challenge_9 import pad


def encrypt_AES_ECB(plaintext, key):
	# dirty way of making sure its a string and not byte array, needed?
	if isinstance(key, str):
		key = key.encode('ascii')
	cipher_obj = AES.new(key, AES.MODE_ECB)
	print("plaintext: ", plaintext)
	encrypted_bytes = cipher_obj.encrypt(plaintext)
	return encrypted_bytes
	

def encrypt_AES_CBC(plaintext, iv, key, block_size):
	encrypted_bytes = bytes()
	plaintext = keysize_blocks(block_size, plaintext)
	xored_plaintext  = xor_bytes(plaintext.pop(0), iv)
	encrypted_bytes += encrypt_AES_ECB(xored_plaintext, key)
	while plaintext:
		xored_plaintext = xor_bytes(plaintext.pop(0), encrypted_bytes[-BLOCK_SIZE:])
		encrypted_bytes += encrypt_AES_ECB(xored_plaintext, key)
	return encrypted_bytes


def decrypt_AES_CBC(

if __name__ == '__main__':
	BLOCK_SIZE = 16
	iv = ("\x00" * BLOCK_SIZE).encode('ascii')
	print("IV is: ", iv)
	
	key = pad("secret_password".encode('ascii'), BLOCK_SIZE)
	print("Key is: ", key)
	
	message = pad("hello world, the quick brown fox".encode('ascii'), BLOCK_SIZE)
	#print("Plaintext message is: ", message)
	
	x = encrypt_AES_CBC(message, iv, key, BLOCK_SIZE)
	print(x)
	#x = encrypt_AES_ECB(message, key)
	#print(x)
	#y = decrypt_AES_ECB_bytes(x, key)
	#print(y)



