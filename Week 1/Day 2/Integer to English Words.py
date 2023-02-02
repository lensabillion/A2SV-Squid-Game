class Solution:
    def numberToWords(self, num: int) -> str:
        string_num = str(num)
        hash_map = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen",20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety", 100:"Hundred", 1000:"Thousand",1000000:"Million",1000000000:"Billion"}
        
        def nameIt(number):
            if len(number) == 1:
                oneth = int(number[-1])
                if oneth in hash_map:
                    return hash_map[oneth]
                return "Zero"
            elif len(number) == 2:
                if int(number) in hash_map:
                    return hash_map[int(number)]
                tenth = int(number[0]) * 10
                oneth = int(number[-1])
                return hash_map[tenth] + " " + hash_map[oneth]
            elif len(number) == 3:
                local = []
                hundredth = int(number[0])
                if hundredth in hash_map:
                    local.append(hash_map[hundredth])
                    local.append(hash_map[100])
                if number[1] == "1":
                    two = int(number[1:])
                    local.append(hash_map[two])
                else:
                    tenth = int(number[1]) * 10
                    oneth = int(number[-1])
                    
                    if tenth in hash_map:
                        local.append(hash_map[tenth])
                    if oneth in hash_map:
                        local.append(hash_map[oneth])
               
                return " ".join(local)
            return ""
        
        ans = []
        arr = []
        n = len(string_num)
        while n >= 0:
            st = max(0,n - 3)
            en = n 
            s = string_num[st:en]
            if len(s) > 0:
                arr.append((s, en))
            n = n - 3
        arr = arr[::-1]
        length = len(string_num)
        for pair in arr:
            word = nameIt(pair[0])
            if len(word) > 0:
                ans.append(word)
            power = length - pair[1]
            if len(word) > 0 and power > 0:
                ans.append(hash_map[10**power])
        
        return " ".join(ans)


