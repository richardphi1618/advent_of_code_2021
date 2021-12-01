from typing import Dict
import csv

depth_test = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

def check_increase (input:list) -> Dict:
    output = {}
    output["raw_data"] = input
    output["observation"] = ["N/A - no previous measurement"]
    output["num_of_inc"] = 0 
    output["num_of_dec"] = 0

    for idx, i in enumerate(input[1::]):
        if i < input[idx]:
            output["observation"] += ['decreased']
            output["num_of_dec"] += 1
        elif i > input[idx]:
            output["observation"] += ['increased']
            output["num_of_inc"] += 1
        else :
            output["observation"] += ['no change']
    
    return output


if __name__ == '__main__':
    

    with open('day1/Book1.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)


    #results = check_increase(depth_test)
    results = check_increase(data)

    for idx, i in enumerate(results["raw_data"]):
        observation = results["observation"][idx]
        print (f"{i} ( {observation} )")

    print("num of decreases: " + str(results["num_of_dec"]))
    print("num of increases: " + str(results["num_of_inc"]))

    