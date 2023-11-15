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
        
        res_1=mochila(data_1)
        
        self.assertLessEqual(res_1,data_1[5])

    def test_restriccion_2(self):
        """
        Se realiza el test para el valor de la restriccion 1 con un conjunto aleatorio de pesos medianos
        """
        min=100
        max=1000

        data_2=[rd.randint(min,max),rd.randint(min,max),rd.randint(min,max),rd.randint(min,max),rd.randint(min,max),rd.randint(min,max)]

        
        res_2=mochila(data_2)

        self.assertLessEqual(res_2,data_2[5])

    def test_restriccion_3(self):
        """
        Se realiza el test para el valor de la restriccion 1 con un conjunto aleatorio de pesos grandes
        """

        min=100000
        max=10000000
        data_3=[rd.randint(min,max),rd.randint(min,max),rd.randint(min,max),rd.randint(min,max),rd.randint(min,max),rd.randint(min,max)]

        
        res_3=mochila(data_3)

        self.assertLessEqual(res_3,data_3[5])
        
if __name__ == '__main__':
    unittest.main()