import pygame
class Miner:
    def __init__(self,name,cost,power,buy):
        self.name = name
        self.cost = cost
        self.power = power
        self.buy = buy
    def __str__(self):
     return f"Miner(name ='{self.name}', cost={self.cost}, power={self.power}), buy={self.buy}"
      

  
      
