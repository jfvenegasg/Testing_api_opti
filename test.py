import unittest
import pickle
import pandas as pd
import numpy as np
import random as rd
from pyomo.environ import *

from modelos_optimizacion import mochila


class TestSum(unittest.TestCase):
    def test_restriccion_1(self):
        """
        Se realiza el test para el valor de la restriccion 1 con un conjunto aleatorio de pesos pequeños
        """
        min=1
        max=100

        data_1=[rd.randint(min,max),rd.randint(min,max),rd.randint(min,max),rd.randint(min,max),rd.randint(min,max),rd.randint(min,max)]
        
        resultado_1=mochila(data_1)
        
        self.assertLessEqual(resultado_1['res'],data_1[5])

    def test_restriccion_2(self):
        """
        Se realiza el test para el valor de la restriccion 1 con un conjunto aleatorio de pesos medianos
        """
        min=100
        max=1000

        data_2=[rd.randint(min,max),rd.randint(min,max),rd.randint(min,max),rd.randint(min,max),rd.randint(min,max),rd.randint(min,max)]

        
        resultado_2=mochila(data_2)

        self.assertLessEqual(resultado_2['res'],data_2[5])

    def test_variables_binarias(self):
        """
        Se realiza el test para la suma de las variables binarias
        """

        min=1
        max=100000
        data_3=[rd.randint(min,max),rd.randint(min,max),rd.randint(min,max),rd.randint(min,max),rd.randint(min,max),rd.randint(min,max)]

        
        resultado_3=mochila(data_3)

        self.assertGreaterEqual(resultado_3['x1']+resultado_3['x2']+resultado_3['x3']+resultado_3['x4']+resultado_3['x5'],0)

    
if __name__ == '__main__':
    unittest.main()