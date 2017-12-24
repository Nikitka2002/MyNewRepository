import random
carrying_capacity_max = 60
carrying_capacity_min = 0
prize = ["goldCoins","empty","Illness"]

class Pirate:
    name = ""
    boat = int()
    chestCount = int()
    gold = int()
    Illness = int()
    emptyChest = int()
    def __init__(self,name,carrying):
        if((carrying>carrying_capacity_max) or (carrying_capacity_min<0)):
            print("!EROR! Carrying_capacity >60 or <0")
        self.name = name
        self.boat = carrying
    def takeChest(self):
        weight = 0
        while(weight <= self.boat):
            chest = Chest()
            if(chest.weight <= self.boat):
                weight += chest.weight
            if(chest.content == "goldCoins"):
                self.gold += chest.gold
            elif(chest.content == "empty"):
                self.emptyChest +=1
            elif(chest.content == "Illness"):
                self.Illness += chest.Illness
            self.chestCount += 1
    def ChestCount(self):
        return self.chestCount

class Chest:
    weight = int()
    content = " "
    gold = int()
    Illness = int()
    empty = int()
    def __init__(self,a = random.randint(4,10)):
        self.weight = a
        content = random.choice(prize)
        if(content == "goldCoins"):
            self.gold = random.randint(3,10)
            self.content = content
        elif(content == "empty"):
            self.empty += 1
            self.content = content
        elif(content == "Illness"):
            self.Illness = random.randint(3,10)
            self.content = content

Pirate1 = Pirate("Boris",59)
Pirate2 = Pirate("Pavel",25)
Pirate3 = Pirate("Kirill",30)
Pirate4 = Pirate("Semen",47)

Pirate4.takeChest()
Pirate3.takeChest()
Pirate1.takeChest()
Pirate2.takeChest()

print(Pirate1.name, " привез ", Pirate1.ChestCount()," сундука")
print(Pirate2.name, " привез ", Pirate2.ChestCount()," сундука")
print(Pirate3.name, " привез ", Pirate3.ChestCount()," сундука")
print(Pirate4.name, " привез ", Pirate4.ChestCount()," сундука")

Pirates = [Pirate1, Pirate2, Pirate3, Pirate4]

Gold_Coins = [Pirate1.gold, Pirate2.gold, Pirate3.gold, Pirate4.gold]
print("Больше всего золота привез/ли ")

for i in range(4):
    if(max(Gold_Coins)==Pirates[i].gold):
        print(Pirates[i])
print(" золота было ",max(Gold_Coins))

Empty_Chest = [Pirate1.emptyChest, Pirate2.emptyChest, Pirate3.emptyChest, Pirate4.emptyChest]
print("Больше всего пустых сундуков было  у  ")

for i in range(4):
    if(max(Empty_Chest)==Empty_Chest[i]):
        print(Empty_Chest[i])
print(" сундуков было  ",max(Empty_Chest))

Illness = [Pirate1.Illness, Pirate2.Illness, Pirate3.Illness, Pirate4.Illness]
print("Больше всего болел ")

for i in range(4):
    if(max(Illness)==Illness[i]):
        print(Illness[i])
print(" болезнь длилась ",max(Illness), " дня/ей")
