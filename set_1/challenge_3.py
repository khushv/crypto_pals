"""Find key for single character XOR'd message"""
"""By using character frequency"""
"""http://cryptopals.com/sets/1/challenges/3"""

from hex_to_base64 import string_to_bytearray

def xor_single(sample, xor_char):
    in_bytes = string_to_bytearray(sample)
    output = bytearray()
    for i in in_bytes:
        output.append(i^xor_char)
    print(output.__repr__())


def charater_frequency(bytearray_sample):
    start = bytes("61")
    end = bytes("7a")

    

if __name__ == '__main__':
    a = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    for i in range(0, 255):
        xor_single(a, i)
