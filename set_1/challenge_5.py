"""
Encrypt it, under the key "ICE", using repeating-key XOR.
"""

import binascii

def text_to_bytes(sample):
    return sample.encode('ascii')


def xor_bytes(sample, key):
    key_pointer = 0
    key_len = len(key)
    result = bytearray()
    for i in sample:
        #print("letter to xor: ", i)
        #print("key to xor: ", key[key_pointer % key_len])
        result.append(i ^ key[key_pointer % key_len])
        key_pointer += 1
    return result


def byte_to_string(sample):
    return binascii.hexlify(sample)


def repeating_key_xor(sample, key):
    sample_byte = text_to_bytes(sample)
    key_byte = text_to_bytes(key)
    sample_xor = xor_bytes(sample_byte, key_byte)
    return byte_to_string(sample_xor)

if __name__ == '__main__':
    a = "Burning 'em, if you ain't quick and nimble\n" \
        "I go crazy when I hear a cymbal"
    print(a)
    key = "ICE"
    # works well, not sure if output should be in two lines
    # output should be
    #0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
    #a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
    print(repeating_key_xor(a, key))
