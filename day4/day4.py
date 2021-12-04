import copy

def load_file(filename:str) -> dict:
    data = {}

    my_file = open(filename, 'r')
    content = my_file.read()
    data['raw_data'] = content.split("\n")
    my_file.close()

    data['number_drawings'] = list(map(int, data['raw_data'][0].split(",")))  
    data['num_of_boards'] = int((len(data['raw_data'])-1)/6)

    data['boards_str'] = [[]]*data['num_of_boards']
    board_num = 0

    for i in data['raw_data'][2::]:
        if i != '':
            data['boards_str'][board_num] += [i]
        else:
            board_num += 1

    data['boards_int'] = [[[]]*5]*data['num_of_boards']

    for idx,x in enumerate(data['boards_int']):
        for idy,y in enumerate(x):
            data['boards_int'][idx][idy] = data['boards_str'][idx][idy].split(" ") 
            while '' in data['boards_int'][idx][idy] : data['boards_int'][idx][idy].remove('')
            data['boards_int'][idx][idy] = list(map(int, data['boards_int'][idx][idy]))  

    return data

def part1 (input:dict) -> None:
    print(input)
    return None

if __name__ == '__main__':
    data = load_file('day4/sampleset_ex.txt')

    print("---------- Part 1 ----------")
    part1(data)
    print("---------- Part 2 ----------")
    #part2(data)
    