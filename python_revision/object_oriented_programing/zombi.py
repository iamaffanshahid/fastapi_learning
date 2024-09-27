# -*- coding: utf-8 -*-

import random as choic


from evil import Evil

class Zombi(Evil):
    
    def __init__(self, damage, health):        
        super().__init__(type_of_evil = "zombi", attack_damage = damage, health_points = health)
        
    def talk(self):
        print("**Grambling.....**")
              
    def spread_disease(self):
        print("zombi is spreading disease")
        
        
    def special_attack(self):
        did_special_attack_work = choic.random() < 0.50
        if  did_special_attack_work:
            self.health_points += 2
            print("zombi regnerated 2 HP!")