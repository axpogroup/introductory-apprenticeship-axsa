win_condition = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)
]
def game_board(board):
    print("-------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("-------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("-------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("-------------")

def gameplay():
    print("Welcome to Tic Tac Toe!")
    print("Player 1: X")
    print("Player 2: O")
    print("Enter the position (1-9) to place your mark:")

def get_user_input():
    placed_mark_str = input("Enter position (1-9): ")
    return placed_mark_str

def check_winner(board):
    for a,b,c in win_condition:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    return None


def rematch():
    answer = input("Do you want to play again? (yes/no): ")
    if answer.lower() == "yes":
        return [" "] * 9
    else:
        print("Thanks for playing!")
        quit()

def input_validation(placed_mark_str, board):
    while True:
        game_turn = board.count("X") + board.count("O")
        current_player = "X"
        if placed_mark_str in "123456789" and len(placed_mark_str) == 1:

            if board[int(placed_mark_str) - 1] != " ":
                print("Position already taken. Please choose another position.")
                placed_mark_str = get_user_input()
                continue

            placed_mark = int(placed_mark_str) - 1

            if board.count("X") > board.count("O"):
                current_player = "O"

            board[placed_mark] = current_player
            game_board(board)
            winner = check_winner(board)
            if winner:
                print(f"Game Over! Player {winner} wins!")
                return rematch()


            if game_turn == 8:
                print("Game Over! It's a tie!")
                return rematch()

            return board
        else:
            print("Invalid input. Please enter a number between 1 and 9")

        placed_mark_str = get_user_input()



def tic_tac_toe():
    board = [" "] * 9
    gameplay()
    game_board(board)

    while True:
        placed_mark_str = get_user_input()
        board = input_validation(placed_mark_str, board)




if __name__ == "__main__":
    tic_tac_toe()
