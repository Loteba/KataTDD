
class Conjunto:
    def __init__(self, datos, pesos):
        self.__datos = datos
        self.__pesos = pesos

    def promedio(self):
        if len(self.__datos) == 0 or len(self.__pesos) == 0 or len(self.__datos) != len(self.__pesos):
            return None
        else:
            total_peso = sum(self.__pesos)
            promedio_ponderado = sum(d * p for d, p in zip(self.__datos, self.__pesos)) / total_peso
            return promedio_ponderado
