#Approach
#Start with firt element in top and bottom  and find the min rotations. if any one of the top or bottom dosent have the element in the array we cannot perform
# else take min from top or bottom

#Complexities:
#Time: O(n)
#Space: O(1)


from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        result = self.check(tops, bottoms, tops[0])
        if result != -1:
            return result
        return self.check(tops, bottoms, bottoms[0])

    def check(self, tops, bottom, target):
        topB, botB = 0, 0
        for i in range(len(tops)):
            if tops[i] != target and bottom[i] != target:
                return -1
            if tops[i] != target:
                topB += 1
            if bottom[i] != target:
                botB += 1
        return min(topB, botB)



