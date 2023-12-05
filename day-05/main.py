#!/bin/python

import re
from copy import deepcopy
import bisect


def parse_file(raw_input):
    seeds = []
    maps = []
    temp_map = []

    for line in raw_input.split('\n'):
        if "seeds:" in line:
            seeds = [int(i) for i in line.split(':')[1].split()]
        elif len(line) == 0:
            pass
        elif "map" in line:
            if len(temp_map) != 0:
                maps.append(deepcopy(temp_map))
                temp_map.clear()
        else:
            temp_map.append([int(i) for i in re.findall(r'\d+', line)])
    maps.append(deepcopy(temp_map))
    
    return seeds, maps

def process_map( value, map ):
    # map entry = (destinationRangeStart, sourceRangeStart, rangeLength)


    for dest, src, numRange in map:
        if src <= value <= src + numRange:
            seed = dest + (value - src)
            return seed
    return value
    

def main():
    with open('.//day-05//input//data.txt') as f:
        raw_input = f.read()

    seeds, maps = parse_file(raw_input)

    locations = []
    for seed in seeds:
        answer = deepcopy(seed)
        for map in maps:
            #print(f"{seed}: Current stage value: {answer}")
            answer = process_map(answer, map)
            
        #print(f"Seed {seed} maps to {answer}")
        locations.append(answer)

    print(f"Part 1: Minimum location value: {min(locations)}")

    print("End-of-Line")

    return

if __name__ == "__main__":
    main()
