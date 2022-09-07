class Solution:
    def collect(self, intervals2):
        a = {}
        for i in intervals2:
            a[tuple(i)] = i[0]
        sorted_dict = dict(sorted(a.items(), key=lambda item:item[1]))
        result = []
        for i in sorted_dict:
            result.append(list(i))
        return result
                
    def merge(self, intervals):
        intervals1 = self.collect(intervals)
        ctr = 0
        total = len(intervals1)
        while ctr < total-1:
            if intervals1[ctr][1] >= intervals1[ctr+1][0]:
                intervals1[ctr] = [min(intervals1[ctr][0],intervals1[ctr+1][0]), max(intervals1[ctr][1], intervals1[ctr+1][1])]
                intervals1.remove(intervals1[ctr+1])
                total = len(intervals1)
            else:
                ctr += 1
            
        return intervals1
                