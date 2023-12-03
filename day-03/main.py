#!/bin/python
import re
from copy import deepcopy


def getNeighbours(numbers, x, y):
    valid = []
    found = []
    # we want to search the next line, so the stop value for range must be +2
    for searchY in range(y-1, y+2):
        if searchY >= 0:
            for searchX in range(x-1,x+2):
                for num, location in numbers[searchY]:
                    if searchX in range(location[0],location[1]):
                        if (num,location) not in found:
                            found.append( (num,location) )
                            valid.append(int(num))
                            break

    return valid





def main():
    '''

    '''
    with open('.//day-03//input//data.txt') as f:
        raw_input = f.read()


    # load grid
    # search for any non '.' characters
    # check the neighbors for a digit
    # isolate the whole number
    numbers = []
    significantCharacters = []
    y = 0
    for line in raw_input.split('\n'):
        x = []
        for match in re.finditer(r'\d+', line):
            x.append( (match.group(), match.span()) )
#            print(f"Line {y}: found {match.group()}")
        numbers.append( deepcopy(x))
        x.clear()

        x= []
        for match in re.finditer(r'[^\d\.]', line):
            x.append( (match.group(), match.start()) )
#            print(f"Line {y}: Found character at {match.start()}")

        significantCharacters.append( deepcopy(x))
        x.clear()
        y += 1


    
    sigNum = []
    for y in range(0,len(significantCharacters)):
        for _, x in significantCharacters[y]:
           sigNum.extend(getNeighbours(numbers, x, y) )
            
    print(f"Sum of part numbers: {sum(sigNum)}")

    ratios = []
    temp = []
    for y in range(0,len(significantCharacters)):
        for _, x in significantCharacters[y]:
           if _ == '*':
                temp = getNeighbours(numbers, x, y)
                if len(temp) == 2:
                    ratios.append( temp[0] * temp[1] )

    print(f"Part 2: Sum of the ratios of the pairs is {sum(ratios)}")

    print("End of Line")
    return

if __name__ == "__main__":
    main()