class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:      # not in multiple will not form groups
            return False
        count = Counter(hand)           # freq to consume cards
        sorted_count = sorted(count)    # sort on keys to go in sequence
        for key in sorted_count:
            freq = count[key]
            if freq == 0:               # cards are consumed in a sequence
                continue
            for i in range(groupSize):  # check all the cards in sequence 
                if count[key+i]<freq:   # for a freq for first element all the consecutive element
                    return False        #  should have same or more freq else it will not form a group
                count[key+i]-=freq      # reduce the count of freq. some count can still have few cards left as 
        return True                     # they can be used in future sequence but first element must have > or = freq

        
        
        