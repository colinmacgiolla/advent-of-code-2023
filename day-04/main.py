#!/bin/python

import re
from collections import defaultdict

def main():
    '''

    '''
    with open('.//day-04//input//data.txt') as f:
        raw_input = f.read()

    data = []
    for line in raw_input.split('\n'):
        cardId = re.search(r'\d+', line.split(':')[0]).group()
        numbers = line.split(':')[1]
        winning = numbers.split('|')[0].split()
        draw = line.split('|')[1].split()

        data.append((int(cardId), winning, draw))

    winners = []
    datastore = {}
    for game in data:
        winCtr = len(set.intersection( set(game[1]), set(game[2]) ) )
        datastore[game[0]] = int(winCtr)
        if winCtr > 0:
            if winCtr == 1:
                winners.append(winCtr)
            else:
                winners.append( 2 ** (winCtr-1) )

    print(f"Part 1: Number of winning cards: {sum(winners)}")

    counter = defaultdict(int)

    for entry in datastore:
        counter[entry] += 1
        for x in range(datastore[entry]):
            counter[entry + x + 1] += counter[entry]

            
    print(f"Part 2: Total sum is: {sum(counter.values())}")

if __name__ == "__main__":
    main()
