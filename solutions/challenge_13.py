import json
from random import randrange

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

if __name__ == '__main__':
	print(encode_user_profile("bob@bob.com", "user"))
