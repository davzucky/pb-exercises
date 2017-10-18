from unittest import TestCase


def bytes_to_str(b, encoding='ascii'):
    '''Returns a string version of the bytes'''
    return b.encode(encoding)


def str_to_bytes(s, encoding='ascii'):
    '''Returns a bytes version of the string'''
    return s.decode(encoding)


class HelperTest(TestCase):

    def test_bytes(self):

        b = b'hello world'
        s = 'hello world'
        self.assertEqual(b, str_to_bytes(s))
        self.assertEqual(s, bytes_to_str(b))
