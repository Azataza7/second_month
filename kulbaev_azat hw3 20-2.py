class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return self.__cpu + self.__memory

    def __gt__(self, other):
        return self.memory > other.memory

    def __lt__(self, other):
        return self.memory < other.memory

    def __ge__(self, other):
        return self.memory >= other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __str__(self):
        return f'{self.cpu},{self.memory},{self.make_computations()}'


class Phone:
    def __init__(self, sim_card_list):
        self.__sim_card_list = sim_card_list

    @property
    def sim_card_list(self):
        return self.__sim_card_list

    @sim_card_list.setter
    def sim_card_list(self, value):
        self.__sim_card_list = value

    @staticmethod
    def call(sim_card_number, call_to_number):
        return f'Идет звонок на номер {call_to_number},c сим-карты: {sim_card_number},' \
               f'{Phone.sim_card_list[sim_card_number]}'

    def __str__(self):
        return f'Список сим кард:{self.sim_card_list}'


Phone.sim_card_list = ['beeline', 'megacom', 'fonex']


class Smartphone(Computer, Phone):
    def __init__(self, cpu, memory, location):
        super().__init__(cpu, memory)
        self.location = location

    @staticmethod
    def use_gps(location):
        return f'Вы проложили маршрут до {location}'

    def __str__(self):
        return f'location:{self.location}, cpu:{self.cpu},memory:{self.memory} sim_cards:{self.sim_card_list}'


windows = Computer(101010, 10234)
nokia = Phone('megacom')
iphone = Smartphone(6, 8, 'asia mall')
xiaomi = Smartphone(10, 16, 'los santos')
print(windows)
print(nokia)
print(iphone)
print(xiaomi)
print(nokia.call(0, 99554443))
print(iphone.use_gps('bishkek'))
print(Smartphone.mro())
print(iphone > xiaomi)























