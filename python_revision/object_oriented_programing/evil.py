# -*- coding: utf-8 -*-

class Evil():
 
    
    def __init__(self,type_of_evil, attack_damage, health_points ):
        self.__type_of_evil = type_of_evil
        self.attack_damage = attack_damage
        self.health_points = health_points

    def talk(self):
        print(f"I am {self.__type_of_evil} be ready to fight.")
        
        
    def walk(self):
        print(f"{self.__type_of_evil} come closer to you.")
        
        
    def attack(self):
        print(f"{self.__type_of_evil} attack for {self.attack_damage} attack damage")
        
        
    def get_type_of_evil(self):
        return self.__type_of_evil
    
    def special_attack(self):
        print("evil has no special attack")