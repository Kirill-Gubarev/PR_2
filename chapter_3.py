import math
from time import sleep
import FormatedText as Ft  # Модуль для вывода текста


class Game:  # игра
    class __Rocket:  # вложенный класс ракета
        def __init__(self, fuel=50, speed=0, capacity=-1):  # конструктор ракеты
            self.__fuel = float(fuel)  # топливо
            self.__capacity = self.__fuel if capacity == -1 else capacity  # емкость
            self.__speed = float(speed)  # скорость
            self.__activeEngine = False  # двигатель
            self.__activeReverseEngine = False  # обратный двигатель

        def getFuel(self):  # возврат топлива
            return self.__fuel

        def getCapacity(self):  # возврат емкости
            return self.__capacity

        def getSpeed(self):  # возврат скорости
            return self.__speed

        def getActiveEngine(self):  # возврат состояния двигателя
            return self.__activeEngine

        def getActiveReverseEngine(self):  # возврат состояния обратного двигателя
            return self.__activeReverseEngine

        def turnEngine(self, value):  # переключение двигателя
            if value and not self.__activeEngine:  # если двигатель выключен и его надо включить
                if self.__fuel >= 5:  # если топлива достаточно
                    self.__fuel -= 5  # на запуск двигателя тратится много топлива
                else:
                    value = False
            self.__activeEngine = value

        def turnReverseEngine(self, value):  # переключение обратного двигателя
            if value and not self.__activeReverseEngine:  # если двигатель выключен и его надо включить
                if self.__fuel >= 2.5:  # если топлива достаточно
                    self.__fuel -= 2.5  # на запуск двигателя тратится много топлива
                else:
                    value = False
            self.__activeReverseEngine = value

        def perform(self):  # выполнение команд ракеты
            if self.__fuel < 1:  # если топлива не достаточно
                self.turnEngine(False)  # выключить двигатель

            if self.__activeEngine:  # если двигатель работает
                self.__fuel -= 1  # сжечь топливо
                self.__speed += 1  # увеличить скорость

            if self.__fuel < 0.5:  # если топлива не достаточно
                self.turnReverseEngine(False)  # выключить обратный двигатель

            if self.__activeReverseEngine:  # если обратный двигатель работает
                self.__fuel -= 0.5  # сжечь топливо
                self.__speed -= 0.5  # уменьшить скорость

    def __init__(self, distance=500, rFuel=50, rSpeed=0, rCapacity=-1):  # конструктор игры
        self.__rocket = self.__Rocket(rFuel, rSpeed, rCapacity)  # ракета
        self.__distance = distance  # дистанция
        self.__wholeDistance = distance  # вся дистанция
        self.__prevSpeed = self.__rocket.getSpeed()  # предыдущая скорость
        self.__prevFuel = self.__rocket.getFuel()  # предыдущее топливо
        self.__prevDistance = self.__distance  # предыдущее расстояние
        self.__ft = Ft.FormatText(100, 7, "blue", "black")  # объект формирующий текст

    def __outInformation(self):  # вывод информации
        self.__ft.writeMatrix("Статус двигателя: ", 0, 0)  # запись текста
        if self.__rocket.getActiveEngine():  # если двигатель работает
            self.__ft.writeMatrix("Активен", 28, 0, "green")  # запись текста
        else:  # если не двигатель работает
            self.__ft.writeMatrix("Выключен", 28, 0, "red")  # запись текста

        self.__ft.writeMatrix("Статус обратного двигателя: ", 0, 1)  # запись текста
        if self.__rocket.getActiveReverseEngine():  # если обратный двигатель работает
            self.__ft.writeMatrix("Активен", 28, 1, "green")  # запись текста
        else:  # если обратный двигатель не работает
            self.__ft.writeMatrix("Выключен", 28, 1, "red")  # запись текста

        # ===СКОРОСТЬ===
        self.__ft.writeMatrix("Скорость: ", 0, 2)  # запись текста
        speed = self.__rocket.getSpeed()  # скорость ракеты
        self.__ft.writeMatrix(str(speed) + " м/c ", 12, 2, "yellow")  # запись скорости

        speed = abs(speed)  # модуль скорости
        difSpeed = speed - self.__prevSpeed  # разница скорости
        if difSpeed != 0:  # если разница не 0
            self.__ft.writeMatrix(f'{difSpeed:+}', 21, 2,
                                  "green" if difSpeed > 0 else "red")  # запись разности скорости

        self.__ft.writeMatrix("█" * math.ceil(speed), 27, 2,
                              "green" if speed <= 5 else ("yellow" if speed <= 10 else "red"))  # запись шкалы скорости

        # ===ТОПЛИВО===
        fuel = self.__rocket.getFuel()  # топливо ракеты
        self.__ft.writeMatrix("Топливо: ", 0, 3)  # запись текста
        self.__ft.writeMatrix(str(fuel) + " кг ", 12, 3, "yellow")  # запись топлива

        capacity = self.__rocket.getCapacity()  # емкость ракеты
        self.__ft.writeMatrix("█" * math.ceil(fuel / (capacity / 50)), 27, 3,
                              "green" if fuel >= capacity * 0.5 else (
                                  "yellow" if fuel >= capacity * 0.2 else "red"))  # запись шкалы топлива

        difFuel = self.__rocket.getFuel() - self.__prevFuel  # разница топлива
        if difFuel != 0:  # если разница не 0
            self.__ft.writeMatrix(f'{difFuel:+}', 21, 3, "green" if difFuel > 0 else "red")  # запись разности топлива

        if difFuel < 0:  # если разница меньше 0
            difFuel = abs(difFuel)  # модуль от разности топлива
            self.__ft.writeMatrix("█" * math.ceil(difFuel), 27 + math.ceil(fuel), 3,
                                  "red" if fuel >= capacity * 0.2 else "purple")  # запись шкалы разницы топлива
        self.__ft.writeMatrix("█" * math.ceil(capacity - fuel - difFuel),
                              27 + math.ceil(fuel) + math.ceil(difFuel), 3, "gray")  # запись шкалы пустой части топлива

        # ===РАССТОЯНИЕ===
        self.__ft.writeMatrix("Расстояние: ", 0, 4)  # запись текста
        self.__ft.writeMatrix(str(self.__distance) + " м", 12, 4, "yellow")  # запись расстояния

        difDistance = self.__distance - self.__prevDistance  # разница расстояния
        if difDistance != 0:  # если разница расстояния не 0
            self.__ft.writeMatrix(f'{difDistance:+}', 21, 4,
                                  "green" if difDistance < 0 else "red")  # запись разницы рассотяния
        self.__ft.writeMatrix("=>", 27 + int((self.__wholeDistance - self.__distance) / (self.__wholeDistance / 50)), 4,
                              "blue")  # запись кораблика
        self.__ft.writeMatrix("=0==0=", 27 + 50, 4, "purple")  # запись станции
        self.__ft.writeMatrix("Следующее действие: ", 0, 6)  # запись текста

        self.__prevSpeed = abs(self.__rocket.getSpeed())  # предыдущая скорость
        self.__prevFuel = self.__rocket.getFuel()  # предыдущее топливо
        self.__prevDistance = self.__distance  # предыдущее расстояние

        self.__ft.printMatrix()  # вывод текста

    def __performAction(self):  # выполнение декствий
        key = input()  # ввод
        if 'stE' in key:  # Start Engine
            self.__rocket.turnEngine(True)  # включить двигатель
        elif 'spE' in key:  # Stop Engine
            self.__rocket.turnEngine(False)  # выключить двигатель
        if 'stRE' in key:  # Start Reverse Engine
            self.__rocket.turnReverseEngine(True)  # включить обратный двигатель
        elif 'spRE' in key:  # Stop Reverse Engine
            self.__rocket.turnReverseEngine(False)  # выключить обратный двигатель

    def __win(self):  # победа
        Ft.printC("Команда: мы приблизились к станции - начать стыковку", self.__ft.getDefColor())  # вывод текста
        sleep(5)  # подождать 5 секунд
        Ft.printC("Команда: cтыковка прошла успешно!", self.__ft.getDefColor())  # вывод текста
        sleep(4)  # подождать 4 секунды
        Ft.printFB("Победа!", "green", "black")  # вывод текста

    def __defeat(self):  # поражение
        Ft.printC("Команда: мы приближаемся к станции очень быстро!", self.__ft.getDefColor())  # вывод текста
        sleep(5)  # подождать 5 секунд
        Ft.printC("Команда: скорость ", self.__ft.getDefColor(), '')  # вывод текста
        Ft.printFB("?©", "red", "black", '')  # вывод текста
        Ft.printFB("сл|и-ишк-ик", "blue", "black", '')  # вывод текста
        Ft.printFB("<P^óE?©ì8Ì~bUjÄL0«h¨bÇP7ýeÜ", "red", "black")  # вывод текста
        sleep(6)  # подождать 6 секунд
        Ft.printFB("Связь с командой потеряна...", "red", "black")  # вывод текста
        sleep(6)  # подождать 6 секунд
        Ft.printFB("Поражение...", "red", "black")  # вывод текста

    def __defeatNotFuel(self):  # поражение закончилось топливо
        Ft.printC("Команда: мы приблизились к станции - начать стыковку", self.__ft.getDefColor())  # вывод текста
        sleep(5)  # подождать 5секунд
        Ft.printC("Команда: двигатели отключились, топлив", self.__ft.getDefColor(), '')  # вывод текста
        Ft.printFB("ïÍ¨T3MûH¥ño¿x³", "red", "black")
        sleep(6)  # подождать 6 секунд
        Ft.printFB("Окружение: никто не отвечает...", "purple", "black")  # вывод текста
        sleep(6)  # подождать 6 секунд
        Ft.printFB("Связь с командой потеряна...", "red", "black")  # вывод текста
        sleep(6)  # подождать 6 секунд
        Ft.printFB("Поражение...", "red", "black")  # вывод текста

    def mainLoop(self):  # главный цикл
        while True:  # бесконечный цикл
            Ft.clear(color=self.__ft.getDefColor())  # очистка консоли
            self.__outInformation()  # вывод информации
            self.__performAction()  # выполнение действия
            self.__rocket.perform()  # выполнение действий ракеты
            self.__distance -= self.__rocket.getSpeed()  # уменьшение расстояния за 1 цикл

            if self.__distance <= 10:  # если расстояние меньше или равно 10
                if self.__rocket.getSpeed() > 10:  # если скорость больше 10
                    self.__defeat()  # поражение
                elif self.__rocket.getFuel() < 3:  # если топлива не достаточно для стыковки
                    self.__defeatNotFuel()  # поражение закончилось топливо
                else:
                    self.__win()  # победа
                break  # конец цикла
