from decouple import config
import random
MAX_NUMBER = 30
rich_people = 200000
cash = int(config("MY_MONEY"))


class Casino:
    def __init__(self):
        self.__money = cash

        while self.__money > 0:
            try:
                print(f'Bank account:{self.__money}')
                self.__winNumber = random.randint(1, 30)
                self.__choice = int(input('Выберите число от 1 до 30:\n'))
                if self.__choice > MAX_NUMBER:
                    print('Вводи только числа от 1 до 30')
                else:
                    print(f'Ваше число:{self.__choice}')
                self.__bet = int(input('Сколько денег хотите слить:\n'))
                if self.__bet > self.__money:
                    print(f'у вас только: {self.__money}')
                    break
                else:
                    self.__money = self.__money - self.__bet
                if self.__winNumber == self.__choice and self.__money > rich_people:
                    win_money = self.__bet * 2
                    self.__money = self.__money + win_money
                    print('Тебе повезло сегодня, но не завтра ты сольешь вдвойне')
                else:
                    user_round = input('Вы проиграли!\nХотите проиграть еще денег?')
                    if user_round == 'da':
                        continue
                    elif user_round == 'net':
                        break
                    else:
                        print('error 404')
            except ValueError:
                print('Вводите только числа!')


    




