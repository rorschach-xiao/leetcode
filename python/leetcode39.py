class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.candidates = candidates
        self.candidates.sort(reverse=True)
        self.result = []
        self.dfs(0,[],target)
        return self.result

    def dfs(self,start,cur_comb,target):
        if target == 0:
            if len(cur_comb) != 0:
                self.result.append(cur_comb.copy())
            return
        for idx in range(start,len(self.candidates)):
            if self.candidates[idx]>target:
                continue
            cur_comb.append(self.candidates[idx])
            self.dfs(idx,cur_comb,target-self.candidates[idx])
            cur_comb.pop(-1)


if __name__ == '__main__':
    solution = Solution()
    candidate = [1]
    target = 2
    print(solution.combinationSum(candidate,target))
