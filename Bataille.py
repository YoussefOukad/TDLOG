from classes import *


Arme1 = Weapon(40, 30, 0)
Arme2 = Weapon(50, 40, 1)
Arme3 = Weapon(15, 20, 2)
"simulation d'une battaille entre 2 joueurs "

Batail = espace()
'Construction des vaisseaux'
Vaisseau2 = Vessel((0, 0, 0), 1, Arme3, 1)
Vaisseau3 = Vessel((1, 0, 0), 10, Arme1, 2)
Vaisseau4 = Vessel((1, 1, -1), 7, Arme3, 3)
Vaisseau5 = Vessel((1, 1, 0), 1, Arme1, 4)
Vaisseau6 = Vessel((1, 2, 0), 1, Arme2, 2)
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
    if len(VaisseaudetruitJ2) == len(L2) and len(VaisseaudetruitJ1) != len(L1) :
        return print("le joueur 1 a gagné")
    if len(VaisseaudetruitJ1) == len(L1) and len(VaisseaudetruitJ2) == len(L2):
        return print("Match nul")

#pour visualiser la validite de la methode, on peut intervertir le role de L1 et L2 ci-dessous pour voir le joueur gagneur se changer:
simu_bataille(L1,L2)
