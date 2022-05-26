import random

x = random.randint(1, 10)
#print(x)
user_num = 0
attempts = 0
while user_num != x and attempts != 3:
    attempts += 1
    user_num = int(input("Guess: "))
    if user_num == x:
        attempts = 3
if user_num == x:
    print("You guessed it!")
else:
    print("Sorry, you suck. Now go rethink your life..")
