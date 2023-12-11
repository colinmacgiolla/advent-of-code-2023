#!/bin/python
from itertools import pairwise


def allEqual(iterable):
    iterator = iter(iterable)
    
    try:
        firstItem = next(iterator)
    except StopIteration:
        return True
        
    for x in iterator:
        if x!=firstItem:
            return False
    return True


def calculate_sequence(data):
    prediction = data[-1]
    
    while data:
        if allEqual(data):
            break
        data = [ current - previous for previous, current in pairwise(data) ]
        prediction += data[-1]
    return prediction
    



def main():
    '''

    '''
    with open('.//day-09//input//data.txt') as f:
        raw_input = f.read()
        
    data = []
    for line in raw_input.split('\n'):
        data.append( [int(i) for i in line.split()] )
        
    print(f"Part 1: {sum(map(calculate_sequence, data))}")
    
    # num[::-1] would have been easier then list(reversed(num))
    print(f"Part 2: {sum( calculate_sequence( list(reversed(num))) for num in data )}")
    
    print("End of line")
        
if __name__ == "__main__":
    main()