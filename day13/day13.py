class data_map():
    '''Builds the data map for day 5'''
    raw_data: list[list[str]] #raw data loaded
    workspace: list[list]
    instructions: list[str]
    max_x: int
    max_y: int

    def __init__(self) -> None:
        self.raw_data = []
        self.raw_data_int = [int]
        self.instructions = []
        self.workspace = []
        self.max_x = 0 
        self.max_y = 0 
        return None

    def load_file(self, filename:str):
        my_file = open(filename, 'r')
        content = my_file.read()
        input = content.split('\n')
        self.raw_data.extend([i.split(',') for i in input])
        self.raw_data.remove([''])
        my_file.close() 

        for j in self.raw_data:
            if len(j) == 1:
                self.instructions += j[:]

        for k in self.instructions:
            self.raw_data.remove([k]) 

        for t in self.raw_data:
            if int(t[0]) >= self.max_x:
                self.max_x = int(t[0]) 
            if int(t[1]) >= self.max_y:
                self.max_y = int(t[1])   

        self.raw_data_int = [tuple(map(int, v)) for v in self.raw_data]

        self.workspace = [['.' for x in range(self.max_x+1)] for y in range(self.max_y+1)]

        for a in self.raw_data_int:
            self.workspace[a[1]][a[0]] = '#'


def part1(filename:str) -> object:
    part1 = data_map()
    part1.load_file(filename)
    
    return None

def part2(filename:str) -> None:
    part2 = data_map()
    part2.load_file(filename)

    return None

if __name__ == '__main__':
    print("---------- Part 1 ----------")
    part1('day13/sampleset_ex.txt')
    print("---------- Part 2 ----------")
    #part2('day13/sampleset.txt')