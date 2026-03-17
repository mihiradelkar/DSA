class Solution:
    def simplifyPath(self, path: str) -> str:
        # Questions:
        #  what all can path contain? . / _ a-zA-Z0-9
        #  can path have consecutive //?
        #  will result always start with /?

        # Approach:
        #  Brute Force: process each char with condition and pop till / if ..   (n,n)
        #  Optimal: Stack with split by /  .,"" skip .. pop else add. res = / join stack (n, n)
        
        # /home/user/Documents/../Pictures
        # stack = [home, user, Pictures]
        # 
        stack = []
        parts = path.split("/")
        for part in parts:
            if part == "." or part == "":
                continue
            elif part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return "/" + "/".join(stack)