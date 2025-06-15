import unittest
from checkprimenum import is_prime

class TestIsPrime(unittest.TestCase):
    def test_primes(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        for p in primes:
            with self.subTest(p=p):
                self.assertTrue(is_prime(p))

    def test_non_primes(self):
        non_primes = [4, 6, 8, 9, 10, 12, 14, 15]
        for n in non_primes:
            with self.subTest(n=n):
                self.assertFalse(is_prime(n))

if __name__ == '__main__':
    unittest.main()
