import random
rand = random.randint(1,100)
guessed = False
for chance in range(10):
    guess = int(input("Try to guess the number: "))
    if guess == rand:
        print(f"Congratulations you guessed it correcly in {chance} chances")
        guessed= True
        break
    if guess > rand:
        print("You guessed a greater value")
    if guess < rand:
        print("You guessed a smaller value")
if guessed == False:
    print(f"You could not guess it the number was {rand}")
