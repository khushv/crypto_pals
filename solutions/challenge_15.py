

def pkcs7_pad_validate(plaintext):
	last_letter = plaintext[-1].encode('ascii')
	ll = int.from_bytes(last_letter, byteorder='big')
	buffer = plaintext[-ll:].encode('ascii')
	for char in buffer:
		#print("Compare", char, " with ", last_letter)
		if char != ll:
			raise Exception("Invalid padding")
	return True
	
def pkcs7_pad_validate_bytes(plaintext):
	last_letter = plaintext[-1]
	"""
	if last_letter > 16 and len(plaintext) % 16 == 0:
		return True
	else:
		return False
	"""
	buffer = plaintext[-last_letter:]
	token = 0
	for char in buffer:
		#print("token: ", token)
		token += 1
		#print("Compare", char, " with ", last_letter)
		if char != last_letter:
			#raise Exception("Invalid padding")
			return False
	return True


if __name__ == '__main__':
	a = "ICE ICE BABY\x04\x04\x04\x04"
	print(pkcs7_pad_validate(a))

	b = "ICE ICE BABY\x05\x05\x05\x05"
	print(pkcs7_pad_validate(b))

	c = "ICE ICE BABY\x01\x02\x03\x04"
	print(pkcs7_pad_validate(c))





"""
PKCS#7 padding validation
Write a function that takes a plaintext, determines if it has valid PKCS#7 padding, and strips the padding off.

The string:

"ICE ICE BABY\x04\x04\x04\x04"
... has valid padding, and produces the result "ICE ICE BABY".

The string:

"ICE ICE BABY\x05\x05\x05\x05"
... does not have valid padding, nor does:

"ICE ICE BABY\x01\x02\x03\x04"
If you are writing in a language with exceptions, like Python or Ruby, make your function throw an exception on bad padding.

Crypto nerds know where we're going with this. Bear with us.

"""
