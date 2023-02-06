class DetectSquares:

    def __init__(self):        
        self.hash_map = {}
    def add(self, point: List[int]) -> None:
        if (point[0], point[1]) not in self.hash_map:
            self.hash_map[(point[0], point[1])] = 0
        self.hash_map[(point[0], point[1])] += 1
        
    def count(self, point: List[int]) -> int:
        ans = 0
        row, col = point[0], point[1]
        for el in self.hash_map:
            if abs(row - el[0]) != abs(col-el[1]) or row == el[0] or col == el[1]:
                continue
            if (el[0], col) in self.hash_map and (row, el[1]) in self.hash_map:

                ans += self.hash_map[(el[0], col)] * self.hash_map[(row, el[1])] * self.hash_map[el]
        return ans
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)