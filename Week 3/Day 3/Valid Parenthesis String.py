class Solution:
    def checkValidString(self, s: str) -> bool:
        _maxopen = 0
        _minopen = 0
        for c in s:
            if c == "(":
                _maxopen += 1
                _minopen += 1
            
            elif c == ")":
                _maxopen -= 1
                _minopen -= 1
            elif c == "*":
                _maxopen += 1
                _minopen -= 1
            if _maxopen < 0:
                return False
            _minopen = max(_minopen,0)
        return _minopen == 0
    