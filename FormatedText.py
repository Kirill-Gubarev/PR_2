def getColorCode(foreground="white", background="black"):  # возврат кода цвета
    f = ""  # текст
    b = ""  # фон
    if foreground == 'white':
        f = "\033[0m"
    elif foreground == 'black':
        f = "\033[30m"
    elif foreground == 'red':
        f = "\033[31m"
    elif foreground == 'green':
        f = "\033[32m"
    elif foreground == 'yellow':
        f = "\033[33m"
    elif foreground == 'blue':
        f = "\033[34m"
    elif foreground == 'purple':
        f = "\033[35m"
    elif foreground == 'turquoise':
        f = "\033[36m"
    elif foreground == 'gray':
        f = "\033[37m"
    else:  # если нет такого цвета
        f = "\033[0m"  # установить код для сброса

    if background == 'black':
        b = "\033[40m"
    elif background == 'red':
        b = "\033[41m"
    elif background == 'green':
        b = "\033[42m"
    elif background == 'yellow':
        b = "\033[43m"
    elif background == 'blue':
        b = "\033[44m"
    elif background == 'purple':
        b = "\033[45m"
    elif background == 'turquoise':
        b = "\033[46m"
    elif background == 'gray':
        b = "\033[47m"
    else:  # если нет такого цвета
        return "\033[0m" + f  # сбросить к стандартному а потом применить цвет текста
    return f + b  # вывод кода цвета


def clearColor():  # сбросить цвет
    print("\033[0m", end='')  # вывод кода сброса


def printFB(text="", fColor="", bColor="", end="\n"):  # вывести цветной текст
    print(getColorCode(fColor, bColor) + text, end=end)  # получить цвет, а потом добавить текст


def printC(text="", color="\033[0m", end="\n"):  # вывести цветной текст
    print(color + text, end=end)  # применить цвет и вывести текст


def setColor(color=""):  # установить цвет
    print(getColorCode(color), end='')  # применить цвет


def clear(count=20, color="\033[0m"):  # очистить консоль
    print(color + "\n" * count, end='')  # вывести переходы на следущую строку


class FormatText:  # класс для вывода текста
    def __init__(self, width=1, height=1, fDefColor="", bDefColor="", endChar='\n'):  # конструктор
        self.__matrix = [" " * width] * height  # матрица символов
        self.__colorCodes = list()  # список координат и кодов цвета
        self.__fDefColor = fDefColor  # цвет текста по умолчанию
        self.__bDefColor = bDefColor  # цвет фона по умолчанию
        self.__endChar = endChar  # последний символ строк

    def getDefColor(self):  # возврат кода цвета по умолчанию
        return getColorCode(self.__fDefColor, self.__bDefColor)  # вернуть код

    def clearMatrix(self):  # очистить матрицу
        self.__matrix = [" " * len(self.__matrix[0])] * len(self.__matrix)  # очистить матрицу
        self.__colorCodes.clear()  # очистить список кодов

    def printMatrix(self):  # вывести матрицу
        self.__colorCodes.sort()  # отсортировать список
        self.__colorCodes.reverse()  # перевернуть список
        defaultColor = self.getDefColor()  # код цвета по умолчанию

        for i in range(0, len(self.__colorCodes)):  # пройти по всему списку кодов цвета
            y = self.__colorCodes[i][0]  # y координата
            x = self.__colorCodes[i][1]  # x координата
            colorCode = self.__colorCodes[i][2]  # код цвета
            self.__matrix[y] = (self.__matrix[y][:x] +
                                colorCode +
                                (self.__matrix[y][x:] +
                                 defaultColor))  # запись кодов цвета в матрицу
        self.__matrix[0] = defaultColor + self.__matrix[0]  # добавить цвет по умолчанию в начало для корректного вывода
        for i in range(0, len(self.__matrix)):  # пройти по всем строкам
            print(self.__matrix[i], end=self.__endChar)  # вывести строку
        self.clearMatrix()  # очистить матрицу

    def writeMatrix(self, value, x, y, fColor="", bColor=""):  # запись текста в матрицу
        if y < 0:  # если меньше 0 значит доступ по отрицательному индексу
            y = len(self.__matrix) + y
        if x < 0:  # если меньше 0 значит доступ по отрицательному индексу
            x = len(self.__matrix[0]) + x

        if x > len(self.__matrix[y]): return  # если вышли за границу строки: ничего не вставлять, выходим

        if len(str(value)) + x <= len(self.__matrix[y]):  # если строка не выходит за границу строки списка
            rightCropIndex = len(str(value))  # последний индекс строки = длина строки
            # (строка вставится полностью)

        else:  # если строка выходит за границу строки списка
            rightCropIndex = len(self.__matrix[y]) - x  # находим индекс до которого будет обрезана строка
            # (строка будет вставлена от x до rightCropIndex)

        # находим индекс для получения обрезанной строки в списке если ее длина окажется равна 0

        leftCropIndex = x + len(str(value)) - len(self.__matrix[y])
        # находим индекс от которого будет обрезана 2 часть строки списка

        if fColor == "":  # если цвет не указан вставить увет по умолчанию
            fColor = self.__fDefColor
        if bColor == "":  # если цвет не указан вставить увет по умолчанию
            bColor = self.__bDefColor

        if leftCropIndex < 0:
            # если leftCropIndex будет положительным то
            # правая строка будет обрезаться отсчитывая индекс слева направо, а нужно справа на лево
            # поэтому в else она не добавляется
            self.__matrix[y] = (self.__matrix[y][:x] +
                                str(value)[:rightCropIndex] +
                                self.__matrix[y][leftCropIndex:])  # вставка строки
        else:
            self.__matrix[y] = (self.__matrix[y][:x] + getColorCode(fColor, bColor) +
                                str(value)[:rightCropIndex])  # вставка строки

        self.__colorCodes.append([y, x, getColorCode(fColor, bColor)])  # добавляем x y координаты и код цвета в список
