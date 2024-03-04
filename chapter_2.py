class Restaurant:
    def __init__(self, address, numberOfStars, numberOfEmployees, income, owner):
        self.__address = address  # адресс
        self.__numberOfStars = int(numberOfStars)  # количество звезд
        self.__numberOfEmployees = int(numberOfEmployees)  # количество работников
        self.__income = income  # доход
        self.__owner = owner  # владелец

    def getAddress(self): return self.__address

    def setAddress(self, address):
        self.__address = address
        return self

    def getNumberOfStars(self): return self.__address

    def setNumberOfStars(self, numberOfStars):
        self.__numberOfStars = numberOfStars
        return self

    def getNumberOfEmployees(self): return self.__numberOfEmployees

    def setNumberOfEmployees(self, numberOfEmployees):
        self.__numberOfEmployees = numberOfEmployees
        return self

    def getNumberOfIncome(self): return self.__income

    def setNumberOfIncome(self, income):
        self.__numberOfIncome = income
        return self

    def getNumberOfOwner(self): return self.__owner

    def setNumberOfOwner(self, owner):
        self.__numberOfOwner = owner
        return self

    def addEmployee(self):
        self.__numberOfEmployees += 1
        return self

    def addStars(self):
        self.__numberOfStars += 1
        return self

    def addIncome(self, count):
        self.__income += count
        return self


class Hotel(Restaurant):  # отель
    def __init__(self, address, numberOfStars, numberOfEmployees, income, owner,
                 numberOfRooms):  # переопределение конструктора
        super().__init__(address, numberOfStars, numberOfEmployees, income, owner)  # вызов родительского конструктора
        self.__numberOfRooms = int(numberOfRooms)  # количество комнат

    def getNumberOfRooms(self): return self.__numberOfRooms

    def setNumberOfRooms(self, numberOfRooms):
        self.__numberOfRooms = numberOfRooms
        return self
