class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations=sorted(citations,reverse = True)
        h = len(citations)
        l = 0
        count = 0
        for i in range(len(citations)):
            if citations[l] >= h:
                count += 1
                l += 1
            else:
                h -= 1

            if count >= h:
                return h
