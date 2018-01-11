import Cryptodome
from Cryptodome.Cipher import AES
from challenge_6 import base64_file_to_bytes

def decrypt_base64_AES(file, key):
	cipher_bytes = base64_file_to_bytes(file)
	key_bytes = key.encode('ascii')
	cipher_obj = AES.new(key_bytes, AES.MODE_ECB)
	decrypted_bytes = cipher_obj.decrypt(cipher_bytes)
	return decrypted_bytes.decode('ascii')
	

if __name__ == '__main__':
	x = decrypt_base64_AES("7.txt", "YELLOW SUBMARINE")
	print(x)
