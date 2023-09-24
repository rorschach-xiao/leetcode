class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations)
        h_index = len(citations)
        for citation in citations:
            if citation < h_index:
                h_index -= 1
            else:
                break
        return h_index