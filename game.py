class Human:
    def __init__(self, hp = 5, attack = 20):
        self.hp = hp
        self.attack = attack
    def __str__(self):
        return f"{self.__class__.__name__}, Hp:{self.hp}, Attack:{self.attack}" 
    def fight(self, enemy):
        enemy.hp -= self.attack
        if enemy.hp <= 0:
            enemy.hp = 0
class Knight(Human):
    def __init__(self, hp, attack, stamina):
        super().__init__(hp, attack)
        self.stamina = stamina
    def __str__(self):
        return super().__str__() + f", Stamina:{self.stamina}"
    def fight(self, enemy): 
        if self.stamina < 10:
            print("You can not attack!")
        else:
            super().fight(enemy) 
            self.stamina -= 10
    def rest(self):
        self.stamina += 30
        if self.stamina >= 100:
            self.stamina = 100

knight = Knight(200, 25, 100)
print(knight)

human = Human(100, 10)
knight.fight(human)
knight.rest()
print(knight)
print(human)
# print(human)
# human_2 = Human()
# print(human_2)
# human.fight(human_2)
# human.fight(human_2)
# print(human_2)
