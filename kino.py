class Seans:
    def __init__(self, f_name, cena, seats):
        self.f_name = f_name 
        self.cena = cena
        self.seats = seats
        self.watchers = []
        self.money = 0
    def sell(self, name):
        if self.seats > len(self.watchers):
            self.money += self.cena
            self.watchers.append(name)
        else:
            print("МЕСТ НЕТ!!!!!!!!!!!!!!!!!")
    
    def all_money(self):
        print(self.money)
        print(self.seats - len(self.watchers))
        
batman = Seans("Batman", 15, 5)
batman.sell("Oleg")
batman.sell("Oleg")
batman.sell("Oleg")
batman.sell("Oleg")
batman.sell("Oleg")
batman.sell("Oleg")
batman.all_money()

