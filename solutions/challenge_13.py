import json
import os
from random import randrange
from challenge_9 import pad
from challenge_10 import encrypt_AES_ECB

def json_parse(cookie_str):
	cookie_obj = {}
	parameters = cookie_str.split("&")
	if parameters:
		for parameter in parameters:
			print(parameter)
			k, v = parameter.split("=")
			cookie_obj[k] = v
		return json.dumps(cookie_obj)
	else:
		raise Exception("No parameters")
	

def encode_user_profile(email_address, role="user"):
	cookie_str = ""
	cookie_str = "email=" + email_address.replace('&', '').replace('=', '')
	cookie_str += "&uid=" + str(randrange(0, 50)) 
	cookie_str += "&role=" + role.replace('&', '').replace('=', '')
	return cookie_str


def encrypt_profile(encoded_str, key):
	encoded_str = encoded_str.encode('ascii')
	encoded_str = pad(encoded.encode('ascii'), BLOCK_SIZE)
	return encrypt_AES_ECB(encoded_str, key)
	

if __name__ == '__main__':
	BLOCK_SIZE = 16
	key = os.urandom(BLOCK_SIZE)
	encoded = encode_user_profile("bob@bob.com", "user")
	x = encrypt_profile(encoded, key)
	print(x)
	
	
	
