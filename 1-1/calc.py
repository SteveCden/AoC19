import math

fuelMass = 0

with open('input.txt') as openFile:
    for line in openFile:
        fuelMass += math.floor(int(line) / 3) - 2
print(fuelMass)
