class Solution:
    def maximumSwap(self, num: int) -> int:
        str_num = str(num)
        store = []
        def maximum(number):            
            ins = list(number)
            ind = 0
            for i in range(1, len(ins)):
                if ins[i] >= ins[ind]:
                    ind = i
            ins[ind], ins[0] = ins[0], ins[ind]
            return "".join(ins)

            
        for i in range(len(str_num)):
            curr = str_num[:i] + maximum(str_num[i:])
            store.append(int(curr))
      
        return max(store)