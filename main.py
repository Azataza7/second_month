#
# import random
#
# round_number = 0
#
#
# class GameEntity:
#     def __init__(self, name, hp, damage):
#         self.__name = name
#         self.__hp = hp
#         self.__damage = damage
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#
#     @property
#     def hp(self):
#         return self.__hp
#
#     @hp.setter
#     def hp(self, value):
#         if value > 0:
#             self.__hp = value
#         else:
#             self.__hp = 0
#
#     @property
#     def damage(self):
#         return self.__damage
#
#     @damage.setter
#     def damage(self, value):
#         self.__damage = value
#
#     def __str__(self):
#         return f"{self.name} HP: {self.hp} [{self.damage}]"
#
#
# class Boss(GameEntity):
#     def __init__(self, name, hp, damage):
#         GameEntity.__init__(self, name, hp, damage)
#
#
# class Hero(GameEntity):
#     def __init__(self, name, hp, damage, skill):
#         GameEntity.__init__(self, name, hp, damage)
#         self.__skill = skill
#
#     @property
#     def skill(self):
#         return self.__skill
#
#     @skill.setter
#     def skill(self, value):
#         self.__skill = value
#
#     def apply_super_power(self, boss, heroes):
#         pass
#
#
# class Warrior(Hero):
#     def __init__(self, name, hp, damage):
#         Hero.__init__(self, name, hp, damage, "CRITICAL DAMAGE")
#
#     def apply_super_power(self, boss, heroes):
#         coeff = random.randint(2, 5)
#         boss.hp -= coeff * self.damage
#         print(f"{self.name} КРИТИЧЕСКИЙ УРОНИЩЕ: {coeff * self.damage}")
#
#
# class Magic(Hero):
#     def __init__(self, name, hp, damage):
#         Hero.__init__(self, name, hp, damage, "BOOST")
#
#     def apply_super_power(self, boss, heroes):
#         boost = random.randint(5, 10)
#         for hero in heroes:
#             if hero.hp > 0:
#                 hero.damage += boost
#                 print("ТЫ НЕ ПРОЙДЕШЬ!!!!!!")
#
#
# class Medic(Hero):
#     def __init__(self, name, hp, damage, heal_points):
#         Hero.__init__(self, name, hp, damage, "HEAL")
#         self.__heal_points = heal_points
#
#     def apply_super_power(self, boss, heroes):
#         for hero in heroes:
#             if hero.hp > 0 and self != hero and self != Avrora.hp:
#                 hero.hp += self.__heal_points
#                 print("Кореш, ща всё будет пучком! Ща я тебя подлатаю!!)")
#
#
# class Berserk(Hero):
#     def __init__(self, name, hp, damage):
#         Hero.__init__(self, name, hp, damage, "SAVE DAMAGE AND RETURN")
#
#     def apply_super_power(self, boss, heroes):
#         damage_range = [5, 10, 15]
#         saved = random.choice(damage_range)
#         self.hp += saved
#         boss.hp -= saved
#         print("Берсерк применил что-то.......")
#
#
#
# class Thor(Hero):
#
#     def __init__(self, name, hp, damage):
#         Hero.__init__(self, name, hp, damage, "FREEZE BOSS")
#
#     def apply_super_power(self, boss, heroes):
#         random_freeze = [1, 2, 3, 4, 5]
#         freeze = random.choice(random_freeze)
#         if freeze == 3:
#             self.hp += 50
#             print("Тор дал по бошку боссу!")
#
#
# class Golem(Hero):
#
#     def __init__(self, name, hp, damage):
#         Hero.__init__(self, name, hp, damage, "DEFEND")
#
#     def apply_super_power(self, boss, heroes):
#         for hero in heroes:
#             if hero.hp > 0 and self != hero:
#                 defend_range = [10, 5, 8]
#                 saved = random.choice(defend_range)
#                 self.hp += saved
#         # for hero in heroes:
#         #     hero.hp += self.defend_point
#
#
# class Witcher(Hero):
#

#     def __init__(self, name, hp, damage, revive_point):
#         Hero.__init__(self, name, hp, damage, "REVIVE")
#         self.revive_point = revive_point
#
#     def apply_super_power(self, boss, heroes):
#         health = 1
#         self.damage = 0
#         for hero in heroes:
#             if health <= 0 and hero.hp <= 0:
#                 if hero.hp == 0 and self != hero:
#                     self.hp += hero.hp
#                     print("Пацан к успеху шёл, не получилось... не фортануло!!")
#
#
# class Avrora(Hero):
#
#     def __init__(self, name, hp, damage, invisibility=1):
#         super().__init__(name, hp, damage, "INVISIBILITY")
#         self.invisibility = invisibility
#
#     def apply_super_power(self, boss, heroes):
#         invisibility = [1, 2, 3]
#         if invisibility == 2:
#             self.hp += 150
#             save_range = [10, 12, 15]
#             saved = random.choice(save_range)
#             self.hp += saved
#             boss.hp -= saved
#             print("Аврора вошла в режим невидимости")
#
#
# class Druid(Hero):
#
#     def __init__(self, name, hp, damage, angel=1):
#         super().__init__(name, hp, damage, "ANGEL AND VORON", )
#         self.angel = angel
#
#     def apply_super_power(self, boss, heroes):
#         random1 = random.randint(1, 5)
#         if random1 == 5 and boss.hp <= 500:
#             self.hp += 3
#             self.damage += 3
#             boss.damage += 25
#             print("Друид ПРЕДАТЕЛЬ!!!! Пахану боссу дал 50% урона!!!!")
#
#
# class AntMan(Hero):
#
#     def __init__(self, name, hp, damage, the_size=1):
#         super().__init__(name, hp, damage, "THE_SIZE")
#         self.the_size = the_size
#
#     def apply_super_power(self, boss, heroes):
#         random1 = random.randint(1, 5)
#         if random1 == 5:
#             self.hp += 150
#             self.damage += 8
#             print("Букашка увеличилось!")
#         elif random == 1 or 2 or 3 or 4:
#             self.hp -= 150
#             self.damage -= 3
#             print("Букашка уменьшилось?")
#
#
# def start():
#     boss = Boss(name="Void", hp=1000, damage=50)
#
#     warrior = Warrior("Ahiles", 270, 15)
#     medic_1 = Medic("Aibolit", 200, 5, 15)
#     magic = Magic("Bairon", 280, 30)
#     berserk = Berserk("Titan", 250, 10)
#     medic_2 = Medic("Medbrat", 230, 10, 5)
#     Thor1 = Thor("Торомэн", 190, 8)
#     Golem1 = Golem("Железный голем", 450, 1)
#     Witcher1 = Witcher("Ведьмак", 220, 0, 150)
#     Avrora1 = Avrora("Трусы", 185, 5)
#     Druid1 = Druid("Сэм", 155, 4, 3)
#     AntMan1 = AntMan("Букашка", 190, 5)
#
#     heroes = []
#     heroes_max = 0
#
#
#     while heroes_max < 4:
#         heroes_game = input("Выберите героев: ")
#         if heroes_game == 'Ahiles':
#             heroes.append(warrior)
#             heroes_max += 1
#             print("Вы выбрали: Ahiles")
#             continue
#         elif heroes_game == 'Aibolit':
#             heroes.append(medic_1)
#             heroes_max += 1
#             print("Вы выбрали: Aibolit")
#         elif heroes_game == 'Bairon':
#             heroes.append(magic)
#             heroes_max += 1
#             print("Вы выбрали: Bairon")
#         elif heroes_game == 'Titan':
#             heroes.append(berserk)
#             heroes_max += 1
#             print("Вы выбрали: Titan")
#         elif heroes_game == 'Medbrat':
#             heroes.append(medic_2)
#             heroes_max += 1
#             print("Вы выбрали: Mebrat")
#         elif heroes_game == 'Торомэн':
#             heroes.append(Thor1)
#             heroes_max += 1
#             print("Вы выбрали: Торомэн")
#         elif heroes_game == 'Железный голем':
#             heroes.append(Golem1)
#             heroes_max += 1
#             print("Вы выбрали: Железный голем")
#         elif heroes_game == 'Ведьмак':
#             heroes.append(Witcher1)
#             heroes_max += 1
#             print("Вы выбрали: Ведьмак")
#         elif heroes_game == 'Трусы':
#             heroes.append(Avrora1)
#             heroes_max += 1
#             print("Вы выбрали: Трусы")
#         elif heroes_game == 'Сэм':
#             heroes.append(Druid1)
#             heroes_max += 1
#             print("Вы выбрали: Сэм")
#         elif heroes_game == 'Букашка':
#             heroes.append(AntMan1)
#             heroes_max += 1
#             print("Вы выбрали: Букашка")
#         else:
#             print("Этого героя не существует!")
#
#         if heroes_max == 4:
#             print("")
#             while not is_game_finished(boss, heroes):
#                 if boss.hp <= 0:
#                     print('Герои выиграли!!! ыгыгыгы')
#                     break
#                 play_round(boss, heroes)
#
#
#
# def print_stats(boss, heroes):
#     print(f"------------------ ROUND: {round_number}---------------------")
#     print(boss)
#     for hero in heroes:
#         print(hero)
#
#
# def boss_hits(boss, heroes):
#     for hero in heroes:
#         if hero.hp > 0 and boss.hp > 0:
#             hero.hp -= boss.damage
#
#
# def heroes_hit(boss, heroes):
#     for hero in heroes:
#         if hero.hp > 0 and boss.hp > 0:
#             boss.hp -= hero.damage
#
#
# def heroes_skills(boss, heroes):
#     for hero in heroes:
#         if hero.hp > 0 and boss.hp > 0:
#             hero.apply_super_power(boss, heroes)
#
#
# def is_game_finished(boss, heroes):
#     if boss.hp <= 0:
#         print("Герои выиграли!!! ыгыгыгы")
#         return False
#
#     all_heroes_dead = True
#     for hero in heroes:
#         if hero.hp > 0:
#             all_heroes_dead = False
#             break
#
#     if all_heroes_dead:
#         print("Босс выиграл муахахахаха!!!!")
#     return all_heroes_dead
#
#
# def play_round(boss, heroes):
#     global round_number
#     round_number += 1
#     boss_hits(boss, heroes)
#     heroes_hit(boss, heroes)
#     heroes_skills(boss, heroes)
#     print_stats(boss, heroes)
#
#
# hero.health <= 100 and self != hero:
#                 hero.health = hero.health - low_damage
#                 damage_blocked = low_damage * 7
#                 print(f'Количество заблокированного урона:{damage_blocked}')
