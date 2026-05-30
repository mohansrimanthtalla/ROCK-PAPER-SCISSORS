import random

# Function to display rules
def show_rules():
    print("\n========== RULES ==========")
    print("Rock beats Scissors")
    print("Scissors beats Paper")
    print("Paper beats Rock")
    print("===========================\n")

# Function to get winner
def determine_winner(user, computer):
    if user == computer:
        return "Tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "User"
    else:
        return "Computer"

# Function to play tournament
def play_game():

    choices = ["rock", "paper", "scissors"]

    user_score = 0
    computer_score = 0
    round_number = 1

    history = []

    print("\n🎮 BEST OF 5 TOURNAMENT STARTED 🎮")

    while user_score < 3 and computer_score < 3:

        print(f"\n---------- Round {round_number} ----------")

        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            user_choice = "rock"
        elif choice == "2":
            user_choice = "paper"
        elif choice == "3":
            user_choice = "scissors"
        else:
            print("Invalid choice!")
            continue

        computer_choice = random.choice(choices)

        print("\nYour Choice:", user_choice)
        print("Computer Choice:", computer_choice)

        result = determine_winner(user_choice, computer_choice)

        if result == "User":
            print("🎉 You Win This Round!")
            user_score += 1

        elif result == "Computer":
            print("😢 Computer Wins This Round!")
            computer_score += 1

        else:
            print("🤝 Round Tied!")

        history.append(
            f"Round {round_number}: You={user_choice} | Computer={computer_choice} | Result={result}"
        )

        print("\n📊 Current Score")
        print("You      :", user_score)
        print("Computer :", computer_score)

        round_number += 1

    print("\n==============================")
    print("🏁 TOURNAMENT FINISHED")
    print("==============================")

    if user_score > computer_score:
        print("🏆 Congratulations! You Won The Tournament!")
    else:
        print("💻 Computer Won The Tournament!")

    print("\n📜 MATCH HISTORY")
    print("------------------------------")

    for item in history:
        print(item)

    print("\n📈 FINAL STATISTICS")
    print("Total Rounds :", round_number - 1)
    print("Your Score   :", user_score)
    print("Computer     :", computer_score)

# Main Menu
while True:

    print("\n==============================")
    print(" ROCK PAPER SCISSORS ")
    print("==============================")
    print("1. Play Tournament")
    print("2. View Rules")
    print("3. Exit")

    option = input("Enter option: ")

    if option == "1":
        play_game()

    elif option == "2":
        show_rules()

    elif option == "3":
        print("\nThank You For Playing!")
        break

    else:
        print("\nInvalid Option!")