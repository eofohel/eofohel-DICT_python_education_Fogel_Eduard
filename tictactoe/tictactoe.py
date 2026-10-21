
cells = ["_"] * 9
current_player = "X"


def print_board():
    print("---------")
    for i in range(0, 9, 3):
        print("| " + " ".join(cells[i:i + 3]) + " |")
    print("---------")


def check_winner(player):
    lines = [
        cells[0:3], cells[3:6], cells[6:9],
        cells[0::3], cells[1::3], cells[2::3],
        cells[0::4], cells[2:7:2]
    ]
    return any(line == [player] * 3 for line in lines)


print_board()

while True:
    while True:
        coordinates = input("Enter the coordinates: ").split()

        if len(coordinates) != 2:
            print("You should enter numbers!")
            continue

        try:
            row, col = map(int, coordinates)
        except ValueError:
            print("You should enter numbers!")
            continue

        if not (1 <= row <= 3 and 1 <= col <= 3):
            print("Coordinates should be from 1 to 3!")
            continue

        index = (row - 1) * 3 + col - 1

        if cells[index] != "_":
            print("This cell is occupied! Choose another one!")
            continue

        cells[index] = current_player
        break

    print_board()

    if check_winner(current_player):
        print(f"{current_player} wins")
        break

    if "_" not in cells:
        print("Draw")
        break

    current_player = "0" if current_player == "X" else "X"
