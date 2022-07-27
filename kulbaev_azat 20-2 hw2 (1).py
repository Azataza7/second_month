class Figure:
    unit = 'mm'
    perimeter = 0

    def __init__(self):
        self.__perimeter = perimeter
        self.__calculate_perimeter = calculate_perimeter

    @property
    def get_perimeter(self):
        return self.__perimeter

    @get_perimeter.setter
    def set_perimeter(self, value):
        if isinstance(value, str):
            raise TypeError('Write only numbers ')
        else:
            self.__perimeter = value

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        self.__calculate_perimeter = calculate_perimeter

    def info(self):
        print(f'perimeter:{self.get_perimeter},settings:{self.set_perimeter}')


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length

    def calculate_perimeter(self):
        self.perimeter = side_length * 4





    # def calculate_area(self):
    #     return self.__side_length **2
    #
    # def calculate_


