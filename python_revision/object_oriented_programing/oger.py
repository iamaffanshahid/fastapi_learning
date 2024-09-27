# -*- coding: utf-8 -*-
import random as choic

from evil import Evil

class Oger(Evil):
    def __init__(self, damage, health):        
        super().__init__(type_of_evil = "oger", attack_damage = damage, health_points = health)
        
        
    def talk(self):
        print("oger is smashimg hands around")
        
    def special_attack(self):
        did_special_attack_work = choic.random() < 0.20
        if  did_special_attack_work:
            self.attack_damage += 4
            print("oger attack damage increased by 4!")    
