# Median of Two Sorted Arrays
# You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order. Return the median value among all elements of the two arrays.

# Your solution must run in 

# O(log(m+n)) time.

# Example 1:

# Input: nums1 = [1,2], nums2 = [3]

# Output: 2.0

def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

    a,b = nums1,nums2

    if len(a) > len(b):
        b,a = a,b

    totalLength = len(a) + len(b)
    half = totalLength //2

    l = 0
    r = len(a)-1

    while True:
        i = (l+r)//2   # mid index of a

        # j represents the index in array b 
        # that complements the index i in 
        # array a, such that the total number 
        # of elements in the left partitions
        #  of both arrays combined equals half. 

        j = half - i -2 

        lefta  = a[i] if i >=0 else float('-inf')
        leftb = b[j] if j >=0 else float('-inf')

        righta = a[i+1] if i+1 < len(a) else float('inf')
        rightb = b[j+1] if j+1  < len(b) else float('inf')

        if lefta < rightb and leftb < righta:
            if totalLength % 2 : # odd
                return min(righta, rightb)
            return (max(lefta,leftb)+ min(righta, rightb)) / 2 # /2 to get float
        
        elif righta < leftb:
            l = i + 1
        else: #rightb < lefta
            r = i - 1