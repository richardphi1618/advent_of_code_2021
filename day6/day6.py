import copy

def load_file(filename:str) -> list:
    my_file = open(filename, 'r')
    content = my_file.read()
    output = content.split(",")
    my_file.close()  

    for i in range(0, len(output)):
        output[i] = int(output[i])
    
    return output

def simulation(input: list[int], number_of_days: int) -> list[int]:
    output = input[:]
    day_num = 0

    for x in range(0, number_of_days):
        day_num += 1

        for idx, i in enumerate(output):
            if i <= 0:
                output[idx] = 6
                output.append(9)
            else:
                output[idx] -= 1
        
        #print (f'After  {day_num} day:  {output}')
    
    print (f'Answer: {len(output)}')
    return output

def part1(filename:str) -> object:
    initial_values = copy.deepcopy(load_file(filename))
    number_of_days = 80
    simulation(initial_values, number_of_days)

    return part1

def part2(filename:str) -> None:
    return None

if __name__ == '__main__':
    print("---------- Part 1 ----------")
    part1('day6/sampleset.txt')
    print("---------- Part 2 ----------")
    part2('day6/sampleset_ex.txt')