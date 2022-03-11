import unittest
from app.models import Quotes



class QuotesTest(unittest.TestCase):

    def setUp(self):
        self.new_quote = Quotes("melody",1234,"pprogramming is all about practice")
    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quotes))

