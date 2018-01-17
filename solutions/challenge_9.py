

def pad(sample, block_size):
	sample_size = len(sample)
	while sample_size > block_size:
		sample_size -= block_size
	pad_amount = block_size - sample_size
	padded_bytes = pad_amount * chr(pad_amount)
	sample = sample + padded_bytes.encode('ascii')
	return sample

if __name__ == '__main__':
	a = "YELLOW SUBMARINE".encode('ascii')
	print(pad(a, 20))
	
	
