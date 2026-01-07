import random


def monty_hall_game():
    doors = [1, 2, 3]
    car = random.choice(doors)

    print("Welcome to the Monty Hall Game!")
    print("There are 3 doors: 1, 2, and 3.")

    player = int(input("Choose a door (1, 2, or 3): "))

    # Host opens a door with a goat
    possible_opens = [d for d in doors if d != player and d != car]
    opened = random.choice(possible_opens)

    print(f"Monty opens door {opened}. It's a goat!")

    decision = input("Do you want to switch doors? (yes/no): ").lower()

    if decision == "yes":
        player = [d for d in doors if d != player and d != opened][0]
        print(f"You switched to door {player}.")
    else:
        print(f"You stayed with door {player}.")

    # Reveal result
    if player == car:
        print("🎉 You WIN! The car was behind your door.")
    else:
        print("🐐 You lose. The car was behind door", car)


if __name__ == "__main__":
    # Run the game
    monty_hall_game()
