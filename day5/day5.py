from types import MappingProxyType


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
    diag_start_positions: list[tuple]
    diag_end_positions: list[tuple]
    max_position : list
    board : list[list]
    directions : list[str]
    spaces : list[list[list[int]]]

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
            temp = ''.join(j)
            temp = temp.split(" ")
            for t in range(3):
                temp[t] = temp[t].split(',')

            self.start_positions += [(int(temp[0][0]),int(temp[0][1]))]
            self.end_positions += [(int(temp[2][0]),int(temp[2][1]))]

        for x in (self.start_positions + self.end_positions):
            if x[0] > self.max_position[0]:
                self.max_position[0] = x[0]
            if x[1] > self.max_position[1]:
                self.max_position[1] = x[1]

        self.board = [[0 for col in range(self.max_position[0]+1)] for row in range(self.max_position[1]+1)]
        return None

    def consider_only_straights(self) -> None:
        to_be_removed = []
        self.diag_start_positions = []
        self.diag_end_positions = []

        for i in range(len(self.start_positions)):
            if self.end_positions[i][0] != self.start_positions[i][0] and self.end_positions[i][1] != self.start_positions[i][1]:
                to_be_removed += [True]
            else:
                to_be_removed += [False]           

        for jdx, j in reversed(list(enumerate(to_be_removed))):
            if j:
                #print('removing: ' + ''.join(str(self.start_positions[jdx])) + ' and ' + ''.join(str(self.end_positions[jdx])))
                self.diag_start_positions.append(self.start_positions[jdx])
                self.diag_end_positions.append(self.end_positions[jdx])
                self.start_positions.remove(self.start_positions[jdx])
                self.end_positions.remove(self.end_positions[jdx])

        return None
    
    def calc_line_direction(self)->None:
        self.directions = []
        self.diag_directions = []

        for idx, i in enumerate(self.start_positions):
            if self.end_positions[idx][0] < i[0]:
                direction = 'left'
            elif self.end_positions[idx][0] > i[0]:
                direction = 'right'
            elif self.end_positions[idx][1] < i[1]:
                direction = 'down'
            elif self.end_positions[idx][1] > i[1]:
                direction = 'up'

            self.directions += [direction]

        for idx, i in enumerate(self.diag_start_positions):
            if self.diag_end_positions[idx][0] < i[0]:
                if self.diag_end_positions[idx][1] < i[1]:
                    direction = 'left down'
                elif self.diag_end_positions[idx][1] > i[1]:
                    direction = 'left up'
            elif self.diag_end_positions[idx][0] > i[0]:
                if self.diag_end_positions[idx][1] < i[1]:
                    direction = 'right down'
                elif self.diag_end_positions[idx][1] > i[1]:
                    direction = 'right up'
            

            self.diag_directions += [direction]
        return None

    def load_board(self) -> None:
        
        for x in self.spaces:
            for y in x:
                self.board[y[0]][y[1]] += 1
    
        return None
    
    def load_spaces_straights(self) -> None:
        self.spaces = []
        position = [0,0]

        self.spaces = [[] for line in range(len(self.start_positions))]

        for i in range(len(self.start_positions)):
            position = list(self.start_positions[i])
            self.spaces[i] += [list(self.start_positions[i])]

            while position != list(self.end_positions[i]):
                if self.directions[i] == 'left':
                    position[0] = position[0]-1
                if self.directions[i] == 'right':
                    position[0] = position[0]+1
                if self.directions[i] == 'up':
                    position[1] = position[1]+1
                if self.directions[i] == 'down':
                    position[1] = position[1]-1

                self.spaces[i].append(position[:])
    
        return None
    
    def load_spaces_diags(self) -> None:

        current_list_length = len(self.spaces) 
        extension = [[] for line in range(len(self.diag_start_positions))]
        self.spaces += extension

        for i in range(len(self.diag_start_positions)):
            position = list(self.diag_start_positions[i])
            self.spaces[i] += [list(self.diag_start_positions[i])]

            while position != list(self.diag_end_positions[i]):
                if self.diag_directions[i] == 'left up':
                    position[0] = position[0]-1
                    position[1] = position[1]+1
                if self.diag_directions[i] == 'right up':
                    position[0] = position[0]+1
                    position[1] = position[1]+1
                if self.diag_directions[i] == 'left down':
                    position[0] = position[0]-1
                    position[1] = position[1]-1
                if self.diag_directions[i] == 'right down':
                    position[0] = position[0]+1
                    position[1] = position[1]-1

                self.spaces[i+current_list_length].append(position[:])

        return None

    def find_largest(self) -> tuple:
        max_val = 0
        occurrence = 0

        for i in self.board:
            if max(i[1:]) > max_val:
                max_val = max(i[1:])
        
        for j in self.board:
            for k in range(2, max_val+1):
                occurrence += j.count(k)

        return (max_val, occurrence)

def part1(filename:str) -> object:
    part1 = data_map()
    part1.build(filename)
    part1.consider_only_straights()
    part1.calc_line_direction()
    part1.load_spaces_straights()
    part1.load_board()
    (val, occurrence) = part1.find_largest()

    print(f'Answer : {val} {occurrence}')
    return part1

def part2(filename:str) -> None:
    part2 = data_map()
    part2.build(filename)
    part2.consider_only_straights()
    part2.calc_line_direction()
    part2.load_spaces_straights()
    part2.load_spaces_diags()
    part2.load_board()

    (val, occurrence) = part2.find_largest()

    print(f'Answer : {val} {occurrence}')
    return None

if __name__ == '__main__':
    print("---------- Part 1 ----------")
    part1('day5/sampleset.txt')
    print("---------- Part 2 ----------")
    part2('day5/sampleset.txt')