class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        q = [(0, 0, "N")]
        store = []
        
        for ins in instructions:
            row, col,  d = q.pop()
            store.append((row, col))
            if ins == "G":
                if d == "N":
                    q.append((row, col + 1, d))
                if d == "S":
                    q.append((row, col - 1, d))
                if d == "E":
                    q.append((row + 1, col, d))
                if d == "W":
                    q.append((row - 1, col, d))
            if ins == "L":
                if d == "N":
                    q.append((row, col, "W"))
                if d == "S":
                    q.append((row, col, "E"))
                if d == "E":
                    q.append((row, col, "N"))
                if d == "W":
                    q.append((row, col, "S"))
            if ins == "R":
                if d == "N":
                    q.append((row, col, "E"))
                if d == "S":
                    q.append((row, col, "W"))
                if d == "E":
                    q.append((row, col, "S"))
                if d == "W":
                    q.append((row, col, "N"))

        
        r, c, d = q.pop()
        if r == 0 and c == 0:
            return True
        else:
            if d == "N":
                return False
            return True
       
      