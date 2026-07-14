import random
secret_number = random.randint(1,10)

print("===== Number Guessing Game =====")

attempts = 1

while attempts <= 5:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess <= 0 or guess > 10:
        print("Invalid input, Enter a number between 1 and 10 only‼")
        continue
    if guess == secret_number:
        print("You guessed it right! In ", attempts, "attempts.")
        break
    elif guess < secret_number:
        print("Too low. Try again‼")
        
    elif guess > secret_number:
        print("Too high. Try again‼")
        
    attempts += 1

if attempts > 5:
    print("you have used all your chances! The secret number was: ", secret_number)
    
    