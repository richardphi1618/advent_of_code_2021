import copy

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

def part1(input:list[list[int]], suppress = True) -> dict: 
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
            epsilon_rate[xdx] = 0
        elif x < len(input)/2:
            gamma_rate[xdx] = 0
            epsilon_rate[xdx] = 1
        else:
            gamma_rate[xdx] = 1
            epsilon_rate[xdx] = 0            

    if suppress is False:
        print(f"raw: {gamma_rate} | int: {binary_list_to_int(gamma_rate)}")
        print(f"raw: {gamma_rate} | int: {binary_list_to_int(epsilon_rate)}")
        print(f"solution {binary_list_to_int(gamma_rate)*binary_list_to_int(epsilon_rate)}")

    result = {}
    result["raw_data"] = input
    result["gamma_rate"] = gamma_rate
    result["epsilon_rate"] = epsilon_rate

    return result

def filter (input: list[list[int]], rating) ->  list[int]:
    working_list = copy.deepcopy(input)
    bit_position = 0

    while bit_position < len(input[0]) and len(working_list) > 1:
        items_to_delete = [False]*len(working_list)
        part1_result = part1(working_list)

        
        for idx,i in enumerate(working_list):
            if rating is "life support":
                if i[bit_position] is not part1_result['gamma_rate'][bit_position]:
                    items_to_delete[idx] = True
            elif rating is "CO2 scrubber":
                if i[bit_position] is not part1_result['epsilon_rate'][bit_position]:
                    items_to_delete[idx] = True

        for jdx, j in enumerate(reversed(items_to_delete)):       
            if j:
                del working_list[len(items_to_delete)-1-jdx]   

        bit_position += 1
    
    return working_list[0]

def part2(input:list[list[int]]) -> None: 
    
    life_support_rating = filter(input, "life support")
    print(life_support_rating)
    print(binary_list_to_int(life_support_rating))

    CO2_scrubber_rating = filter(input, "CO2 scrubber")
    print(CO2_scrubber_rating)
    print(binary_list_to_int(CO2_scrubber_rating))

    print(f"solution {binary_list_to_int(life_support_rating)*binary_list_to_int(CO2_scrubber_rating)}")
    
    return None


if __name__ == '__main__':

    data = load_file('day3/sampleset.txt')

    print("---------- Part 1 ----------")
    part1(data, False)
    print("---------- Part 2 ----------")
    part2(data)