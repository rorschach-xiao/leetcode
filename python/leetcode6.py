class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        unit_num = numRows + numRows - 2
        unit_str_list = []
        num_unit = len(s) // unit_num + 1 if len(s) % unit_num != 0 else len(s) // unit_num
        for i in range(num_unit):
            unit_str_list.append(s[i*unit_num: (i+1)*unit_num])
        row_str_list = [[] for _ in range(numRows)]
        for unit in unit_str_list:
            for i in range(len(unit)):
                if i < numRows:
                    row_str_list[i].append(unit[i])
                else:
                    row_str_list[numRows - (i % numRows + 1) - 1].append(unit[i])
        result = ''.join([''.join(row) for row in row_str_list])
        return result

if __name__ == '__main__':
    solution = Solution()
    s = "PAYPALISHIRING"
    numRows = 3
    print(solution.convert(s, numRows))