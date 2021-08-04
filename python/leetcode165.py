class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1_num_list = version1.split('.')
        v2_num_list = version2.split('.')
        if len(v1_num_list) < len(v2_num_list):
            diff = len(v2_num_list) - len(v1_num_list)
            v1_num_list += [0] * diff
        elif len(v1_num_list) > len(v2_num_list):
            diff = len(v1_num_list) - len(v2_num_list)
            v2_num_list += [0] * diff

        n = len(v1_num_list)
        for i in range(n):
            if int(v1_num_list[i]) > int(v2_num_list[i]):
                return 1
            elif int(v1_num_list[i]) < int(v2_num_list[i]):
                return -1

        return 0
if __name__ == '__main__':
    solution = Solution()
    v1 = '1.02'
    v2 = '1.011.2'
    print(solution.compareVersion(v1,v2))