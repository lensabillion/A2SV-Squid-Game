import heapq
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        ans = []
       
        digits = []
        letters = []
        for ind, log in enumerate(logs):
            slog = log.split(" ")
            if slog[1].isnumeric():
                heapq.heappush(digits,(ind, log))
            else:
                heapq.heappush(letters,(" ".join(slog[1:]), slog[0], log))
       
        while letters:
            curr = heapq.heappop(letters)  
            ans.append(curr[2])
        while digits:
            curr = heapq.heappop(digits)
            ans.append(curr[1])
        return ans