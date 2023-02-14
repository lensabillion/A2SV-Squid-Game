from collections import Counter
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
       
        # store all the possible reorders if it doesnt have a leading zero
        
        nums = Counter(list(str(n)))
        def occur(map1, map2):
            for el in map1:
                if el not in map2 or map1[el] != map2[el]:
                    return False
            for el in map2:
                if el not in map1 or map1[el] != map2[el]:
                    return False
            return True
        # print(nums)
        for i in range(30):
            current = Counter(list(str(2 ** i)))
            # print(current, "cur")
            if occur(nums, current):
                return True
                break
        return False
       