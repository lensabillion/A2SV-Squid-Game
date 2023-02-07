class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        store = []
        ans = []
        i = 0
        while i < len(words):
            ins = []
            length = 0
            while i < len(words) and length + len(words[i]) <= maxWidth:
                length += (len(words[i]) + 1) 
                ins.append(words[i])  
                i += 1             
            store.append(ins)
       
        for i in range(len(store)-1):
            word = store[i]      
            string = " ".join(word)
            if len(string) == maxWidth:
                ans.append(string)
            elif len(string) < maxWidth:
                space = 0
                r = 0
                remaning = maxWidth - len(string)
                if remaning < len(word) - 1:
                    for r in range(remaning):
                        word[r] = word[r] + " "
                elif len(word) - 1 > 0:                    
                    space = remaning // (len(word) -1 )    
                    r = remaning % (len(word)-1)
                    if r == 1: 
                        word[0] = word[0] + (" " * r)
                    for j in range(len(word)-1):
                        word[j] = word[j] + (" " * space)            
                else:
                    word[0] = word[0] + (" " * remaning)                
                ans.append(" ".join(word))
        last_word = " ".join(store[-1])
        remaning = maxWidth - len(last_word)
        last_word = last_word + (" " * remaning)       
        a = last_word
        ans.append(a)        
        return ans
