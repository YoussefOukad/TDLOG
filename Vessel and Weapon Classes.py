import math
from typing import List


# creation de la classe ARME:
class Weapon:
    # type d'Arme existants:
    Weapon_type = ['lance-missiles antisurface', 'Lance-missiles anti-air', 'Lance-torpilles']

    # initation et definition de la classe:
    def __init__(self, ammunitions, range, i):
        self.ammunitions = ammunitions
        self.range = range
        self.weapontype = Weapon.Weapon_type[i]

    def fire_at(self, x, y, z):
        if self.ammunitions == 0:
            print('NoAmmunitionError')
        if self.ammunitions != 0 and math.sqrt(x ** 2 + y ** 2 + z ** 2) > self.range:
            print('OutOfRangeError')
        if self.ammunitions != 0 and self.weapontype == 'lance-missiles antisurface' and z != 0:
            print('OutOfRangeError')
        if self.ammunitions != 0 and self.weapontype == 'Lance-missiles anti-air' and z <= 0:
            print('OutOfRangeError')
        if self.ammunitions != 0 and self.weapontype == 'Lance-torpilles' and z > 0:
            print('OutOfRangeError')
        else:
            self.ammunitions -= 1


Arme1 = Weapon(40, 30, 0)
Arme2 = Weapon(50, 40, 1)
Arme3 = Weapon(15, 20, 2)


class Vessel:
    # type de vaisseaux existants:
    Vessel_type: list[str] = ['Cruiser', 'Submarine', 'Fregate', 'Destroyer', 'Aircraft']

    # initation et definition de la classe:
    def __init__(self, coordinates:tuple, max_hits: int, Weapon: object, j: int):
        self.coordinates = coordinates
        self.max_hits = max_hits
        self.weapon = Weapon
        self.vesseltype = Vessel.Vessel_type[j]

    def go_to(self, x, y, z):
        if self.max_hits == 0:
            return 'DestroyedError'
        elif self.vesseltype == 'Cruiser' and z != 0:
            return 'OutOfRangeError'
        elif self.vesseltype == 'Submarine' and z != 0 and z != -1:
            return 'OutOfRangeError'
        elif self.vesseltype == 'Fregate' and z != 0:
            return 'OutOfRangeError'
        elif self.vesseltype == 'Destroyer' and z != 0:
            return 'OutOfRangeError'
        elif self.vesseltype == 'Aircraft' and z != 1:
            return 'OutOfRangeError'
        else:
            self.coordinates = (x,y,z)
            print("le vaisseau {} est dans le point {},{},{}".format(self.vesseltype, x, y, z))

    def get_coordinates(self):
        return self.coordinates

    def fire_at(self, x, y, z):
        if self.max_hits == 0:
            return 'DestroyedError'
        else:
            return self.weapon.fire_at(x, y, z)




O = (0, 0, 0)
Vaisseau1 = Vessel(O, 6, Arme2, 0)
Vaisseau2 = Vessel((0, 0, 0), 2, Arme3, 1)
Vaisseau3 = Vessel((0, 0, 0), 5, Arme1, 2)
Vaisseau4 = Vessel((0, 0, 0), 7, Arme3, 3)
Vaisseau5 = Vessel((0, 0, 0), 1, Arme1, 4)

#trying different technics

print(Vaisseau4.vesseltype=='Destroyer')
print(Vaisseau4.go_to(1,10,1))
print(Vaisseau4.get_coordinates())
