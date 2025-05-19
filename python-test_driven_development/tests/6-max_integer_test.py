#!/usr/bin/python3
'''Unittest for max_integer([..])
'''
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''Unit test class'''

    def test_ordered_list(self):
        '''Ordered lists unit tests'''
        ordered_list_1 = [1, 2, 3, 4]
        ordered_list_2 = [-50, 20, 37, 425]
        
        self.assertEqual(max_integer(ordered_list_1), 4)
        self.assertEqual(max_integer(ordered_list_2), 425)

        self.assertNotEqual(max_integer(ordered_list_1), 1)
        self.assertNotEqual(max_integer(ordered_list_1), 2)
        self.assertNotEqual(max_integer(ordered_list_1), 3)

        self.assertNotEqual(max_integer(ordered_list_2), -50)
        self.assertNotEqual(max_integer(ordered_list_2), 20)
        self.assertNotEqual(max_integer(ordered_list_2), 37)


    def test_unordered_list(self):
        '''Unordered lists unit tests'''
        unordered_list_1 = [1, 3, 2, 4]
        unordered_list_2 = [-50, 20, 425, 37]

        self.assertEqual(max_integer(unordered_list_1), 4)
        self.assertEqual(max_integer(unordered_list_2), 425)

        self.assertNotEqual(max_integer(unordered_list_1), 1)
        self.assertNotEqual(max_integer(unordered_list_1), 3)
        self.assertNotEqual(max_integer(unordered_list_1), 2)

        self.assertNotEqual(max_integer(unordered_list_2), -50)
        self.assertNotEqual(max_integer(unordered_list_2), 20)
        self.assertNotEqual(max_integer(unordered_list_2), 37)


    def test_other_list(self):
        '''
        Other lists unit tests
        (float, negative, None, inf, NaN, empty, missing arg)
        '''
        other_list_1 = [242.124, -611.661, 166, -805]
        other_list_2 = [242.124, 611.661, -166, -805]
        other_list_3 = [-242.124, -611.661, 166, -805]
        other_list_4 = [-242.124, -611.661, -166, -805]

        self.assertEqual(max_integer(other_list_1), 242.124)
        self.assertEqual(max_integer(other_list_2), 611.661)
        self.assertEqual(max_integer(other_list_3), 166)
        self.assertEqual(max_integer(other_list_4), -166)

        self.assertNotEqual(max_integer(other_list_1), -611.661)
        self.assertNotEqual(max_integer(other_list_1), 166)
        self.assertNotEqual(max_integer(other_list_1), -805)
        
        self.assertNotEqual(max_integer(other_list_2), 242.124)
        self.assertNotEqual(max_integer(other_list_2), -166)
        self.assertNotEqual(max_integer(other_list_2), -805)

        self.assertNotEqual(max_integer(other_list_3), -242.124)
        self.assertNotEqual(max_integer(other_list_3), -611.661)
        self.assertNotEqual(max_integer(other_list_3), -805)
        
        self.assertNotEqual(max_integer(other_list_4), -242.124)
        self.assertNotEqual(max_integer(other_list_4), -611.661)
        self.assertNotEqual(max_integer(other_list_4), -805)

        self.assertEqual(max_integer([None]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([98]), 98)


if __name__ == '__main__':
    unittest.main()
