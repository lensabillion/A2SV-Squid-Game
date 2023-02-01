class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        next_plant = 0
        next_bloom = 0
        arr = [[] for _ in range(len(plantTime))]
        for i in range(len(plantTime)):
            arr[i].append(plantTime[i])
            arr[i].append(growTime[i])
        sor = sorted(arr, key = lambda x:x[1],reverse=True)
        for i in range(len(plantTime)):
            next_bloom = max(next_bloom, next_plant + (sor[i][0] + sor[i][1]))
            next_plant += sor[i][0]
        return next_bloom