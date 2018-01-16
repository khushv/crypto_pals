

def pad(sample, block_size):
	sample_size = len(sample)
	while sample_size > block_size:
		sample_size -= block_size
	sample = sample + b"\x04" * (block_size - sample_size)
	return sample

if __name__ == '__main__':
	a = "YELLOW SUBMARINE".encode('ascii')
	print(pad(a, 20))
	
	
