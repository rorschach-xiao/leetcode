class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        targetDict = {}
        # initialize hash map
        for i in range(n):
            if t[i] not in targetDict:
                targetDict[t[i]] = 1
            else:
                targetDict[t[i]] += 1
        front, behind = 0, 0
        minSubstring = ""
        counter = n
        while (front < m):
            if s[front] in targetDict:
                targetDict[s[front]] -= 1
                if targetDict[s[front]] >= 0:
                    counter -= 1

            while (counter == 0):
                if "" == minSubstring or front - behind + 1 < len(minSubstring):
                    minSubstring = s[behind: front + 1]
                if (s[behind] in targetDict):
                    targetDict[s[behind]] += 1
                    if targetDict[s[behind]] > 0:
                        counter += 1
                behind += 1
            front += 1
        return minSubstring

if __name__ =='__main__':
    solution = Solution()
    print(solution.minWindow("ADOBECODEBANC", "ABC"))