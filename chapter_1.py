class Entity:

    def __init__(self, life=3, damage=1, resistance=1):
        self.__life = float(life)
        self.__damage = float(damage)
        self.__resistance = float(resistance)

    def getLife(self):  # геттер
        return self.__life

    def getDamage(self):  # геттер
        return self.__damage

    def takeDamage(self, damage):  # получить урон
        self.__life -= damage / self.__resistance

    def attack(self, entity):  # атаковать
        entity.takeDamage(self.__damage)

    def heal(self, count=1):  # восстановить здоровье
        self.__life += count

    def useAbility(self, entity):  # использовать способность
        self.attack(entity)


class Thanos(Entity):
    def __init__(self, life=100, damage=10, resistance=10):  # переопределение аргументов по умолчанию
        super().__init__(life, damage, resistance)

    def useInfinityGauntlet(self, entity):  # перчатка бесконечности
        entity.takeDamage(9999999999999)

    def useAbility(self, entity):  # использовать способность
        self.useInfinityGauntlet(entity)
