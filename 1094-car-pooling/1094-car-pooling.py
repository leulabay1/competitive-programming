class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        timeLine = {}
        for trip in trips:
            timeLine[trip[1]] = trip[0] + timeLine.get(trip[1],0)
            timeLine[trip[2]] = timeLine.get(trip[2],0) - trip[0]
        
        timeLine = {key: val for key, val in sorted(timeLine.items(), key = lambda ele: ele[0])}
        passengerNo = 0
        for i in timeLine.values():
            passengerNo += i
            if passengerNo > capacity:
                return False
        return True
            