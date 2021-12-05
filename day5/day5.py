def load_file(filename:str) -> list:
    my_file = open(filename, 'r')
    content = my_file.read()
    output = content.split("\n")
    my_file.close()  

    return output

class data_map():
    '''Builds the data map for day 5'''
    raw_data: list[list[str]] #raw data loaded
    start_positions: list[tuple]
    end_positions: list[tuple]
    max_position : list
    board : list[list]

    def __init__(self) -> None:
        self.raw_data = []
        self.start_positions = []
        self.end_positions = []
        self.max_position = [0,0]
        return None

    def build(self, filename:str) -> None:
        temp_load = load_file(filename)
        for i in temp_load:
            self.raw_data += [list(i)]

        for j in self.raw_data:
            self.start_positions += [(int(j[0]),int(j[2]))]
            self.end_positions += [(int(j[-3]),int(j[-1]))]

        for x in (self.start_positions + self.end_positions):
            if x[0] > self.max_position[0]:
                self.max_position[0] = x[0]
            if x[1] > self.max_position[1]:
                self.max_position[1] = x[1]

        self.board = [[0 for col in range(self.max_position[0])] for row in range(self.max_position[1])]

        return None

def part1(filename:str) -> None:
    part1 = data_map()
    part1.build(filename)
    return None

def part2() -> None:

    return None

if __name__ == '__main__':
    print("---------- Part 1 ----------")
    part1('day5/sampleset_ex.txt')
    print("---------- Part 2 ----------")
    #part2('day5/sampleset.txt')