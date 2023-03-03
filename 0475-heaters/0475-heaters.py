class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        test = float("inf")
        ans = 0
        for house in houses:
           
            right_heater_index = bisect_left(heaters, house)
            right_heater = heaters[right_heater_index] if right_heater_index < len(heaters) else test
            left_heater = heaters[right_heater_index-1] if right_heater_index > 0 else -1*test
            
            radius = min(house - left_heater, right_heater - house)
            ans = max(ans, radius)
        
        return ans