class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Questions:
        #  char in order unique and sorted in custom order
        #  can char in s appear more than once?
        #  do char not in order need to any order?

        # Approach:
        #  sort using comparator keyed to index in order - O(nlogn), O(n)
        #  rank = {c: i for i, c in enumerate(order)}
        #  return ''.join(sorted(s, key=lambda c: rank.get(c, len(order))))
        # 
        # Optimal: Hashmap (count of S) + iterate over order
        #  count all the char in s
        #  iterate over order and build res from char in ch*count_s[ch]
        #  add remaining char of s in res with ch*count

        count_s = Counter(s)                # Count all the char in s
        # res = []
        res = ""
        for ch in order:                    # Iterate over char in order
            if ch in s:                     # add ch if it is in s
                # res.append(ch*count_s[ch])  # add char with count in res
                res += ch * count_s[ch]
                del count_s[ch]             # delete count of ch from count_s
        for ch, count in count_s.items():   # process all the remaining chars
            # res.append(ch*count)
            res+= ch*count
        # return "".join(res)                 # join and return
        return res