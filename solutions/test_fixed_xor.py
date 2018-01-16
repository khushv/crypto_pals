import unittest
from fixed_xor import fixed_xor

class TestCase(unittest.TestCase):
    """Test for second challenge"""

    def test_hex_to_base64(self):
        """Does it convert hex to base64?"""
        a = "1c0111001f010100061a024b53535009181c"
        b = "686974207468652062756c6c277320657965"
        a_b_xor = "746865206b696420646f6e277420706c6179"
        self.assertEqual(fixed_xor(a, b), a_b_xor)

if __name__ == '__main__':
    unittest.main()
