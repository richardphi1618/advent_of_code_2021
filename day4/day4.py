import copy

class Bingo_Game:
    """Represents the game of bingo"""

    raw_data: list[str]
    number_drawings: list[int]
    num_of_boards: int
    boards_str: list[list[str]]
    boards_int: list[list[list[int]]]
    boards_matches: list[list[list[bool]]]
    game_over : bool
    turn : int
    winning_board : int
    board_turn_is_winner: list[int]

    def __init__(self) -> None:
        self.raw_data = []
        self.number_drawings = []
        self.num_of_boards = 0
        self.boards_str = []
        self.boards_matches = [[[]]]
        self.game_over = False
        self.turn = 0

    def build_game(self, filename:str) -> None:
        
        self.raw_data = load_file(filename)

        self.number_drawings = list(map(int, self.raw_data[0].split(",")))  
        self.num_of_boards = int((len(self.raw_data)-1)/6)
        self.turn_boards_are_winners = [0 for x in range(self.num_of_boards)] 

        self.boards_str = []
        
        for i in self.raw_data[2::]:
            if i != '':
                self.boards_str += [i]

        self.boards_int = [[[-1 for col in range(5)] for row in range(5)] for board in range(self.num_of_boards)]

        row_num = 0

        for board_num in range(0,self.num_of_boards):
            for board_row in range(0,5):
                row_of_interest = self.boards_str[row_num].split(" ")
                while '' in row_of_interest : row_of_interest.remove('')
                row_of_interest = list(map(int, row_of_interest))
                self.boards_int[board_num][board_row] = copy.deepcopy(row_of_interest)
                row_num += 1

        self.boards_matches = [[[False for col in range(5)] for row in range(5)] for board in range(self.num_of_boards)]


    def find_matches (self, drawn_number: int) -> None:
        #print(f"This round drawn number:{drawn_number} ")
        for board_dx, board in enumerate(self.boards_int):
            for row_dx, row in enumerate(board):
                for column_dx, item in enumerate(row): #item can double as column
                    if drawn_number == item:
                        self.boards_matches[board_dx][row_dx][column_dx] = True        
        return None
    
    def check_for_winner (self, verbose = True) -> None:
        self.turn += 1

        #check rows
        for board_dx, board in enumerate(self.boards_matches):
            for row_dx, row in enumerate(board):
                if all(self.boards_matches[board_dx][row_dx]):
                    self.winning_board = board_dx + 1
                    self.winning_row = self.boards_int[board_dx][row_dx]
                    self.game_over = True
        
        #check columns
        for board_dx, board in enumerate(self.boards_matches):
            for col in range(0,5):
                column_of_interest_matches = [board[0][col], board[1][col], board [2][col], board [3][col], board [4][col]]
                if all(column_of_interest_matches):
                    self.winning_board = board_dx + 1
                    column_of_interest = []
                    
                    for i in self.boards_int[board_dx]:
                        column_of_interest += [i[col]]

                    self.winning_row = column_of_interest
                    self.game_over = True

        return None
        
def sum_unmatched(board_items: list, board_matches: list) -> int:
    val = 0
    
    for row_dx, row in enumerate(board_items):
        for col_dx, item in enumerate(row):
            if board_matches[row_dx][col_dx] == False:
                val += item

    return val


def load_file(filename:str) -> list:
    my_file = open(filename, 'r')
    content = my_file.read()
    output = content.split("\n")
    my_file.close()  

    return output

def part1 (filename:str) -> None:
    part1 = Bingo_Game()
    part1.build_game(filename)

    for i in part1.number_drawings:
        part1.find_matches(i)
        part1.check_for_winner()
        if part1.game_over: break

    print(f"Game Over!!! \nTurn Num. {part1.turn}")
    print(f"Winning board is:{part1.winning_board} \nWinning row: {part1.winning_row}")

    unmatached_sum = sum_unmatched(part1.boards_int[part1.winning_board-1], part1.boards_matches[part1.winning_board-1])

    print(f"\nunmatched sum: {unmatached_sum}")
    print(f"winning drawing: {part1.number_drawings[part1.turn-1]}")

    print(f"\nanswer: {unmatached_sum*part1.number_drawings[part1.turn-1]}")
    return None

def part2(filename:str) -> None:
    part2 = Bingo_Game()
    part2.build_game(filename)

    winning_boards_matches = []
    winning_boards = []
    
    for i in part2.number_drawings:
        part2.find_matches(i)
        part2.check_for_winner()
        if part2.game_over and len(part2.boards_int) != 1:
            winning_boards_matches += copy.deepcopy([part2.boards_matches[part2.winning_board-1]])
            winning_boards += copy.deepcopy([part2.boards_int[part2.winning_board-1]])
            part2.boards_matches.remove(part2.boards_matches[part2.winning_board-1])
            part2.boards_int.remove(part2.boards_int[part2.winning_board-1])
            part2.game_over = False
        
        if part2.game_over and len(part2.boards_int) == 1: 
            break
    

    unmatached_sum = sum_unmatched(winning_boards[-1], winning_boards_matches[-1])

    print(f"Game Over!!! \nTurn Num. {part2.turn}")
    print(f"Winning board is:{part2.winning_board} \nWinning row: {part2.winning_row}")

    print(f"\nunmatched sum: {unmatached_sum}")
    print(f"winning drawing: {part2.number_drawings[part2.turn-1]}")

    print(f"\nanswer: {unmatached_sum*part2.number_drawings[part2.turn-1]}")

    return None

if __name__ == '__main__':
    print("---------- Part 1 ----------")
    part1('day4/sampleset.txt')
    print("---------- Part 2 ----------")
    part2('day4/sampleset.txt')
    