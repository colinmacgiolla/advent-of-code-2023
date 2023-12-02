#!/bin/python
from copy import deepcopy
from operator import mul
from functools import reduce


def parse_line(line):
    
    game_id, games = line.split(':')
    game_id = game_id.split()[1]
    
    round_list = []
    for entry in games.split(';'):
        
        round = {}
        
        for record in entry.split(','):
            v,k = record.split()
            round[k] = int(v)
        round_list.append( deepcopy(round) )
        
    return game_id,round_list
        
       
        
    
def main():
    '''

    '''
    with open('.//day-02//input//data.txt') as f:
        raw_input = f.read()
        
    data = {}
    for line in raw_input.split('\n'):
        k,v = parse_line(line)
        data[k] = v
    
    bad_games = []
    good_games = []
    checkList = [('red',12),('green',13),('blue',14)]

        
    for game in data:
        for round in data[game]:
            for k,v in checkList:
                if k in round:
                    if round[k] > v:
                        bad_games.append(int(game))
        if int(game) not in bad_games:
            good_games.append(int(game))
    
    print(f"Part 1: Sum of good game IDs: {sum(good_games)}")
    print(f"Sum of bad game IDs: {sum(bad_games)}")
    
    minimum = {}
    totals = []
    for game in data:
        minimum['red'] = 0
        minimum['green'] = 0
        minimum['blue'] = 0
        
        for round in data[game]:
            for k in round.keys():
                if minimum[k] < round[k]:
                    minimum[k] = round[k]
        
        power = reduce(mul, minimum.values(), 1)
        totals.append( power)
        
    print(f"Part 2: The Sum of the powers is: {sum(totals)}")
            
        
    print("End of Line")






if __name__ == "__main__":
    main()