
def load_file(filename:str) -> list[str]:
    my_file = open(filename, 'r')
    content = my_file.read()
    data = content.split("\n")
    my_file.close()

    return data


if __name__ == '__main__':
    data = load_file('day2/sampleset.txt')
    
    depth = 0
    horizontal_position = 0

    for i in data:
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