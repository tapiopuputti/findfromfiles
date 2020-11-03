import unittest

from findfromfile import list_files, search_text, user_input

class TestTextSearch(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(clas):
        print('tearDownClass')

    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')
        
# TODO: 
# testi, joka kokeilee hakemiston kautta- ja kenoviivoilla ja loppuun viiva vai ei
# testi, joka etsii unicodea
# testi, joka kokeilee yleisellä syötteellä (osuu)
# testi, joka ei osu
# testi, että ei tule exceptejä