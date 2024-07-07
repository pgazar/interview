# Permutation String
# You are given two strings s1 and s2.

# Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

# Both strings only contain lowercase letters.

def checkInclusion(self, s1: str, s2: str) -> bool:
    n1= len(s1)
    n2= len(s2)

    count1=[0]* 26
    count2=[0]* 26

    if n1>n2:
        return False
    
    for i in range(n1):
        count1[ord(s1[i]) - ord('a')] +=1
        count2[ord(s2[i]) - ord('a')] +=1

    if count1 == count2:
        return True
    #sliding window moves forward

    for i in range(n1,n2):
        count2[ord(s2[i]) - ord('a')] +=1
        count2[ord(s2[i - n1]) - ord('a')] -=1
        if count1 == count2:
            return True
    return False


    