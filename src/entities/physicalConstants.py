import numpy as np

# Physical constants
pi = np.pi
angstron = 1e-10
hBar =  6.626086e-34/(2 * pi)
eV = 1.60217646e-19

# Electron constants
electronMass = 9.11e-31
electronMassBarrier = 0.0665 * electronMass

# Hole constant
holeMass = 2.18 * electronMass
holeMassBarrier = 0.33 * electronMass


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
    
        