class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0]*n
        prev = 0
        for log in logs:
            parts = log.split(":")
            id,status,time = int(parts[0]),parts[1],int(parts[2])
            if status == "start":
                if stack:
                    res[stack[-1]] += time - prev
                stack.append(id)
                prev = time
            else:
                res[stack[-1]] += time-prev+1
                stack.pop()
                prev = time+1
        return res
                
            
        
        