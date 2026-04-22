class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def pattern(word):
            res = []
            n = len(word)
            for i in range(n):
                for j in range(i,n):
                    w = list(word)
                    w[i] = "*"
                    w[j] = "*"
                    res.append("".join(w))
            return res
                    
        pm = set()
        for word in dictionary:
            for p in pattern(word):
                pm.add(p)
        
        res =[]
        for word in queries:
            # for p in pattern(word):
                # if p in pm:
                #     res.append(word)
                #     break
            if any(p in pm for p in pattern(word)):   # short circuits on first hit
                res.append(word)

        return res
        