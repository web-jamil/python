""" The rules of **Rock, Paper, Scissors** are simple and widely understood. Here’s a breakdown of how the game works:

---

### **Basic Rules**
1. **Game Setup**:
   - Two players face each other.
   - Each player chooses one of three options: **Rock**, **Paper**, or **Scissors**.

2. **Hand Signals**:
   - **Rock**: A closed fist.
   - **Paper**: An open hand with fingers extended.
   - **Scissors**: A fist with the index and middle fingers extended, forming a "V."

3. **Gameplay**:
   - Players count down (e.g., "Rock, Paper, Scissors, Shoot!") and simultaneously reveal their choices.
   - The winner is determined based on the rules below.


### **Winning Rules**
- **Rock beats Scissors**: Rock crushes scissors.
- **Scissors beats Paper**: Scissors cut paper.
- **Paper beats Rock**: Paper wraps rock.

If both players choose the same option, it's a **tie**, and the game is repeated.


### **Optional Variations**
1. **Best of Three**:
   - Players compete in multiple rounds, and the player who wins the majority of rounds is the overall winner.

2. **Score-Based**:
   - Assign points for each win (e.g., 1 point per round).
   - Play until a target score is reached (e.g., first to 3 points).

3. **Advanced Variants**:
   - Add more options like **Lizard** and **Spock** (as in "Rock, Paper, Scissors, Lizard, Spock"):
     - Rock crushes Scissors and Lizard.
     - Scissors cut Paper and decapitate Lizard.
     - Paper covers Rock and disproves Spock.
     - Lizard poisons Spock and eats Paper.
     - Spock smashes Scissors and vaporizes Rock.

### **Tips for Fair Play**
- Choices should be revealed simultaneously to avoid bias.
- Keep it fun and lighthearted—it's a game of chance with some room for psychological tactics! """


import random

def determine_winner(player_choice, computer_choice):
    winning_combinations = {
        "rock": ["scissors", "lizard"],
        "scissors": ["paper", "lizard"],
        "paper": ["rock", "spock"],
        "lizard": ["spock", "paper"],
        "spock": ["scissors", "rock"]
    }

    if player_choice == computer_choice:
        return "tie"
    elif computer_choice in winning_combinations[player_choice]:
        return "win"
    else:
        return "lose"

def play_game():
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
    print("Choices: rock, paper, scissors, lizard, spock")

    player_choice = input("Enter your choice: ").lower()
    while player_choice not in choices:
        print("Invalid choice. Please choose again.")
        player_choice = input("Enter your choice: ").lower()

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(player_choice, computer_choice)

    if result == "tie":
        print("It's a tie!")
    elif result == "win":
        print("You win!")
    else:
        print("You lose!")

# Play the game
if __name__ == "__main__":
    play_game()





def best_of_n():
    rounds = int(input("Best of how many rounds? "))
    player_score, computer_score = 0, 0

    while player_score < (rounds // 2 + 1) and computer_score < (rounds // 2 + 1):
        # Same game logic as above
        # Increment `player_score` or `computer_score` based on the winner

        print(f"Final Score - Player: {player_score}, Computer: {computer_score}")




import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    player = input("Enter rock, paper, or scissors: ").lower()
    computer = random.choice(choices)

    print(f"You chose: {player}")
    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        print("You win!")
    else:
        print("You lose!")

rock_paper_scissors()
