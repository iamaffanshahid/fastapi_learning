# -*- coding: utf-8 -*-
import evil as Evil  
from oger import Oger
from zombi import Zombi

def battle(e1: Evil, e2: Evil):
    
    e1.talk()
    e2.talk()



    while e1.health_points > 0 and e2.health_points > 0:
      
      print("---------")  
      e1.special_attack()
      e2.special_attack()
      print(f"{e1.get_type_of_evil()}:{e1.health_points} HP left!")
      print(f"{e2.get_type_of_evil()}:{e2.health_points} HP left!")
      e2.attack()
      e1.health_points -= e2.attack_damage
      e1.attack()
      e2.health_points -= e1.attack_damage
      
    if e1.health_points > 0:
          print("Evil 1 wins")
    else:
          print("Evil 2 wins")
print("----------")

zombi = Zombi(5, 10)
oger = Oger(5, 10)


battle(zombi, oger)





