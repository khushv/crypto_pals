import Cryptodome
from Cryptodome.Cipher import AES
from challenge_6 import base64_file_to_bytes

def decrypt_AES_ECB_bytes(cipher_bytes, key):
	if isinstance(key, str):
		key = key.encode('ascii')
	cipher_obj = AES.new(key, AES.MODE_ECB)
	decrypted_bytes = cipher_obj.decrypt(cipher_bytes)
	return decrypted_bytes.decode('ascii')
	

if __name__ == '__main__':
	cipher_text = base64_file_to_bytes("7.txt")
	x = decrypt_AES_ECB_bytes(cipher_text, "YELLOW SUBMARINE")
	print(x)
