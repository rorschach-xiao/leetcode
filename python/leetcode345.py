class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_set = {"a","e","i","o","u","A","E","I","O","U"}
        p1, p2 = 0, len(s) - 1
        s = list(s)
        while p1 < p2:
            while p1 < p2 and s[p1] not in vowel_set:
                p1 += 1
            while p1 < p2 and s[p2] not in vowel_set:
                p2 -= 1
            s[p1], s[p2] = s[p2], s[p1]
            p1 += 1
            p2 -= 1
        return "".join(s)