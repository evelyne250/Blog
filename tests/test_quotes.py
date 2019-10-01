import unittest
from app.models import Quotes

class testQuotes(unittest.TestCase):
    def setUp(self):
        self.new_quote = Quotes('evelyne','If Java had true garbage collection, most programs would delete themselves upon execution.','http://quotes.stormconsultancy.co.uk/quotes/31')

    def test_variables(self):
        self.assertTrue(isinstance(self.new_quote,Quotes))