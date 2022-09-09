class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        temp = arr
        result = []
        for i in range(len(arr), 0, -1):
            #reversing the last unsorted element to the front
            position = temp.index(i)
            temp_front = temp[0:position+1]
            temp_front.reverse()
            temp_back = temp[position+1:len(arr)]
            temp = temp_front + temp_back
            #now reversing the element back to it's sorted postion
            temp_front = temp[0: i]
            temp_front.reverse()
            temp_back = temp[i:len(arr)]
            temp = temp_front + temp_back
            result.append(position+1)
            result.append(i)
        return result
    
