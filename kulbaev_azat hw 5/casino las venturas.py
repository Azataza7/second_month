
from decouple import config
import random

cash = int(config('MY_MONEY', default=0))


class Casino:
    def __init__(self):
        self.__money = cash

    def money(self):
        return self.__money

    def __str__(self):
        return f'total money:{self.money()}'
    

print(Casino())


