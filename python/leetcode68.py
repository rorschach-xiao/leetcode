from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        justified_lines = []
        current_line_words = []
        current_line_words_total_len = 0
        for word in words:
            if current_line_words_total_len + len(current_line_words) + len(word) <= maxWidth:
                current_line_words.append(word)
                current_line_words_total_len += len(word)
            else:
                space_num = maxWidth - current_line_words_total_len
                if len(current_line_words) - 1 == 0:
                    interval_min_space = space_num
                else:
                    interval_min_space = space_num // (len(current_line_words) - 1)
                current_line = ""
                for i in range(len(current_line_words)):
                    if i == len(current_line_words) - 1:
                        if len(current_line_words) - 1 != 0:
                            current_line += current_line_words[i]
                        else :
                            current_line += current_line_words[i] + " " * interval_min_space
                    elif i < space_num % (len(current_line_words) - 1):
                        current_line += current_line_words[i]
                        current_line += " " * (interval_min_space + 1)
                    else:
                        current_line += current_line_words[i]
                        current_line += " " * interval_min_space
                current_line_words = [word]
                current_line_words_total_len = len(word)
                justified_lines.append(current_line)
        if len(current_line_words) != 0:
            current_line = " ".join(current_line_words)
            current_line += " " * (maxWidth - len(current_line))
            justified_lines.append(current_line)

        return justified_lines

if __name__ == '__main__':
    solution = Solution()
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    print(solution.fullJustify(words, maxWidth))