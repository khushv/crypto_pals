from Cryptodome.Cipher import AES
from challenge_7 import decrypt_AES_ECB_bytes


def encrypt_AES_ECB(cipher_bytes, key):
	# dirty way of making sure its a string and not byte array, needed?
	if isinstance(key, str):
		key_bytes = key.encode('ascii')
	cipher_obj = AES.new(key_bytes, AES.MODE_ECB)
	encrypted_bytes = cipher_obj.encrypt(cipher_bytes)
	return encrypted_bytes
	
	
if __name__ == '__main__':
	
	key = 16*'\x00'
	x = encrypt_AES_ECB(b'hello world, the quick brown fox', key)
	print(x)
	y = decrypt_AES_ECB_bytes(x, key)
	print(y)
