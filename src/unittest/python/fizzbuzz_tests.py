from unittest import TestCase
from fizzbuzz import fizzBuzz

class fizzBuzzTest(TestCase):
    def test_if_3_is_lucky(self):
        fizzbuzz = fizzBuzz()
        self.assertEqual(fizzbuzz.getFizzBuzz(3), 'lucky')

    def test_if_9_is_fizz(self):
        fizzbuzz = fizzBuzz()
        self.assertEqual(fizzbuzz.getFizzBuzz(9), 'fizz')

    def test_if_5_is_buzz(self):
        fizzbuzz = fizzBuzz()
        self.assertEqual(fizzbuzz.getFizzBuzz(5), 'buzz')

    def test_if_10_is_buzz(self):
        fizzbuzz = fizzBuzz()
        self.assertEqual(fizzbuzz.getFizzBuzz(10), 'buzz')

    def test_if_15_is_fizzbuzz(self):
        fizzbuzz = fizzBuzz()
        self.assertEqual(fizzbuzz.getFizzBuzz(15), 'fizzbuzz')

    def test_if_4_is_4(self):
        fizzbuzz = fizzBuzz()
        self.assertEqual(fizzbuzz.getFizzBuzz(4), '4')

    def test_if_0_is_0(self):
        fizzbuzz = fizzBuzz()
        self.assertEqual(fizzbuzz.getFizzBuzz(0), '0')

    def test_if_fizzbuzz_list_is_initialized(self):
        fizzbuzz = fizzBuzz()
        self.assertListEqual(fizzbuzz.num_list, [])

    def test_if_fizzbuzz_start_sets(self):
        fizzbuzz = fizzBuzz()
        fizzbuzz.setFizzBuzzStart(1)
        self.assertEqual(fizzbuzz.start, 1)

    def test_if_fizzbuzz_start_sets(self):
        fizzbuzz = fizzBuzz()
        fizzbuzz.setFizzBuzzEnd(20)
        self.assertEqual(fizzbuzz.end, 20)

    def test_if_fizzbuzz_list_raises_start_exception(self):
        with self.assertRaises(ValueError):
            fizzbuzz = fizzBuzz()
            fizzbuzz.setFizzBuzzEnd(20)
            fizzbuzz.setList()

    def test_if_fizzbuzz_list_raises_end_exception(self):
        with self.assertRaises(ValueError):
            fizzbuzz = fizzBuzz()
            fizzbuzz.setFizzBuzzStart(11)
            fizzbuzz.setList()

    def test_if_fizbuzz_list_contains_start_to_end(self):
        fizzbuzz = fizzBuzz()
        fizzbuzz.setFizzBuzzStart(11)
        fizzbuzz.setFizzBuzzEnd(20)
        fizzbuzz.setList()
        expected = [i for i in range(11,21)]
        self.assertListEqual(fizzbuzz.num_list, expected)

    def test_if_fizbuzz_list_is_reversable(self):
        fizzbuzz = fizzBuzz()
        fizzbuzz.setFizzBuzzStart(20)
        fizzbuzz.setFizzBuzzEnd(11)
        fizzbuzz.setList()
        expected = [i for i in range(20,10,-1)]
        self.assertListEqual(fizzbuzz.num_list, expected)

    def test_if_makeFizzBuzz_returns_empty_list(self):
        fizzbuzz = fizzBuzz()
        fizzbuzz.makeFizzBuzz()
        self.assertListEqual(fizzbuzz.num_list, [])

    def test_if_fizzbuzz_list_is_converted_to_fizzbuzz(self):
        fizzbuzz = fizzBuzz()
        fizzbuzz.setFizzBuzzStart(11)
        fizzbuzz.setFizzBuzzEnd(20)
        fizzbuzz.setList()
        fizzbuzz.makeFizzBuzz()
        expected = ['11','fizz','lucky','14','fizzbuzz','16','17','fizz','19','buzz']
        self.assertListEqual(fizzbuzz.num_list, expected)

    def test_if_fizzbuzz_returns_a_string(self):
        fizzbuzz = fizzBuzz()
        fizzbuzz.setFizzBuzzStart(11)
        fizzbuzz.setFizzBuzzEnd(20)
        fizzbuzz.setList()
        fizzbuzz.makeFizzBuzz()
        expected = '11 fizz lucky 14 fizzbuzz 16 17 fizz 19 buzz'
        self.assertEqual(fizzbuzz.makeOutputString(), expected)
        
    def test_if_fizzMyBuzz_returns_correct_format(self):
        fizzbuzz = fizzBuzz()
        expected = '11 fizz lucky 14 fizzbuzz 16 17 fizz 19 buzz'
        self.assertEqual(fizzbuzz.fizzMyBuzz(11,20), expected)
        
    def test_if_fizzMyBuzz_raises_start_exception(self):
        with self.assertRaises(ValueError):
            fizzbuzz = fizzBuzz()
            fizzbuzz.fizzMyBuzz(None,20)

    def test_if_fizzMyBuzz_raises_end_exception(self):
        with self.assertRaises(ValueError):
            fizzbuzz = fizzBuzz()
            fizzbuzz.fizzMyBuzz(11,None)









