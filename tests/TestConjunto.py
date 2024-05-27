import unittest
import src.logica
from src.logica.Conjunto import Conjunto

class TestConjunto( unittest.TestCase ):

    def test_conjunto_vacio_retornaNOne(self):
        conjunto = Conjunto([])
        self.assertIsNone(conjunto.promedio())

if __name__== "__main__"
