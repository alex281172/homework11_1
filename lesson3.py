import random


raz = int(input('Сколько раз вы хотите играть? :'))

from famous_pers import *

# import famous_pers
for couter in range(raz):
    famous_pers.get_person_and_question()
    # get_person_and_question()

print('Все!')