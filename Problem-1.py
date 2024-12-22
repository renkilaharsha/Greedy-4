#Approach
#Have 2 pointers and iterate over target and s if both strings are equall increment both
# if not increment s pointer and if reaches the end and j is not reached end then reinitialise the i=0 and do

#Complexities
#Time: O(mLog(n)
#Space O(n)

class Solution:
    """
    @param s: Source string
    @param target: Target string
    @return: Number of subsequences that can be spliced into target
    """
    def shortest_way(self, s: str, target: str) -> int:
        sourceLength = len(s)
        targetLength = len(target)

        i=0
        j=0
        count = 0
        hashSet = set()
        for i in s:
            hashSet.add(i)
        while j < targetLength:
            if target[j] in hashSet:
                if s[i]==target[i]:
                    i+=1
                    j+=1
                    if j==targetLength:
                        return count+1
                else:
                        i+=1
                if i==sourceLength:
                    count +=1
                    i=0
            else:
                return  -1
        return -1


class Solution:
    """
    @param s: Source string
    @param target: Target string
    @return: Number of subsequences that can be spliced into target
    """
    def shortest_way(self, s: str, target: str) -> int:
        sourceLength = len(s)
        targetLength = len(target)

        i=0
        j=0
        count = 0
        hashMap = dict()
        for i in range(len(s)):
            if s[i] not in hashMap:
                hashMap[s[i]]=[]
            hashMap[s[i]].append(i)

        while j < targetLength:
            if target[j] in hashMap:
                k = self.binarySearch(hashMap[target[j]],0,len(hashMap[target[j]])-1,i)
                if k == len(hashMap[target[j]]):
                    i=0
                    count+=1
                else:
                    i = hashMap[target[j]][k]
                    i+=1
                    j+=1
                    if j==targetLength:
                        return count+1
                    if i==sourceLength:
                        count +=1
                        i=0
            else:
                return  -1
        return -1

    def binarySearch(self,arr,low,high,target):
        mid  = (low+high)//2
        while low<=high:
            if arr[mid]==target:
                return mid
            elif arr[mid]>target:
                high=mid-1
            else:
                low = mid+1
        return low


