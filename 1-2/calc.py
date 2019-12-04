import math

mass = 0
tempMass = 0
fuelMass = 0

with open('input.txt') as openFile:
    for line in openFile:
        fuelMass = math.floor(int(line) / 3) - 2
        mass += fuelMass
        while fuelMass > 0:
            fuelMass = math.floor(fuelMass/3) - 2
            if fuelMass > 0:
                mass += fuelMass
print(mass)
