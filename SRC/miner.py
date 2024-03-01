import pygame
class Miner:
    #Miner cost is (cost= b(1.25)^x where b =base cost and x = owned miners 
    def __init__(self,name,cost,power,amount):
        self.name = name
        self.cost = cost
        self.power = power
        self.amount = amount
    def __str__(self):
     return f"Miner(name ='{self.name}', cost={self.cost}, power={self.power} amount={self.amount})"
      

  
      
