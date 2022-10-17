class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = {}
        ans = 0
        lp = 0
        for j in range(len(fruits)):
            basket[fruits[j]] = basket.get(fruits[j],0) + 1
            
            while len(basket) > 2:
                basket[fruits[lp]] = basket.get(fruits[lp], 0) - 1
                if basket[fruits[lp]] == 0:
                    del basket[fruits[lp]]
                lp+=1
            ans = max(ans, j-lp+1)
        return ans