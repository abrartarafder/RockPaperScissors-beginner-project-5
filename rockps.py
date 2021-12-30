import random

def game():
    count = 0
    r_count = 0
    for i in range(3):
        print("Welcome to Rock, Paper, Scissors best of 3")
        print("************************************")
        user_input = input("Enter rock, paper or scissor: ")
        options = ("rock","paper", "scissor")
        r = random.choice(options)
        print(f'computer entered: {r}')
        if user_input == r:
            print("Tie game")
        if user_input == "rock" and r == "scissor":
            print("Game Won")
            count += 1
        if user_input == "rock" and r == "paper":
            print("Game Lost")
            r_count += 1
        if user_input == "scissor" and r == "rock":
            print("Game Lost")
            r_count += 1
        if user_input == "scissor" and r == "paper":
            print("Game Won")
            count += 1
        if user_input == "paper" and r == "rock":
            print("Game Won")
            count += 1
        if user_input == "paper" and r == "scissor":
            print("Game Lost")
            r_count += 1
    return f"Computer score: {r_count}, Your score: {count}"


print(game())
