class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        temp_dict = dict()
        temp = []
        for i in points:
            if tuple(i) in temp_dict: 
                temp.append(tuple(i))
            else:
                dist = ((i[0])**2 + (i[1])**2)**(0.5)
                temp_dict[tuple(i)] = dist
            
        sorted_dict = {key: val for key, val in sorted(temp_dict.items(), key = lambda ele: ele[1])}
        ctr = 0
        result = []
        for i in sorted_dict.keys():
            if ctr >= k:
                break
            if i in temp :
                for j in range(temp.count(i)+1):
                    result.append(list(i))
                    ctr += 1
                    if ctr >= k:
                        break
            else:
                result.append(list(i))
                ctr += 1
                if ctr >= k:
                    break
        return result