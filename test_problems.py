import unittest
from problem_solving import (
    clean_and_reverse,
    group_by_department,
    sum_of_primes,
    compress_string,
    get_second_largest,
    sum_main_diagonal,
    validate_ipv4
)

class TestGauntlet(unittest.TestCase):

    def test_clean_and_reverse(self):
        self.assertEqual(clean_and_reverse("  Hello "), "olleh")
        self.assertEqual(clean_and_reverse("PYTHON"), "nohtyp")
        self.assertEqual(clean_and_reverse(""), "")

    def test_group_by_department(self):
        input_data = [
            {'name': 'Alice', 'dept': 'HR'},
            {'name': 'Bob', 'dept': 'Eng'},
            {'name': 'Charlie', 'dept': 'HR'},
            {'name': 'David', 'dept': 'Eng'},
            {'name': 'Eve', 'dept': 'Sales'}
        ]
        
        expected = {
            'HR': ['Alice', 'Charlie'],
            'Eng': ['Bob', 'David'],
            'Sales': ['Eve']
        }
        
        result = group_by_department(input_data)
        
        self.assertTrue('HR' in result)
        self.assertEqual(result['HR'], ['Alice', 'Charlie'])
        self.assertEqual(result['Sales'], ['Eve'])

    def test_sum_of_primes(self):
        print("Testing Level 3: Prime Logic...")
        self.assertEqual(sum_of_primes(10), 17)
        self.assertEqual(sum_of_primes(20), 77)
        self.assertEqual(sum_of_primes(1), 0)
        self.assertEqual(sum_of_primes(2), 2)

    def test_compress_string(self):
        self.assertEqual(compress_string("AAA"), "3A")
        self.assertEqual(compress_string("AAABBC"), "3A2B1C")
        self.assertEqual(compress_string("AAABBAA"), "3A2B2A")
        self.assertEqual(compress_string(""), "")
        self.assertEqual(compress_string("A"), "1A")

    def test_get_second_largest(self):
        self.assertEqual(get_second_largest([10, 20, 4, 45, 99]), 45)
        self.assertEqual(get_second_largest([1, 2]), 1)
        self.assertEqual(get_second_largest([-10, -2, -5]), -5)

    def test_sum_main_diagonal(self):
        matrix = [
            [10, 2, 3],
            [4, 10, 6],
            [7, 8, 10]
        ]
        self.assertEqual(sum_main_diagonal(matrix), 30)
        
        matrix_small = [[1, 1], [1, 1]]
        self.assertEqual(sum_main_diagonal(matrix_small), 2)

    def test_validate_ipv4(self):
        self.assertTrue(validate_ipv4("192.168.0.1"))
        self.assertTrue(validate_ipv4("0.0.0.0"))
        self.assertTrue(validate_ipv4("255.255.255.255"))
        
        self.assertFalse(validate_ipv4("256.0.0.0"))
        self.assertFalse(validate_ipv4("-1.0.0.0"))
        self.assertFalse(validate_ipv4("192.168.1"))
        self.assertFalse(validate_ipv4("192.168.a.1"))
        self.assertFalse(validate_ipv4("..."))

if __name__ == '__main__':
    unittest.main(failfast=True, verbosity=0)
