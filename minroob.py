import random
from collections import deque

# Game settings
ROWS = 8
COLS = 7
TOTAL_MINES = 15
WIN_THRESHOLD = 8  # 50% of 15 mines

# Console color codes
COLORS = {
    'red': '\033[91m',
    'blue': '\033[94m',
    'reset': '\033[0m'
}

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.score = 0

def get_cell_number(row, col):
    return (row-1)*COLS + col

def get_neighbors(row, col):
    neighbors = []
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)
    ]
    
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 1 <= nr <= ROWS and 1 <= nc <= COLS:
            neighbors.append((nr, nc))
    return neighbors

def create_board():
    all_cells = [(r,c) for r in range(1, ROWS+1) for c in range(1, COLS+1)]
    mines = random.sample(all_cells, TOTAL_MINES)
    
    board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    
    for (r,c) in mines:
        board[r-1][c-1] = 'M'
    
    for r in range(1, ROWS+1):
        for c in range(1, COLS+1):
            if board[r-1][c-1] != 'M':
                count = 0
                for (nr, nc) in get_neighbors(r, c):
                    if board[nr-1][nc-1] == 'M':
                        count += 1
                board[r-1][c-1] = count
    
    return board, mines

def print_board(board, revealed, mines_found):
    print("\n" + "="*(COLS*4))
    print("   " + "   ".join(str(i) for i in range(1, COLS+1)))
    for r in range(ROWS):
        print(f"{r+1:2}|", end="")
        for c in range(COLS):
            cell = board[r][c]
            if (r, c) in revealed:
                if cell == 'M':
                    color = 'red' if (r, c) in mines_found['red'] else 'blue'
                    print(f"{COLORS[color]} M{COLORS['reset']}", end='  ')
                else:
                    print(f' {cell} ', end='  ')
            else:
                print(' ■ ', end='  ')
        print()
    print("="*(COLS*4))

def play_game():
    player1 = Player(input("Player 1 name: "), 'red')
    player2 = Player(input("Player 2 name: "), 'blue')
    
    players = [player1, player2]
    current_player = 0
    board, mines = create_board()
    revealed = set()
    mines_found = {'red': set(), 'blue': set()}
    
    while True:
        print(f"\n{COLORS[players[current_player].color]}Current: {players[current_player].name} ({players[current_player].score} pts){COLORS['reset']}")
        print_board(board, revealed, mines_found)
        
        try:
            row = int(input("Enter row (1-8): "))
            col = int(input("Enter column (1-7): "))
            if not (1 <= row <= ROWS and 1 <= col <= COLS):
                raise ValueError
        except:
            print("Invalid input!")
            continue
            
        r_idx = row-1
        c_idx = col-1
        
        if (r_idx, c_idx) in revealed:
            print("Already revealed!")
            continue
            
        if board[r_idx][c_idx] == 'M':
            players[current_player].score += 1
            mines_found[players[current_player].color].add((r_idx, c_idx))
            revealed.add((r_idx, c_idx))
            print(f"{COLORS[players[current_player].color]}Mine found! Score: {players[current_player].score}{COLORS['reset']}")
            
            if players[current_player].score >= WIN_THRESHOLD:
                print(f"\n=== {players[current_player].name} reached {WIN_THRESHOLD} points and wins! ===")
                break
        else:
            queue = deque([(row, col)])
            while queue:
                current = queue.popleft()
                r, c = current
                r_idx = r-1
                c_idx = c-1
                if (r_idx, c_idx) in revealed:
                    continue
                revealed.add((r_idx, c_idx))
                if board[r_idx][c_idx] == 0:
                    for neighbor in get_neighbors(r, c):
                        queue.append(neighbor)
            current_player = 1 - current_player
        
        total_found = len(mines_found['red']) + len(mines_found['blue'])
        if total_found == TOTAL_MINES:
            print("\n=== All mines found! ===")
            if player1.score > player2.score:
                winner = player1
            elif player2.score > player1.score:
                winner = player2
            else:
                winner = None
            
            if winner:
                print(f"{COLORS[winner.color]}{winner.name} wins with {winner.score} points!{COLORS['reset']}")
            else:
                print("It's a tie!")
            break
    
    print("\n1. Restart Game\n2. Exit Game")
    while True:
        choice = input("Choose (1/2): ")
        if choice == '1':
            return True
        elif choice == '2':
            return False
        print("Invalid choice!")

if __name__ == "__main__":
    while True:
        if not play_game():
            print("Thanks for playing!")
            break
        print("\n" + "="*30 + " NEW GAME " + "="*30)