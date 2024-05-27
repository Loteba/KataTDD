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

    def test_conjunto_dosElementos_retornaPromedioElementos( self ):
        conjunto=Conjunto([5,7])
        self.assertEqual(6,conjunto.promedio())



if __name__== "__main__"
    def promedio( self ):
        if len(self.__conjunto) == 1:
            return (self.__conjunto[0])
        elif len(self.__conjunto) == 2:
            return (self.__conjunto[0]+self.__conjunto[1])/2
        else:
            return None


