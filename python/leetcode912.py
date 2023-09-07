import random
# QUICKSORT
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.nums = nums
        start = 0
        end = len(nums)-1
        self.helper(start,end)
        return self.nums

    def helper(self,start,end):
        if start>=end:
            return
        pivot = self.partition(start,end)
        self.helper(start,pivot-1)
        self.helper(pivot+1,end)

    def partition(self,start,end):
        pivot = random.randint(start,end)
        self.swap(pivot,start)
        pivot = start
        left_p = start
        right_p = end
        while(left_p<right_p):
            if self.nums[right_p]>self.nums[pivot]:
                right_p-=1
                continue
            if self.nums[left_p]<=self.nums[pivot]:
                left_p+=1
                continue

            self.swap(left_p,right_p)

        self.swap(pivot,right_p)
        return right_p

    def swap(self,i,j):
        tmp = self.nums[i]
        self.nums[i] = self.nums[j]
        self.nums[j] = tmp
# MERGESORT
class Solution2():
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.nums = nums
        result = self.helper(0,len(nums)-1)
        return result

    def helper(self,start,end):
        if start >= end:
            return self.nums[start:start+1]
        mid = (start+end)//2
        s1 = self.helper(start,mid)
        s2 = self.helper(mid+1,end)
        return self.merge(s1,s2)

    def merge(self,s1,s2):
        p1 = 0
        p2 = 0
        n1 = len(s1)
        n2 = len(s2)
        new_s = []
        while(p1<n1 and p2<n2):
            if s1[p1]<s2[p2]:
                new_s.append(s1[p1])
                p1+=1
            else:
                new_s.append(s2[p2])
                p2+=1
        if p1!=n1:
            new_s+=s1[p1:]
        if p2!=n2:
            new_s+=s2[p2:]
        return new_s



if __name__ == '__main__':
    solution = Solution2()
    # nums = [3,2,1,4,5,6]
    nums = [-4,0,7,4,9,-5,-1,0,-7,-1]
    print(solution.sortArray(nums))
