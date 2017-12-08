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



if __name__ == '__main__':
    a = "Burning 'em, if you ain't quick and nimble\n" \
        "I go crazy when I hear a cymbal"
    print(a)
    a_bytes = text_to_bytes(a)
    a_xor = xor_bytes(a_bytes, text_to_bytes("ICE"))
    print(byte_to_string(a_xor))
