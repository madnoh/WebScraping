# Tai Sai simulator

'''from itertools import combinations_with_replacement

threeDice = combinations_with_replacement(range(1, 7), 3)
#print(list(threeDice))
print(type(threeDice))'''

# Small is between 4 to 10, except triples Pay 1:1
# Big is between 11 to 17, except triples Pay 1:1
# Triples pay 1:30
# Specific triples Pay 1:180
# Doubles Pay 1:11
# Total 4 or 17 Pay 1:60
# Total 5 or 16 Pay 1:20
# Total 6 or 15 Pay 1:18
# Total 7 or 14 Pay 1:12
# Total 8 or 13 Pay 1:8
# Total 9, 10, 11 or 12 Pay 1:6

from random import randint

# Look at def dice_roll (num_dice = 0 , num_sides = 0):
# Look at return sum(random.randint(1,num_sides) for die in range(num_dice))
positive, negative = 0, 0

for _ in range(1000):
    cash, win = 100, 0
    bet1, bet2 = 1, 1
    winresult = [9, 10 , 11, 12]
    iterations = 100

    def isTriple(d1, d2, d3):
        if d1 == d2 and d2 == d3:
            return bet1 * 31
        return 0

    def NineToTwelve(d1, d2, d3):
        if d1+ d2 + d3 in winresult:
            return bet2 * 7
        return 0

    for i in range(0,iterations):
        dice1, dice2, dice3 = randint(1,6), randint(1,6), randint(1,6)
        win = isTriple(dice1, dice2, dice3) + NineToTwelve(dice1, dice2, dice3)
        cash = win - bet1 - (4 * bet2)

    if cash > 0:
        positive += 1
    else:
        negative += 1

print(f'Win = {positive} times, Lose = {negative} times.')

