from hex_to_base64 import string_to_bytearray
import binascii


def fixed_xor(a, b):
    hex_a = string_to_bytearray(a)
    hex_b = string_to_bytearray(b)
    if len(a) == len(b):
        result = ''.join([('%X' % (x^y)).lower() for x, y in zip(hex_a, hex_b)])        

        return result
    else:
        raise Exception

if __name__ == '__main__':
    a = "1c0111001f010100061a024b53535009181c"
    b = "686974207468652062756c6c277320657965"

    print(fixed_xor(a,b))
