import base64

def convert_hex_to_base64(sample):
    converted_bytes = string_to_bytearray(sample)
    return bytearray_to_base64(converted_bytes)


def string_to_bytearray(sample):
    return bytearray.fromhex(sample)

def bytearray_to_base64(sample):
    return base64.b64encode(sample)


if __name__ == '__main__':
    sample = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f"
    "69736f6e6f7573206d757368726f6f6d"

    print(convert_hex_to_base64(sample))
