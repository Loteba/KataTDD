import unittest
import src.logica
from src.logica.Conjunto import Conjunto

class TestConjunto( unittest.TestCase ):
    def test_conjunto_vacio_retornaNone( self ):
        conjunto=Conjunto([])
        self.assertIsNone(conjunto.promedio())

    def test_conjunto_unElemento_retornaValorUnicoElemento( self ):
        conjunto=Conjunto([5])
        self.assertEqual(5,conjunto.promedio())


if __name__== "__main__"
    if len(self.__conjunto) == 1:
        return (self.__conjunto[0])
    else:
        return None
