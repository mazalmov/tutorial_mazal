import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Welcome to the 'Guess the Number' game!")
    print("I am thinking of a number between 1 and 100.")
    
    while True:
        try:
            guess = int(input("Try to guess the number: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("Your guess is too low. Try again!")
            elif guess > number_to_guess:
                print("Your guess is too high. Try again!")
            else:
                print(f"Correct! The number was {number_to_guess}.")
                print(f"You finished the game in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()

