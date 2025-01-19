import random 

randomNum = random.randint(1,10);

print("I am think of a number between 1 and 10");

print(str(randomNum));1

## None null value place holder

playerGuess = None;

while playerGuess != randomNum:
    print('your guess: ');
    playerGuess = int(input());

    if playerGuess < randomNum:
        print('Your guess is too low');
    elif playerGuess > randomNum:
        print('Your guess is too high');
    else:
        break;

if playerGuess == randomNum:
    print("You guess my number " + str(randomNum));


