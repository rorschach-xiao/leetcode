from typing import List


# class Solution:
#     def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
#         flowers = sorted(flowers)
#         n = len(flowers)
#         completed = sum([flower >= target for flower in flowers])
#         maxBeauty = completed * full
#         if flowers[0] < target:
#             maxBeauty += flowers[0] * partial
#         right = n - 1
#         while 0 <= right and newFlowers > 0:
#             if target - flowers[right] > 0:
#                 # situation 1: make the garden[right] incompleted
#                 curMin = self.helper(flowers, 0, right + 1, target, newFlowers)
#                 curBeauty1 = completed * full
#                 if completed < n:
#                     curBeauty1 += curMin * partial
#                 # situation 2: make the garden[right] completed
#                 newFlowers -= target - flowers[right]
#                 remainFlowers = newFlowers
#                 if remainFlowers >= 0:
#                     completed += 1
#                     curMin = self.helper(flowers, 0, right, target, remainFlowers)
#                     curBeauty2 = completed * full
#                     if completed < n:
#                         curBeauty2 += curMin * partial
#                 maxBeauty = max(maxBeauty, curBeauty1, curBeauty2)
#             right -= 1
#         return maxBeauty
#
#     def helper(self, flowers, left, right, target, remainFlowers):
#         curMin = flowers[0]
#         # distribute the remaining flowers to rest imcompleted garder
#         while left < right and remainFlowers > 0:
#             if left + 1 < right:
#                 pre = remainFlowers
#                 remainFlowers -= (flowers[left + 1] - flowers[left]) * (left + 1)
#                 if remainFlowers >= 0:
#                     curMin = flowers[left + 1]
#                 else:
#                     curMin = curMin + pre // (left + 1)
#
#             else:
#                 pre = remainFlowers
#                 remainFlowers -= (target - 1 - flowers[left]) * (left + 1)
#                 if remainFlowers >= 0:
#                     curMin = target - 1
#                 else:
#                     curMin = curMin + pre // (left + 1)
#             left += 1
#         return curMin

class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        flowers = sorted([min(target, f) for f in flowers])
        totalSum = sum(flowers)
        preSum = 0
        n = len(flowers)
        maxBeauty = 0
        if target * n - totalSum <= newFlowers:
            maxBeauty = full * n

        p = n - 1
        for i in range(n - 1, -1, -1):
            if i != n - 1:
                preSum += flowers[i + 1]
            if flowers[i] == target:
                continue
            rest = newFlowers - (target * (n - i - 1) - preSum)
            if rest < 0:
                break

            while i < p or flowers[p] * (p + 1) - totalSum > rest:
                totalSum -= flowers[p]
                p -= 1
            rest -= flowers[p] * (p + 1) - totalSum

            maxBeauty = max(maxBeauty, (n - i - 1) * full + partial * min(flowers[p] + rest // (p + 1), target - 1))

        return maxBeauty

if __name__ == '__main__':
    solution = Solution()
    flowers = [1, 3, 1 ,1]
    newFlowers = 7
    target = 6
    full = 12
    partial = 1
    print(solution.maximumBeauty(flowers, newFlowers, target, full, partial))
