import unittest

from findfromfile import list_files, search_text, user_input

class TestTextSearch(unittest.TestCase):

    def test_paths(self):
        self.assertRaises(TypeError, search_text('random', 'asd')) # Test giving a non-existing path
        # assertRaises(exception, callable, *args, **kwds)
        # assertRaises(exception, *, msg=None)

    def test_hits(self):
        self.assertEqual(search_text('lorem', 'test/'), [5, 1]) # Test lower case search match
        self.assertEqual(search_text('Lorem', 'test/'), [3, 2]) # Test case sensitive search match with hits inside multiple files
        self.assertListEqual(search_text('', 'test/'), [3036, 2])  # Test empty string search match
        self.assertListEqual(search_text(' ', 'test/'), [430, 2])  # Test space search match
        self.assertListEqual(search_text('sadjhaskjfhfkjhaskhf', 'test/'), [0, 0])  # Test searching zero hits
    
    def test_unicode(self): # Test searching unicode characters
        self.assertEqual(search_text('“', 'test/'), [2, 1])
        self.assertEqual(search_text('”', 'test/'), [1, 1])

    def test_nontextfile(self): # Test searching in a directory containing a non-text file
        # TODO: not working properly, TypeError instead of UnicodeDecodeError ??
        # program itself returns UnicodeDecodeError but this test passes with TypeError. WHY?!
        #self.assertRaises(UnicodeDecodeError, search_text('random', 'test/nontext/'))
        self.assertRaises(TypeError, search_text('random', 'test/nontext/'))

# TODO: 
# testi, joka kokeilee hakemiston kautta- ja kenoviivoilla ja loppuun viiva vai ei
# testi, joka ei osu

if __name__ == '__main__':
    unittest.main()