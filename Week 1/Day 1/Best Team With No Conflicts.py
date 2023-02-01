class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        scag = [[] for _ in range(len(scores))]
        for i in range(len(scores)):
            scag[i].append(ages[i])
            scag[i].append(scores[i])
        sor = sorted(scag)
        ans = [0 for _ in range(len(scores))]
        res = 0
        for i in range(len(scores)):
            ans[i] = sor[i][1]
            for j in range(i):
                if sor[i][1] >= sor[j][1]:
                    ans[i] = max(ans[i], ans[j] + sor[i][1])
            res = max(res, ans[i])
        return res