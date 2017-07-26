from random import randint

player=input('rock (r), paper (p), scissors (s)?')

print(player, 'vs', end='')

chosen=randint(1,3)


if chosen == 1:
  computer = 'r'
elif chosen == 2:
  computer = 'p'
else:
  computer = 's'
