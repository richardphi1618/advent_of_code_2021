from typing import Dict

depth_test = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

def check_increased (input:list[int]) -> Dict:
    output = {}
    output["raw_data"] = input
    output["observation"] = ["N/A - no previous measurement"]
    output["windows"] = []
    output["num_of_inc"] = 0 
    output["num_of_dec"] = 0
    output["num_of_no_change"] = 0

    for idx, i in enumerate(input[1::]):
        compared = int(input[idx+1]) - int(input[idx])
        if compared < 0:
            output["observation"] += ['decreased']
            output["num_of_dec"] += 1
        elif compared > 0:
            output["observation"] += ['increased']
            output["num_of_inc"] += 1
        else :
            output["observation"] += ['no change']
            output["num_of_no_change"] += 1
    
    return output

def check_increased_windows (input:list[int]) -> Dict:
    output = {}
    output["raw_data"] = input
    output['windows'] = []

    for idx, i in enumerate(input[:-2:]):
        output['windows'] += [input[idx] + input[idx+1] + input[idx+2]]
    
    output = check_increased (output['windows'])

    return output


if __name__ == '__main__':

    my_file = open('day1/sampleset.txt', 'r')
    content = my_file.read()
    data = content.split("\n")
    my_file.close()
    data = [int(i) for i in data]

    #data = depth_test

    print("using simple method")
    results = check_increased(data)
    print("num of increases: " + str(results["num_of_inc"]))

    print("using windows method")
    results = check_increased_windows(data)
    print("num of increases: " + str(results["num_of_inc"]))

    