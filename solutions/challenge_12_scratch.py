	#setup
	BLOCK_SIZE = 16
	key_size = BLOCK_SIZE # can also be 24, 32
	en_key = sys.argv[1].encode('utf-8', 'surrogateescape')
	"""
	#sanity check
	test_input = "A" * 16 + "A" * 15 + "A"
	encrypted = ecb_oracle(test_input, BLOCK_SIZE)
	decrypted = decrypt_AES_ECB_bytes(encrypted[:16], en_key)
	print("Does input: ", test_input, " match decrypted output: ", 
		decrypted.decode('ascii'), " ?")
	"""
	my_input = "A" * 16 + "A" * 15 
	original = my_input
	print("Input: ", my_input)
	print("Length: ", len(my_input))	
	encrypted = ecb_oracle(my_input, BLOCK_SIZE)
	encrypted_blocks = keysize_blocks(BLOCK_SIZE, encrypted)
	print("Encrypted string: ", encrypted_blocks)
	print("Encrypted length: ", len(encrypted))
	x = find_letter(encrypted_blocks[1], "A"*15, ecb_oracle)
	print("First letter is: ", x)
	secret_key = ""
	secret_key = x
	my_input = block_fusion(my_input, x)
	print(my_input)
	encrypted = ecb_oracle(original, BLOCK_SIZE)
	encrypted_blocks = keysize_blocks(BLOCK_SIZE, encrypted)
	print("Encrypted blocks ", encrypted_blocks)
	x = find_letter(encrypted_blocks[1], my_input, ecb_oracle)
	print("Second letter is: ", x)
	import pdb; pdb.set_trace()

