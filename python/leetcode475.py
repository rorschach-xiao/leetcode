class Solution:
    def findRadius(self, houses, heaters) -> int:
        n = len(houses)
        m = len(heaters)
        houses = sorted(houses)
        heaters = sorted(heaters)
        ans = 0
        j = 0
        for i in range(n):
            cur_distance = abs(houses[i] - heaters[j])
            while(j < m - 1 and abs(houses[i] - heaters[j]) >= abs(houses[i] - heaters[j + 1])):
                cur_distance = abs(houses[i] - heaters[j + 1])
                j += 1
            if cur_distance > ans:
                ans = cur_distance
        return ans

    # sort + binary search
    # def findRadius(self, houses, heaters) -> int:
    #     n = len(houses)
    #     m = len(heaters)
    #     houses = sorted(houses)
    #     heaters = sorted(heaters)
    #     min_he, max_he = heaters[0], heaters[-1]
    #     max_minradius = -1
    #     for i in range(n):
    #         if min_he >= houses[i]:
    #             min_heater_distance = min_he - houses[i]
    #         elif houses[i] >= max_he:
    #             min_heater_distance = houses[i] - max_he
    #         else:
    #             l_p, r_p = 0, m - 1
    #             m_p = (l_p + r_p) // 2
    #             while(l_p + 1 < r_p):
    #                 if heaters[m_p] < houses[i]:
    #                     l_p = m_p
    #                     m_p = (l_p + r_p) // 2
    #                 elif heaters[m_p] > houses[i]:
    #                     r_p = m_p
    #                     m_p = (l_p + r_p) // 2
    #                 else:
    #                     break
    #
    #             min_heater_distance = min(abs(heaters[l_p] - houses[i]) , abs(heaters[r_p] - houses[i]), abs(heaters[m_p] - houses[i]))
    #         if min_heater_distance > max_minradius:
    #             max_minradius = min_heater_distance
    #     return max_minradius

if __name__ == '__main__':
    solution = Solution()
    houses = [1,2,3]
    heaters = [1,2,3]
    print(solution.findRadius(houses, heaters))
