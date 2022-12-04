from unittest import TestCase

from day2 import is_valid_password, valid_toboggan_password


class IsValidPasswordTest(TestCase):
    def test_knows_valid_password(self):
        """is_valid_password should know if a password is valid"""
        assert is_valid_password(1, 3, 'a', 'abcde')
        assert not is_valid_password(1, 3, 'b', 'cdefg')
        assert is_valid_password(2, 9, 'c', 'ccccccccc')


class ValidTobogganPassword(TestCase):
    def test_knows_valid_password(self):
        """valid_toboggan_password should know if a password is valid"""
        assert valid_toboggan_password(1, 3, 'a', 'abcde')
        assert not valid_toboggan_password(1, 3, 'b', 'cdefg')
        assert not valid_toboggan_password(2, 9, 'c', 'ccccccccc')
