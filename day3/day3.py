def load_file(filename:str) -> list[list[int]]:
    my_file = open(filename, 'r')
    content = my_file.read()
    rows = content.split("\n")
    data =[]

    for i in rows:
        data += [list(i)]
    my_file.close()

    for idx, x in enumerate(data):
        data[idx] =list(map(int, x))

    return data


def binary_list_to_int(binary_list:list[int]) -> int:
    result = int("".join(str(i) for i in binary_list),2)
    return result

def part1(input:list[list[int]]) -> None: #tuple[int, int, int]: 
    #Part 1
    
    col_sum = [0] * len(input[0]) 
    gamma_rate = [0] * len(input[0])
    epsilon_rate = [0] * len(input[0])

    for idx, i in enumerate(input):
        for jdx,j in enumerate(i):
            col_sum[jdx] += j
    
    for xdx, x in enumerate(col_sum):
        if x > len(input)/2:
            gamma_rate[xdx] = 1
        else:
            gamma_rate[xdx] = 0

        if x < len(input)/2:
            epsilon_rate[xdx] = 1
        else:
            epsilon_rate[xdx] = 0

        

    print(binary_list_to_int(gamma_rate))
    print(binary_list_to_int(epsilon_rate))
    print(f"solution {binary_list_to_int(gamma_rate)*binary_list_to_int(epsilon_rate)}")

    return None


if __name__ == '__main__':
    data = load_file('day3/sampleset.txt')

    print("---------- Part 1 ----------")
    part1(data)
    print("---------- Part 2 ----------")
    #part2(data)