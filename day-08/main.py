#!/bin/python
import re

def main():
    '''
    LLR

    AAA = (BBB, BBB)
    BBB = (AAA, ZZZ)
    ZZZ = (ZZZ, ZZZ)
    '''
    with open('.//day-08//input//data.txt') as f:
        raw_input = f.read()
    input = raw_input.split('\n')    
    
    directions = input[0]
    myMap = {}
    
    for line in input[2::]:
        myMap[ line.split("=")[0].strip() ] =   tuple(re.findall('[A-Z]+', line.split("=")[1]))
    
    instruction = 0
    location = "AAA"
    while location != "ZZZ":
        if directions[instruction%len(directions)] == 'L':
            location = myMap[location][0]
        else:
            location = myMap[location][1]
        instruction += 1
        
    print(f"Part 1: Number of steps is: {instruction}")
        
    print("End of line")
        
if __name__ == "__main__":
    main()