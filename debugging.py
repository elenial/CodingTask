from unittest import TestCase

def increment_dictionary_values(d, i):
       incremented_dictionary = {}
       for k, v in d.items():
              incremented_dictionary[k] = v + i
       return incremented_dictionary

class TestIncrementDictionaryValues(TestCase):
       def test_increment_dictionary_values(self):
              d = {'a':1}
              dd = increment_dictionary_values(d, 1)
              ddd = increment_dictionary_values(d, -1)
              self.assertEqual(dd['a'], 2)
              self.assertEqual(ddd['a'], 0)