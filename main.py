
class Converter:
    def __init__(self):

        # 1 килограмм = ...
        self.weight = {"килограмм": 1, "карат": 5000,
                       "грамм": 1000, "тонна": 0.001,
                       "фунт": 2.205, "унция": 35.27,
                       "драхма": 564.4, "гран": 15432,
                       }

        # 1 метр = ...
        self.distance = {"метр": 1, "сантиметр": 100,
                         "километр": 0.001, "миля": 0.0006214,
                         "ярд": 1.094, "фут": 3.281,
                         "лье": 0.0002071, "дюйм": 39.37,
                         }

        # 1 кубический метр
        self.volume = {"кубический метр": 1, " кубический сантиметр": 1000000,
                       "литр": 1000, "миллилитр": 1000000,
                       "галлон": 264.2, "пинта": 2113,
                       "жидкая унция": 33814, "жидкая драхма": 270512,
                       }

        # 1 квадратный метр = ...
        self.area = {"квадратный метр": 1, "квадратный километр": 0.000001,
                     "гектар": 0.0001, "сотка": 0.01,
                     "акр": 0.0002471, "квадратный фут": 10.76,
                     }

        # 1 метр в секунду
        self.speed = {"метр в секунду": 1, " километр в час": 3.6,
                      "миля в час": 2.237, "фут в час": 11811,
                      "узел": 1.944,
                      }

        self.unit_classes = {"Вес": self.weight, "Расстояние": self.distance, "Объем": self.volume,
                             "Площадь": self.area, "Скорость": self.speed}

    def choose_unit_class(self, unit_class_index):

        if len(self.unit_classes) <= unit_class_index or unit_class_index < 0:
            return "Wrong input"

        unit_class = list(self.unit_classes.keys())[unit_class_index]
        return unit_class

    def choose_unit(self, unit_class, unit_index):

        if len(self.unit_classes[unit_class]) <= unit_index or unit_index < 0:
            return "Wrong input"

        unit = list(self.unit_classes[unit_class].keys())[unit_index]
        return unit

    def process_unit(self, unit_class, unit, value):
        standard_value = value / self.unit_classes[unit_class][unit]

        converted_values = dict()

        for key, value in self.unit_classes[unit_class].items():
            converted_values[key] = value * standard_value

        return converted_values



if __name__ == "__main__":
    conv = Converter()
    while True:
        print()
        print(">------------------------------------------------<")

        for i, key in enumerate(conv.unit_classes.keys()):
            print(f'{i} -- {key}')

        # выбор группы величин
        unit_class_index = int(input("Выберите класс величины (номер класса): "))
        unit_class = conv.choose_unit_class(unit_class_index)

        if unit_class == "Wrong input":
            print("НЕВЕРНЫЙ ВВОД")
            continue

        # выбор величины
        for i, key in enumerate(conv.unit_classes[unit_class].keys()):
            print(f'{i} -- {key}')

        unit_index = int(input("Выберите величину (номер величины): "))
        unit = conv.choose_unit(unit_class, unit_index)

        if unit == "Wrong input":
            print("НЕВЕРНЫЙ ВВОД")
            continue

        # расчет
        value = float(input("Введите величину (число): "))
        converted_values = conv.process_unit(unit_class, unit, value)

        for key, value in converted_values.items():
            print(f'{key} -- {value}')