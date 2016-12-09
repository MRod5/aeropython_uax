# -*- coding: utf-8 -*-
"""

Ecuación de Estado para gas ideal en forma másica.
--------------------------------------------------

"""


def solve(R_g, P=False, V=False, m=False, T=False):
    """
    Dada la constante del gas (R_g) se obtiene la solución de la Ecuación de
    Estado para Gas Ideal (p·V=m·R_g·T).

    Se obtiene la propiedad termodinámica que se deje a False en la llamada a 
    la función. Por ejemplo si se quiere resolver la presión que tiene un 
    sistema de 50g de aire, a 288K en un volumen de 0.001 m³:
    
        P = eq_state.solve(R_g=R_a, V=1e-3, m=0.05, T=288)

    """

    if P is False:
        #Obtención de la presión
        P_=solve_P(V, m, T, R_g)
        return P_
    elif V is False:
        #Obtención del volumen
        V_=solve_V(P, m, T, R_g)
        return V_
    elif m is False:
        #Obtención de la masa
        m_ = solve_m(P, V, T, R_g)
        return m_
    elif T is False:
        #Obtención de la temperatura
        T_ = solve_T(P, V, m, R_g)
        return T_


def solve_P(V, T, m, R_g):
    """
    Resuelve la presión dadas las demás propiedades de la ecuación de estado
    """
    return m*R_g*T/V

def solve_V(P, m, T, R_g):
    """
    Resuelve el volumen dadas las demás propiedades de la ecuación de estado
    """
    return m*R_g*T/P
    
def solve_m(P, V, T, R_g):
    """
    Resuelve la masa dadas las demás propiedades de la ecuación de estado
    """    
    return P*V/R_g/T

def solve_T(P, V, m, R_g):
    """
    Resuelve la temperatura dadas las demás propiedades de la ecuación de estado
    """    
    return P*V/m/R_g

