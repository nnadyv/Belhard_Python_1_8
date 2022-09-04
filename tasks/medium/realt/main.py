from house import House
from townhouse import Townhouse
from person import Person


if __name__ == "__main__":
    house1 = House("Mickiewicza", 46, 700)
    house = House("Chrobrego", 5, 800)
    townhouse1 = Townhouse("Mick", 3, 1000)
    townhouse2 = Townhouse("Crob", 4, 1100)
    person1 = Person("Anna", 75)
    person1.earn_money(3)
    person1.make_deal(house1)
    person1.earn_money(70)
    print(person1.info())
