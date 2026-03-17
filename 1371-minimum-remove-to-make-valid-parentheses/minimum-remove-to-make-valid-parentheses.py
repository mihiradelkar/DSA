class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove = set()
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                if stack:
                    stack.pop()
                else:
                    remove.add(i)
        remove |= set(stack)
        return "".join([ch for i, ch in enumerate(s) if i not in remove])

















        # questions:
        # can the string be empty?
        # can it have all valid parentheses/no parentheses?
        # all umatched "(((" or ")))" return ""
        # just round brackets?
        
        #edge cases:
        # "" => ""
        # "abc" => "abc"
        # all char or "(" or ")"
        
        # approach
        # stack with index []
        # remove stack with index to remove -> set()
        # algo:
        # push "(" index to stack
        # pop on ")" is stack not empty
        # if stack empty add to remove set
        # merge remaing index in stack with remove set

        stack = []
        remove = set()
        for i, ch in enumerate(s):
        	if ch == "(":
        		stack.append(i)
        	elif ch == ")":
        		if stack:
        			stack.pop()
        		else:
        			remove.add(i)
        
        remove |= set(stack)  # union 
        # for i in stack:     # same
        # 	remove.add(i)
        
        return "".join(ch for i, ch in enumerate(s) if i not in remove) # in one line
        res = ""                                                        # same
        for i, ch in enumerate(s):
        	if i not in remove:
        		res+=ch
        return res

# O(1) space
    def minRemoveToMakeValid(self, s: str) -> str:

        open = close = 0

        for c in s:
            if c == "(":
                open += 1
            elif c == ")":
                if open:
                    open -= 1
                else:
                    close += 1

        s = s.replace(")", "", close)
        s = s[::-1]
        s = s.replace("(", "", open)

        return s[::-1]
        
# all type
        stack = []       # stores (char, index) of unmatched openers
        to_remove = set()       
        
        matching = {')': '(', '}': '{', ']': '['}
        
        openers = set('({[')        
        
        for i, ch in enumerate(s):
            if ch in openers:
                stack.append((ch, i))
            elif ch in matching:
                if stack and stack[-1][0] == matching[ch]:
                    stack.pop()              # matched pair
                else:
                    to_remove.add(i)         # unmatched closer     
        
        # remaining in stack are unmatched openers
        to_remove |= {i for _, i in stack}      
        
        return ''.join(ch for i, ch in enumerate(s) if i not in to_remove)
        