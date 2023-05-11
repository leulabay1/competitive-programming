class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        nums = []
        for i, task in enumerate(tasks):
            nums.append((task[0],task[1], i))
        nums.sort(key = lambda x: x[0])
        tasks = nums
        avail = []
        heapq.heapify(avail)
        for task in tasks:
            if task[0] == tasks[0][0]:
                heapq.heappush(avail, (task[1],task[-1], task[0]))
            else:
                break
                
        ans = []
        time = tasks[0][0]
        count = len(avail)
        while count < len(tasks) or avail:
            if avail:
                node = heapq.heappop(avail)
                time += node[0]
                ans.append(node[1])
            while count < len(tasks):
                if tasks[count][0] <= time:
                    heapq.heappush(avail, (tasks[count][1],tasks[count][-1],tasks[count][0]))
                    count+=1
                else:
                    break
            if not avail:
                time += tasks[count-1][0]
        return ans
            