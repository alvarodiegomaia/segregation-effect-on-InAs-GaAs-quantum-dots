import numpy as np
from physicalConstants import pi, angstron, hBar, eV
from physicalConstants import  electronMass, electronMassBarrier
from physicalConstants import  holeMass, holeMassBarrier


def KroneckerDelta(i, j):
    """
    Kronecker delta

    Args:
        i (int): i index
        j (int): j index
    """
    return (i == j).astype(int)


def Mass1(x):
    """
    Parallel effective mass in unities of m0.

    Args:
        x (float): InAs Concentration
    """
    return (0.067 - 0.0131318 * x - 0.015862 * x ** 2) * electronMass


def Mass2(x):
    """
    Perpendicular effective mass in unities of m0.

    Args:
        x (float): InAs Concentration
    """
    return (0.067 - 0.000173691 * x - 0.0246154 * x ** 2) * electronMass


def A_InGaAs(T, x):
    """
    Net parameter of In_XGa_(1-x)As in meters.

    Args:
        T (float): Temperature in K
        x (float): InAs Concentration
    """
    return (5.65325 + 3.88E-5 *(T - 300.0) + (0.40505 - 1.14E-5 * (T - 300.0)) * x) * angstron


def DivQD(T, x, hQD):
    """
    returns the number of discs in the division of the QD

    Args:
        T (float): Temperature in K
        x (float): Concentration of InAs
        hQD (float): Height of the QD
    """
    
    return 1 + np.round(hQD / (A_InGaAs(T, x) / 2))


def DivWL(T, x, hWL):
    """
    returns the number of discs in the division of the WL

    Args:
        T (float): Temperature in K
        x (float): Concentration of InAs
        hWL (float): Thickness of the WL
    """
    
    return 1 + np.round(hWL / (A_InGaAs(T, x) / 2))


def ThickQD(T, x, hQD):
    """
    returns the thickness of discs in the division of the QD

    Args:
        T (float): Temperature in K
        x (float): Concentration of InAs
        hQD (float): Height of the QD
    """
    
    return hQD/DivQD(T, x, hQD)


def ThickWL(T, x, hWL):
    """
    returns the thickness of discs in the division of the WL

    Args:
        T (float): Temperature in K
        x (float): Concentration of InAs
        hWL (float): Height of the QD
    """
    
    return hWL/DivQD(T, x, hWL)


def f(l, m, n, l1, m1, n1):
    """
    Returns the solution of the free particle integral
    inside a cilindre

    Args:
        l (int): Quantum number l
        m (int): Quantum number m
        n (int): Quantum number n
        l1 (int): Quantum number l
        m1 (int): Quantum number m
        n1 (int): Quantum number n
    """
    
    return (((hBar ** 2) / (2 * Mass1(0.0))) * ((l * pi / H_C) * (l * pi / H_C) + k(m,n) ** 2)) * KroneckerDelta(l, l1) * KroneckerDelta(m, m1) * KroneckerDelta(n, n1)



if __name__ == '__main__':
    print(f'')
    print(f'Physical constants')
    print(f'pi: {pi}')
    print(f'angstron: {angstron}')
    print(f'hBar: {hBar}')
    print(f'eV: {eV}')
    print(f'')
    print(f'Electron constants')
    print(f'Electron mass: {electronMass}')
    print(f'Electron mass in barrier: {electronMassBarrier}')
    print(f'')
    print(f'Hole constants')
    print(f'Hole mass: {holeMass}')
    print(f'Hole mass in barrier: {holeMassBarrier}')