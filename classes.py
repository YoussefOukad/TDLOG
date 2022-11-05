import math
import numpy as np
import random
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

#les armes demandés:

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



#les vaisseaux demandés:
O = (0, 0, 0)
Vessel1 = Vessel(O, 6, Arme2, 0)
Vessel2 = Vessel((0, 0, 0), 2, Arme3, 1)
Vessel3 = Vessel((0, 0, 0), 5, Arme1, 2)
Vessel4 = Vessel((0, 0, 0), 7, Arme3, 3)
Vessel5 = Vessel((0, 0, 0), 1, Arme1, 4)

#trying different technics
"""
print(Vaisseau4.vesseltype=='Destroyer')
print(Vaisseau4.go_to(1,10,1))
print(Vaisseau4.get_coordinates())

"""

class espace():

    def __init__(self):
        self.shape = np.empty((3, 101, 101), dtype='object')  # on represente un espace par une matrice de dimension 3
        self.vaisseaux = []

    def ajouter(self, numJ, vaisseau: Vessel):
        max = 0
        for v in self.vaisseaux:
            max = + v[0].max_hits
        if self.recevoir(vaisseau):
            print("Cette position est deja occupée, veuillez choisir une autre position")
        elif max > 22:
            print("seuil max_hits depassé")
        else:
            (x, y, z) = vaisseau.coordinates
            if numJ == 1:
                self.vaisseaux.append((vaisseau, 1))  # (vaisseau,1) cad le vaisseau du joueur 1
                self.shape[z + 1, x, y] = (vaisseau, 1)
            else:
                self.vaisseaux.append((vaisseau, 2))
                self.shape[z + 1, x, y] = (vaisseau, 2)

    def recevoir(self, vaisseau):
        for i in range(len(self.vaisseaux)):
            v = self.vaisseaux[i][0]  # recuperer le vaisseau de la la liste des vaisseaux
            if v.get_coordinates() == vaisseau.coordinates:
                return True
            else:
                return False




"simulation d'une battaille entre 2 joueurs "

Batail = espace()
'Construction des vaisseaux'
Vaisseau2 = Vessel((0, 0, 0), 1, Arme1, 1)
Vaisseau3 = Vessel((1, 0, 0), 1, Arme1, 1)
Vaisseau4 = Vessel((1, 1, -1), 1, Arme1, 1)
Vaisseau5 = Vessel((1, 1, 0), 1, Arme1, 1)
Vaisseau6 = Vessel((1, 2, 0), 1, Arme1, 1)
Vaisseau7 = Vessel((2, 1, 0), 1, Arme1, 1)

"Ajout des vaisseaux à l'espace du joueur 1"
espace.ajouter(Batail, 1, Vaisseau2)
espace.ajouter(Batail, 1, Vaisseau6)
espace.ajouter(Batail, 1, Vaisseau4)
L1=[Vaisseau2,Vaisseau6,Vaisseau4] #les vaisseaux du Joueur 1
"Ajout des vaisseaux à l'espace du joueur 2"

espace.ajouter(Batail, 2, Vaisseau5)
espace.ajouter(Batail, 2, Vaisseau3)
espace.ajouter(Batail, 2, Vaisseau7)
L2=[Vaisseau5,Vaisseau3,Vaisseau7] # les vaisseaux du Joueur 2

'Simulation de la bataille'
# Un loop d'echange de coup entre les deux joueurs.
VaisseaudetruitJ1 = set()
VaisseaudetruitJ2 = set()


def simu_bataille(L1,L2):
    for i in range(len(L1)):
        for j in range(len(L2)):
            # condition d'echange de coups entre les joueurs, que les deux joueurs aient au moins avec quoi attaquer.
            while L1[i].max_hits >0 and L1[i].weapon.ammunitions >0 and L2[j].max_hits > 0 and L2[j].weapon.ammunitions >0:
                # On cherche un target à attaquer
                target1 = 0
                target2 = 0
                # Une condition que le vaisseau attaqué doit avoir un hits_max>0 sinon on cherche un autre vaisseau à viser.

                while L1[i].fire_at(L2[target1].get_coordinates()[0],L2[target1].get_coordinates()[1],L2[target1].get_coordinates()[2]) == 'OutOfRangeError' and target1<len(L2):

                    target1 +=1

                # Si la condition est verfiée on lance l'attaque sur le joueur 2
                if L1[i].fire_at(L2[target1].get_coordinates()[0],L2[target1].get_coordinates()[1],L2[target1].get_coordinates()[2]) != 'OutOfRangeError'and L2[target1].max_hits >0:
                    L2[target1].max_hits -=1

                #idem
                while L2[j].fire_at(L1[target2].get_coordinates()[0],L1[target2].get_coordinates()[1],L1[target2].get_coordinates()[2])=='OutOfRangeError' and target2<len(L1):
                    target2 +=1

                if L2[j].fire_at(L1[target2].get_coordinates()[0],L1[target2].get_coordinates()[1],L1[target2].get_coordinates()[2]) != 'OutOfRangeError' and L1[target2].max_hits >0:
                    L1[target2].max_hits -= 1

            if L1[i].max_hits == 0 or L1[i].weapon.ammunitions == 0:
                VaisseaudetruitJ1.add(i)
            if L2[j].max_hits == 0 or L2[j].weapon.ammunitions == 0:
                VaisseaudetruitJ2.add(j)
    if len(VaisseaudetruitJ1) == len(L1) and len(VaisseaudetruitJ2) != len(L2) :
        return print("le joueur 2 a gagné")
    if len(VaisseaudetruitJ2) == len(L1) and len(VaisseaudetruitJ1) != len(L2) :
        return print("le joueur 1 a gagné")
    if len(VaisseaudetruitJ1) == len(L1) and len(VaisseaudetruitJ2) == len(L2):
        return print("Match nul")


simu_bataille(L1,L2)