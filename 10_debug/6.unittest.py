######################################UnitTest#####################################
# What's the point of passing unit tests? If we abs() modify the function code, we only need to run the unit test again. 
# If it passes, it means that our modification will not abs() affect the original behavior of the function. 
# If the test fails, it means that our modification is inconsistent with the original behavior. 
# Either modify the code or modify the tests.
class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

# The biggest benefit of this test-driven development model is to ensure that the behavior of a program module 
# conforms to the test cases we design. When modified in the future, there is a high degree of assurance that 
# the module behavior will still be correct.
import unittest

class TestDict(unittest.TestCase):

    def setUp(self):
        print('...setUp...')

    def tearDown(self):
        print('...tearDown...')

    def test_init(self):
        d = Dict(a=1, b='test')
        print("test_init")
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        print("test_key")
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        print("test_attr")
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        print("test_keyerror")
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        print("test_attrerror")
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == '__main__':
    unittest.main()

# The outputs are as the follows:

# $ python 6.unittest.py 
# ...setUp...
# test_attr
# ...tearDown...
# ....setUp...
# test_attrerror
# ...tearDown...
# ....setUp...
# test_init
# ...tearDown...
# ....setUp...
# test_key
# ...tearDown...
# ....setUp...
# test_keyerror
# ...tearDown...
# .
# ----------------------------------------------------------------------
# Ran 5 tests in 0.004s

# OK
