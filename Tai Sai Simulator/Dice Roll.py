from random import randint

sum = [0] * 13
doubles = 0
iterations = 1000000
pct = 100/iterations

for i in range(0,iterations):
    dice1, dice2 = randint(1,6), randint(1,6)
    sum[dice1 + dice2] += 1
    if dice1 == dice2:
        doubles += 1

for i in range(2,13):
    print(f'Dice total {i} = {(sum[i] * pct):.3f}%')

print(f'doubles = {(doubles * pct):.3f}%')