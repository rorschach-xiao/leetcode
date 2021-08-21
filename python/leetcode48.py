class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # [row,col] -> [col,(n-1)-row]
        # [2,2] -> [2,0]
        n = len(matrix)
        margin = 0
        while(n-2*margin>1):
            cur_x = margin
            start = margin
            end = n-margin-1
            for i in range(start,end):
                cur_y = i
                cur_val =  matrix[cur_x][cur_y]
                for _ in range(4):
                    next_x = cur_y
                    next_y = (n-1) - cur_x
                    next_val = matrix[next_x][next_y]
                    matrix[next_x][next_y] = cur_val
                    cur_val = next_val
                    cur_x = next_x
                    cur_y = next_y
            margin+=1
if __name__ == '__main__':
    solution = Solution()
    matrix = [[1,2,3],
              [4,5,6],
              [7,8,9]]

    solution.rotate(matrix)
    print(matrix)
