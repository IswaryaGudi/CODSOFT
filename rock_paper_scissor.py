import random 
def display_instructions():
    print("\nWelcome to the game of Rock, Paper, Scissors!")
    print("Instructions for Rock-Paper-Scissor game are:")
    print("1. Choose 'rock', 'paper', or 'scissors'.")
    print("2. Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")
    print("3. The game will keep track of the score.")
    print("4. You can play multiple rounds!")
    print("5. Type 'exit' anytime to quit the game.") 
def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        elif user_choice == "exit":
            return "exit"
        else:
            print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.") 
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"]) 
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer" 
def main():
    user_score = 0
    computer_score = 0
    display_instructions() 
    while True:
        # Get the user's choice
        user_choice = get_user_choice()
        if user_choice == "exit":
            print("Thanks for playing! Final Score - You: {} | Computer: {}".format(user_score, computer_score))
            break 
        computer_choice = get_computer_choice()  
        print(f"\nYou chose: {user_choice}")
        print(f"The computer chose: {computer_choice}") 
        winner = determine_winner(user_choice, computer_choice) 
        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            user_score += 1
            print("You win this round!")
        else:
            computer_score += 1
            print("Computer wins this round!") 
        print(f"Score: You: {user_score} | Computer: {computer_score}") 
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Final Score - You: {} | Computer: {}".format(user_score, computer_score))
            break 
if __name__ == "__main__":
    main()
