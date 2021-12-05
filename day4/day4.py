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
        print(f"This round drawn number:{drawn_number} ")
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

        if verbose:
            if self.game_over:
                print(f"Game Over!!! \nTurn Num. {self.turn}\nWinning is board:{self.winning_board} \nWinning row: {self.winning_row}")
            else:
                print(f"Game continues... \n Turn Num. {self.turn}")
        
        return None
        
    def sum_unmatched(self) -> int:
        val = 0

        winning_board = self.boards_int[self.winning_board-1]
        
        for row_dx, row in enumerate(winning_board):
            for col_dx, item in enumerate(row):
                if self.boards_matches[self.winning_board-1][row_dx][col_dx] == False:
                    val += item

        return val


def load_file(filename:str) -> list:
    my_file = open(filename, 'r')
    content = my_file.read()
    output = content.split("\n")
    my_file.close()  

    return output

def part1 (input:dict) -> None:
    #print(input)
    part1 = Bingo_Game()
    part1.build_game('day4/sampleset.txt')

    for i in part1.number_drawings:
        part1.find_matches(i)
        part1.check_for_winner()
        if part1.game_over: break
    
    unmatached_sum = part1.sum_unmatched()

    print(f"unmatched sum: {unmatached_sum}")
    print(f"winning drawing: {part1.number_drawings[part1.turn-1]}")

    print(f"\nanswer: {unmatached_sum*part1.number_drawings[part1.turn-1]}")
    return None

if __name__ == '__main__':
    data = load_file('day4/sampleset_ex.txt')

    print("---------- Part 1 ----------")
    part1(data)
    print("---------- Part 2 ----------")
    #part2(data)
    