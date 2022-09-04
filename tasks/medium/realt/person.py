class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.money = 0
        self.realty = []

    def info(self):
        return f"{self.name}, {self.age} , {self.money}$, {self.realty}"

    def earn_money(self, value):
        self.money += value

    def make_deal(self, obj):
        if self.money >= obj.cost:
            self.money -= obj.cost
            self.realty.append(obj)
