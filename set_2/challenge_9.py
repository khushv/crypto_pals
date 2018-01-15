

def pad(sample, block_size):
	sample_size = len(sample)
	while sample_size > block_size:
		sample_size -= block_size
	sample += b"\x04" * (block_size - sample_size)
	return sample

if __name__ == '__main__':
	a = "abcdefghiklmnop".encode('ascii')
	pad(a, 4)
	
	
