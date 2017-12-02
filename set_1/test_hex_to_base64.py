import unittest
from hex_to_base64 import convert_hex_to_base64

class TestCase(unittest.TestCase):
    """Test for first class"""

    def test_hex_to_base64(self):
        """Does it convert hex to base64?"""
        input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        output = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
        self.assertEqual(convert_hex_to_base64(input), output)

if __name__ == '__main__':
    unittest.main()
