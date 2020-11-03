import unittest

from findfromfile import list_files, search_text, user_input

class TestTextSearch(unittest.TestCase):

    def test_paths(self):
        # self.assertRaises(TypeError, search_text, 'random', 'asd') # Test a non-existing path
        self.assertEqual(search_text('text', 'invalid path'), 'TypeError') # Test a non-existing path
        self.assertEqual(search_text('lorem', 'test\\'), [5, 1, 1]) # Test giving backslash in path
        self.assertEqual(search_text('lorem', 'test'), [5, 1, 1]) # Test giving directory without (back)slash

    def test_hits(self):
        self.assertEqual(search_text('lorem', 'test/'), [5, 1, 1]) # Test lower case search match in one file
        self.assertEqual(search_text('Lorem', 'test/'), [3, 2, 1]) # Test case sensitive search match with hits inside multiple files
        self.assertListEqual(search_text('', 'test/'), [3036, 2, 1])  # Test empty string search match (results in total number of characters including spaces and line breaks)
        self.assertListEqual(search_text(' ', 'test/'), [430, 2, 1])  # Test space search match
        self.assertListEqual(search_text('sadjhaskjfhfkjhaskhf', 'test/'), [0, 0, 1])  # Test search resultin in zero hits
    
    def test_unicode(self): # Test searching unicode characters
        self.assertEqual(search_text('“', 'test/'), [2, 1, 1])
        self.assertEqual(search_text('”', 'test/'), [1, 1, 1])

    def test_nontextfile(self): # Test searching in a directory containing a non-text file. 
        # self.assertRaises(UnicodeDecodeError, search_text, 'random', 'test/nontext/')
        # self.assertEqual(search_text('random', 'test'), 'UnicodeDecodeError')
        self.assertEqual(search_text('random string', 'test/'), [0, 0, 1])


if __name__ == '__main__':
    unittest.main()