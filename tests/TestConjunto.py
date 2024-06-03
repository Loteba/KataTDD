import unittest
import sys
import os

# Añadir el directorio base del proyecto al sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.logica.Conjunto import Conjunto

class TestConjunto(unittest.TestCase):
    def test_conjunto_vacio_retornaNone(self):
        conjunto = Conjunto([], [])
        self.assertIsNone(conjunto.promedio())

    def test_conjunto_unElemento_retornaValorUnicoElemento(self):
        conjunto = Conjunto([5], [1])
        self.assertEqual(5, conjunto.promedio())

    def test_conjunto_dosElementos_retornaPromedioElementos(self):
        conjunto = Conjunto([5, 7], [1, 1])
        self.assertEqual(6, conjunto.promedio())

    def test_conjunto_nElementos_retornaPromedioNElementos(self):
        conjunto = Conjunto([2, 4, 8, 9, 10, 15], [1, 1, 1, 1, 1, 1])
        self.assertEqual((2 + 4 + 8 + 9 + 10 + 15) / 6, conjunto.promedio())

    def test_conjunto_datosPesosEjemplo0(self):
        conjunto = Conjunto([10, 12, 14], [3, 4, 2])
        self.assertAlmostEqual(11.78, conjunto.promedio(), places=2)

    def test_conjunto_datosPesosEjemplo1(self):
        conjunto = Conjunto([15, 15, 17], [3, 4, 2])
        self.assertAlmostEqual(15.44, conjunto.promedio(), places=2)

if __name__ == "__main__":
    unittest.main()
