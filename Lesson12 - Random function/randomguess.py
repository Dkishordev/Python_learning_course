import random
lowest_number=1
highest_number=100

answer = random.randint(lowest_number,highest_number)

print(f"Enter any number between {lowest_number} and {highest_number} :")
count =0
is_guess =True

while is_guess:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess=int(guess)
        count+=1
        if guess < lowest_number or guess > highest_number:
            print("Invalid number")
            print(f"Enter any number between {lowest_number} and {highest_number} :")
        elif guess < answer:
            print("Your guess is too low.")
        elif guess > answer:
            print("Your guess is too high.")
        else:
            print("Correct answer!.")
            print(f"You made it in {count} attemps.")
            is_guess =False

    else:
        print("Invalid number")
        print(f"Enter any number between {lowest_number} and {highest_number} :")