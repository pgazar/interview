# Eating Bananas
# You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.

# You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

# Return the minimum integer k such that you can eat all the bananas within h hours.

import math
def minEatingSpeed(self, piles: list[int], h: int) -> int:
    l = 1 #at least one banana
    r = max(piles)
    res = r

    while l <=r:
        k = (l+r)//2
        totalH = 0

        for p in piles:
            totalH += math.ceil(p/k) # time taken for each pile if koko eats k banana
        
        if totalH <= h:
            res = min(res,k) # find min number of bananas (k) to finish in h time
            r = k-1
        else:
            l = k+1
    return res


