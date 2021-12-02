
def load_file(filename:str) -> list[str]:
    my_file = open(filename, 'r')
    content = my_file.read()
    data = content.split("\n")
    my_file.close()

    return data

def part1(input:list[str]) -> tuple[int, int]: 
    #Part 1
    depth = 0
    horizontal_position = 0
    for i in input:
        command = i.split(" ")
        if 'up' in i:
            depth -= int(command[1])
        elif 'down' in i:
            depth += int(command[1])
        elif 'forward' in i:
            horizontal_position += int(command[1])

    print (depth)
    print (horizontal_position)

    print (f'answer: {depth*horizontal_position}')

    return depth, horizontal_position

def part2(input:list[str]) -> tuple[int, int, int]: 
    #Part 1
    aim = 0
    depth = 0
    horizontal_position = 0
    for i in input:
        command = i.split(" ")
        if 'up' in i:
            aim -= int(command[1])
        elif 'down' in i:
            aim += int(command[1])
        elif 'forward' in i:
            horizontal_position += int(command[1])
            depth += aim * int(command[1])
    
    print (aim)
    print (depth)
    print (horizontal_position)

    print (f'answer: {depth*horizontal_position}')

    return aim, depth, horizontal_position


if __name__ == '__main__':
    data = load_file('day2/sampleset.txt')

    print("---------- Part 1 ----------")
    part1(data)
    print("---------- Part 2 ----------")
    part2(data)
    
