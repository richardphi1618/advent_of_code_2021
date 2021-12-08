def load_file(filename:str) -> list:
    my_file = open(filename, 'r')
    content = my_file.read()
    temp = content.split('\n')
    output =[]
    output.extend([i.split('|') for i in temp])
    my_file.close()  

    return output

def part1(filename:str) -> object:
    data = load_file(filename)
    count = 0

    for i in data:
        temp = i[1].split(' ')
        for t in temp:
            if len(t) in [2, 3, 4, 7]: count += 1 #looking if number is 1, 7, 4, and 8 respectively

    print(count)
    return None

def part2(filename:str) -> None:
    data = load_file(filename)

    print(data)
    return None

if __name__ == '__main__':
    print("---------- Part 1 ----------")
    part1('day8/sampleset.txt')
    print("---------- Part 2 ----------")
    #part2('day8/sampleset.txt')