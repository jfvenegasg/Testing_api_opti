import pandas as pd
import numpy as np
from pyomo.environ import *


def mochila(args):
        modelo=ConcreteModel()

        modelo.x1=Var(within=Binary,bounds=(0,1))
        modelo.x2=Var(within=Binary,bounds=(0,1))
        modelo.x3=Var(within=Binary,bounds=(0,1))
        modelo.x4=Var(within=Binary,bounds=(0,1))
        modelo.x5=Var(within=Binary,bounds=(0,1))

        v1=0.2
        v2=0.2
        v3=0.2
        v4=0.2
        v5=0.2
        
        data = pd.DataFrame({'Peso Objeto 1': [args[0]],'Peso Objeto 2': [args[1]], 'Peso Objeto 3': [args[2]],'Peso Objeto 4': [args[3]],'Peso Objeto 5': [args[4]],'Peso Total': [args[5]]})

        modelo.objetivo = Objective(expr=v1*modelo.x1+v2*modelo.x2+v3*modelo.x3+v4*modelo.x4+v5*modelo.x5, sense=maximize)
        
        modelo.restriccion = Constraint(expr=data.loc[0, 'Peso Objeto 1']*modelo.x1 + data.loc[0, 'Peso Objeto 2']*modelo.x2 + data.loc[0, 'Peso Objeto 3']*modelo.x3 + data.loc[0, 'Peso Objeto 4']*modelo.x4 + data.loc[0, 'Peso Objeto 5']*modelo.x5 <= data.loc[0, 'Peso Total'])

        glpsol_path = 'glpk-4.65\w64\glpsol.exe'

        solver = SolverFactory('glpk', executable=glpsol_path)  

        solver.solve(modelo)

        peso_mochila = value(modelo.x1)*data.loc[0, 'Peso Objeto 1'] + value(modelo.x2)*data.loc[0, 'Peso Objeto 2'] + value(modelo.x3)*data.loc[0, 'Peso Objeto 3'] + value(modelo.x4)*data.loc[0, 'Peso Objeto 4'] + value(modelo.x5)*data.loc[0, 'Peso Objeto 5']

        resultado = {
        'res': peso_mochila,
        'x1': value(modelo.x1),
        'x2': value(modelo.x2),
        'x3': value(modelo.x3),
        'x4': value(modelo.x4),
        'x5': value(modelo.x5)
        }
       
        return resultado