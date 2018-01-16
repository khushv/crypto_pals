from Cryptodome.Cipher import AES
from challenge_5 import xor_bytes
from challenge_6 import keysize_blocks, base64_file_to_bytes
from challenge_7 import decrypt_AES_ECB_bytes
from challenge_9 import pad


def encrypt_AES_ECB(plaintext, key):
	# dirty way of making sure its a string and not byte array, needed?
	if isinstance(key, str):
		key = key.encode('ascii')
	cipher_obj = AES.new(key, AES.MODE_ECB)
	encrypted_bytes = cipher_obj.encrypt(plaintext)
	return encrypted_bytes
	

def encrypt_AES_CBC(plaintext, iv, key, block_size):
	encrypted_bytes = bytes()
	plaintext = keysize_blocks(block_size, plaintext)
	#initial iv
	xored_plaintext  = xor_bytes(plaintext.pop(0), iv)
	encrypted_bytes += encrypt_AES_ECB(xored_plaintext, key)
	while plaintext:
		xored_plaintext = xor_bytes(plaintext.pop(0), encrypted_bytes[-BLOCK_SIZE:])
		encrypted_bytes += encrypt_AES_ECB(xored_plaintext, key)
	return encrypted_bytes


def decrypt_AES_CBC(ciphertext, iv, key, block_size):
	plaintext = bytes()
	ciphertext = keysize_blocks(block_size, ciphertext)
	
	intermediate = ciphertext.pop(0)
	decrypted_bytes = decrypt_AES_ECB_bytes(intermediate, key)
	plaintext += xor_bytes(decrypted_bytes, iv)
	iv = intermediate
	
	while ciphertext:
		intermediate = ciphertext.pop(0)
		decrypted_bytes = decrypt_AES_ECB_bytes(intermediate, key)
		plaintext += xor_bytes(decrypted_bytes, iv)
		iv = intermediate
	return plaintext
		
	

if __name__ == '__main__':
	BLOCK_SIZE = 16
	iv = ("\x00" * BLOCK_SIZE).encode('ascii')
	
	key = pad("secret_password".encode('ascii'), BLOCK_SIZE)
	message = pad("hello world, the quick brown fox".encode('ascii'), BLOCK_SIZE)
	
	x = encrypt_AES_CBC(message, iv, key, BLOCK_SIZE)
	#print(x)
	#x = encrypt_AES_ECB(message, key)
	#print(x)
	#y = decrypt_AES_ECB_bytes(x, key)
	#print(y)
	y = decrypt_AES_CBC(x, iv, key, BLOCK_SIZE)
	print(y.decode('ascii'))
	
	key2 = pad("YELLOW SUBMARINE".encode('ascii'), BLOCK_SIZE)
	cipher_message = base64_file_to_bytes('10.txt')
	decrypted = decrypt_AES_CBC(cipher_message, iv, key2, BLOCK_SIZE)
	print(decrypted.decode('ascii'))


