class Solution:
    def countStudents(self, students, sandwiches) -> int:
        while (len(students) > 0 and len(sandwiches) > 0):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                if len(students) == sum(students) or sum(students) == 0:
                    break
                cur = students.pop(0)
                students.append(cur)

        return len(students)

if __name__ == '__main__':
    solution = Solution()
    students = [1,0,1,0,1,1,0,1,1,1,1,0,0,0,1,1,1,0,1,1,1,1,0,0,0,1,0,0,0,0]
    sandwiches = [0,1,0,0,1,1,1,1,1,1,0,1,1,0,0,0,1,1,0,0,1,1,1,1,0,0,1,0,1,0]
    print(solution.countStudents(students, sandwiches))