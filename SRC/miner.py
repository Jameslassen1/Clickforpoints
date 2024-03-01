import pygame
class Miner:
    def __init__(self,name,cost,power):
        self.name = name
        self.cost = cost
        self.power = power
    def __str__(self):
     return f"Miner(name ='{self.name}', cost={self.cost}, power={self.power})"
      

  
      
