import unittest
import pickle
import pandas as pd
import numpy as np
from pyomo.environ import *

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        #data = [1, 2, 3]
        #result = sum(data)
        #self.assertEqual(result, 7)

        #data = pd.DataFrame({'Peso Objeto 1': [objeto1_peso],'Peso Objeto 2': [objeto2_peso], 'Peso Objeto 3': [objeto3_peso], 
        #                 'Peso Objeto 4': [objeto4_peso],'Peso Objeto 5': [objeto5_peso],'Peso Total': [peso_total]})
        modelo = pickle.load(open("modelo_optimizacion/modelo.pkl", "rb"))

        data=pd.DataFrame([25,27,23,26,28,60])
        modelo.restriccion = Constraint(expr=data.iloc[0]*modelo.x1 + data.iloc[1]*modelo.x2+data.iloc[2]*modelo.x3+data.iloc[3]*modelo.x4+data.iloc[4]*modelo.x5 <= data.iloc[5])


        glpsol_path = 'glpk-4.65/w64/glpsol.exe'
        #solver.set_executable(executable='app/glpk-4.65/w64/glpsol.exe', validate=False)
        solver = SolverFactory('glpk', executable=glpsol_path)  

        resultado = solver.solve(modelo)

        self.assertLessEqual(value(modelo.x1)*data.iloc[0]+value(modelo.x2)*data.iloc[1]+value(modelo.x3)*data.iloc[2]+
            value(modelo.x4)*data.iloc[3]+value(modelo.x5)*data.iloc[4],data[5])

if __name__ == '__main__':
    unittest.main()