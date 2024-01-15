import unittest
from PnoneNumberBr import PnoneNumberBr

class PhonesNumbersBrTest(unittest.TestCase):

    def test_valid_number(self):
        phoneNumber = PnoneNumberBr("553399007243")
        self.assertEqual(phoneNumber.getNumber(), "+55(33)99007-243")

    def test_invalid_number(self):
        with self.assertRaises(ValueError):
            PnoneNumberBr("12345")

    def test_number_with_ninth_digit(self):
        phoneNumber = PnoneNumberBr("553312345678")
        self.assertEqual(phoneNumber.getNumber(), "+55(33)12345-678")

    def test_number_with_ninth_digit_alternative_format(self):
        phoneNumber = PnoneNumberBr("5533123456789")
        self.assertEqual(phoneNumber.getNumber(), "+55(33)12345-6789")

    def test_number_with_ninth_digit_alternative_format_without_country_code(self):
        phoneNumber = PnoneNumberBr("33123456789")
        self.assertEqual(phoneNumber.getNumber(), "+55(33)12345-6789")

    def test_invalid_number_with_ninth_digit_alternative_format_without_country_code(self):
        with self.assertRaises(ValueError):
            PnoneNumberBr("3312345678910")

    def test_invalid_number_with_ninth_digit_alternative_format_invalid(self):
        with self.assertRaises(ValueError):
            PnoneNumberBr("55123456789a")

if __name__ == '__main__':
    unittest.main()