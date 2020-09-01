from preprocess import execute
import unittest

class PreprocessTest(unittest.TestCase):
    def test_preprocess(self):
        # Test train and val data path string value
        self.assertRaises(TypeError, execute, 2)
        self.assertRaises(TypeError, execute, True)
        self.assertRaises(TypeError, execute, ['s'])

if __name__ == "__main__":
    unittest.main()