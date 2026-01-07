import random

def simulate(n=10000):
    switch_wins = 0
    stay_wins = 0

    for i in range(n):
        doors = [0, 1, 2]
        car = random.choice(doors)
        player = random.choice(doors)

        # Which door is the host allowed to open?
        for d in doors:
            if d != player and d != car:
                host_opens = d
                break
        possible_opens = [host_opens]
        # Or with list comprehension
        #possible_opens = [d for d in doors if d != player and d != car]

        host = random.choice(possible_opens)
        if player == car:
            stay_wins += 1

        # Which are the remaining doors if the player switches?
        for d in doors:
            if d != player and d != host:
                remaining = d
                break

        # Or with list comprehension
        # remaining = [d for d in doors if d != player and d != host][0]
        if remaining == car:
            switch_wins += 1

    print("Stay win rate:", stay_wins / n)
    print("Switch win rate:", switch_wins / n)

if __name__ == "__main__":
    simulate()

