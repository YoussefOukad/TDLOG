import unittest 
from math import*
from classes import * # code source
class MyTests(unittest.TestCase):
    
    def test_fire_at(self,weapontype, ammunition,z, range):
        if self.ammunition ==0:
            self.assertEqual(fire_at(x,y,z), 'NoAmmunitionsError')
        elif math.sqrt(x*2+y2+z*2)>self.range:
            self.assertEqual(fire_at(x,y,z),"OutOfRangeError")
        elif self.z!=0 and self.weapontype == 'lance-missiles antisurface':
            self.assertEqual(fire_at(x,y,z),"OutOfRangeError")
        elif self.z>0 and self.weapontype == 'Lance-torpilles':
            self.assertEqual(fire_at(x,y,z),"OutOfRangeError")
        elif self.z<=0 and self.weapontype == 'Lance-missiles anti-air':
            self.assertEqual(fire_at(x,y,z),"OutOfRangeError")
        else :
            self.ammunition == self.ammunition -1
            self.assertEqual(fire_at(x,y,z), ammunition)
            
    def test_go_to(self,vaisseau,z):            
        elif self.z!=0 and self.vaisseau == 'Cruiser' or self.vaisseau == 'Fregate' or self.vaisseau == 'Destroyer':
            self.assertEqual(go_to(x,y,z),"OutOfRangeError")
        elif self.z!=1 and self.vaisseau == 'Aircraft':
            self.assertEqual(go_to(x,y,z),"OutOfRangeError")
        elif self.z!=0 and self.z!=-1 and self.vaisseau == 'Submarine':
            self.assertEqual(go_to(x,y,z),"OutOfRangeError")
            
    def test_fire_at2(self, z, max_hits, range):
        if self.max_hits == 0:
            self.assertEqual(fire_at(x,y,z), 'DestroyedError')
        elif math.sqrt(x*2+y2+z*2)>self.range:
            self.assertEqual(fire_at(x,y,z),"OutOfRangeError")
        else :
            self.ammunition== self.amunition-1
            self.assertEqual(fire_at(x,y,z), ammunition)