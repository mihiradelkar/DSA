class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def best(f_start,f_dur,s_start,s_dur):
            # get first best start + duration
            best_start = float("inf")
            for s,d in zip(f_start,f_dur):
                best_start = min(best_start,s+d)
            # get min dur after best start
            min_dur = float("inf")
            for s,d in zip(s_start,s_dur):
                min_dur = min(min_dur,max(best_start,s)+d)
            
            return min_dur
        
        land_first  = best(landStartTime, landDuration, waterStartTime, waterDuration)
        water_first = best(waterStartTime, waterDuration, landStartTime, landDuration)

        return min(land_first,water_first)