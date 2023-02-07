class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log[0] != ".":
                stack.append(log[:len(log)-1])
            elif log[0] == "." and len(log) == 2:
                continue
            else:
                if len(stack) > 0:
                    stack.pop()
        return len(stack)