import random
import time

def roll_dice():
    print("Rolling the dice...")
    time.sleep(1)  # Just for fun, adds delay
    dice = random.randint(1, 6)
    print(f"You rolled a {dice}!")

def main():
    while True:
        input("Press Enter to roll the dice or type 'q' to quit: ")
        roll_dice()
        choice = input("Roll again? (Press Enter to continue, or 'q' to quit): ").lower()
        if choice == 'q':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()