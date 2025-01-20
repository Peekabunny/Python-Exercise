import random

cpu = random.randint(1,3)

# 1 = rock, 2 = paper, 3 = scissor

guess = None;

if cpu == 1:
    cpu = 'r';
elif cpu == 2:
    cpu = 'p';
else:
    cpu = 's'

print('Lets play Rock, Paper, Scissor: ')

# cant use guess != cpu in 2.1 in 2.1r
while True:
    print('player type r for rock, p for paper, and scissor for s')
    guess = input();
    if guess == cpu:
        print('Draw try again');
        continue;
    elif guess == 'r' and cpu == 'p':
        print('You Lost');
        break;
    elif guess == 'r' and cpu == 's':
        print('You Win!');
        break;
    elif guess == 'p' and cpu == 's':
        print('You Lost');
        break;
    elif guess == 'p' and cpu == 'r':
        print('You Win!');
        break;
    elif guess == 's' and cpu == 'r':
        print('You Lost');
        break;
    elif guess == 's' and cpu == 'p':
        print('You Win!');
        break;
