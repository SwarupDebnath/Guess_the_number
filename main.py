ans = 18
guess = 0
print("Guess a number from 1 to 60\nLevel 1 : 10 attempts, level 2 : 8 attempts, level 3 : 5 attempts")
lev = int(input("Choose level (1 or 2 or 3) : "))
if lev == 1:
    guess = 10
elif lev == 2:
    guess = 8
elif lev == 3:
    guess = 5
attempt = guess
while guess > 0:
    user = int(input("guess the number : "))
    guess = guess - 1
    if user == ans:
        print("\nCongratulations you guessed it right and you took", attempt - guess, "attempts")
        break
    elif guess == 0:
        print("\nGame over the secret number was", ans)
    elif user > ans:
        print("\nAttempts left :", guess)
        print("The number is less than", user, end=", ")
        continue
    elif user < ans:
        print("\nAttempts left :", guess)
        print("The number is greater than", user, end=", ")
        continue