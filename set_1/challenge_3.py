"""Find key for single character XOR'd message"""
"""By using character frequency"""
"""http://cryptopals.com/sets/1/challenges/3"""

from hex_to_base64 import string_to_bytearray
from binascii import unhexlify

def xor_single(sample, xor_char):
    in_bytes = unhexlify(sample)
    output = bytearray()
    for i in in_bytes:
        output.append(i^xor_char)
    print(output.__repr__())
    return output

def charater_frequency(bytearray_sample):
    start_upper = ord("A")
    end_upper = ord("Z")

    start_lower = ord("a")
    end_lower = ord("z")



if __name__ == '__main__':

    a = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    b = xor_single(a, 56)

    char_freq = {}
    start_upper = ord("A")
    end_upper = ord("Z")

    for i in b:
        print(i)
        if start_upper <= i <= end_upper:
            dict_value = chr(i).lower()
            if dict_value in char_freq:
                char_freq[dict_value] += 1
            else:
                char_freq[dict_value] = 1

    print(char_freq)
