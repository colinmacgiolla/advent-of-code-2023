#!/bin/python

from collections import Counter
from functools import total_ordering

@total_ordering
class Hand():
    def __init__(self, input) -> None:
        self.hand, bid = input.split()
        #self.strength = enumerate( list(range(2,10)).extend( ['T','J','Q','K','A'] ) )
        self.joker = False
        if 'J' in self.hand:
            self.joker = True
        self.bid = int(bid)
        self._calculateType()
        
    def __repr__(self):
        return self.hand
    
    def __lt__(self, other):
        if self.type != other.type:
            return self.type < other.type
        
        for a,b in zip(self.hand, other.hand):
            if a == b:
                continue
            if a.isdigit() and b.isdigit():
                return int(a) < int(b)
            if a.isdigit() or b.isdigit():
                return a.isdigit()
            for card in ['T','J','Q','K','A']:
                if a == card or b == card:
                    return a == card
        return False
                
        
        
    def _calculateType(self):
        type = 0
        counts = Counter(self.hand).most_common()
        
        if self.hand == "Q2Q2Q":
            print("stop")
        
        if counts[0][1] == 5:
            type = 6
        elif counts[0][1] == 4:
            type = 5
        elif counts[0][1] == 3:
            if counts[1][1] == 2:
                # full house
                type = 4
            else:
                type = 3
        elif counts[0][1] == counts[1][1] == 2:
            # 2 pairs
            type = 2
        elif counts[0][1] == 2:
            # 1 pair
            type = 1
        else:
            # high card
            type = 0
            
        self.type = type
            
            


def main():
    '''

    '''
    with open('.//day-07//input//data.txt') as f:
        raw_input = f.read()
        
    deck = sorted([ Hand(line) for line in raw_input.split('\n') ])
    value = sum( [ ((rank+1) * hand.bid) for rank, hand in enumerate(deck) ] )
    
    

    
    print(f"Solution for Part 1: {value}")
    
    print("End of line")
        
if __name__ == "__main__":
    main()