class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        ans = [0] * k
        dict = {}
        for log in logs:
            if log[0] not in dict:
                dict[log[0]] =set()
            dict[log[0]].add(log[1])
       
        for el in dict:
            index = len(dict[el])
            
            ans[index-1] +=1
        return ans