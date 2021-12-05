import copy

class Bingo_Game:
    """Represents the board that the game of tic-tac-toe is played on."""

    raw_data: list[str]
    number_drawings: list[int]
    num_of_boards: int
    boards_str: list[list[str]]
    boards_int: list[list[list[int]]]
    boards_matches: list[list[list[bool]]]

    def __init__(self) -> None:
        self.raw_data = []
        self.number_drawings = []
        self.num_of_boards = 0
        self.boards_str = [[]]
        self.boards_int = [[[]]] #[board_num][row][column]
        self.boards_matches = [[[]]]

    def build_game(self, filename:str) -> None:
        
        self.raw_data = load_file(filename)

        self.number_drawings = list(map(int, self.raw_data[0].split(",")))  
        self.num_of_boards = int((len(self.raw_data)-1)/6)

        self.boards_str = [[]]*self.num_of_boards
        board_num = 0

        for i in self.raw_data[2::]:
            if i != '':
                self.boards_str[board_num] += [i]
            else:
                board_num += 1

        self.boards_int = [[[]]*5]*self.num_of_boards

        for idx,x in enumerate(self.boards_int):
            for idy,y in enumerate(x):
                self.boards_int[idx][idy] = self.boards_str[idx][idy].split(" ") 
                while '' in self.boards_int[idx][idy] : self.boards_int[idx][idy].remove('')
                self.boards_int[idx][idy] = list(map(int, self.boards_int[idx][idy])) 

        self.boards_matches = [[[False]*5]*5]*self.num_of_boards


def load_file(filename:str) -> list:
    my_file = open(filename, 'r')
    content = my_file.read()
    output = content.split("\n")
    my_file.close()  

    return output

def part1 (input:dict) -> None:
    #print(input)
    part1 = Bingo_Game()
    part1.build_game('day4/sampleset_ex.txt')
    print(part1)
    return None

if __name__ == '__main__':
    data = load_file('day4/sampleset_ex.txt')

    print("---------- Part 1 ----------")
    part1(data)
    print("---------- Part 2 ----------")
    #part2(data)
    