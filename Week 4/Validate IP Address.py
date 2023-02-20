class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        arr = []
        characters = "abcdefABCDEF"
        if "." in queryIP and ":" in queryIP:
            return "Neither"
        elif "." in queryIP:
            arr = queryIP.split(".")
        elif ":" in queryIP:
            arr = queryIP.split(":")
        # print(arr)
        if len(arr) == 4:
            for w in arr:
                for e in w:
                    if not e.isnumeric():
                        return "Neither"

                if len(w) > 1 and w[0] == "0":
                    return "Neither"
                elif len(w) == 0 or len(w) > 3:
                    return "Neither"
                elif len(w) > 0 and 0 > int(w) or int(w) > 255:
                    return "Neither"
                
                
            return "IPv4"
        elif len(arr) == 8:
            for w in arr:
                for e in w:
                    if e.isalpha() and (e not in characters):
                        return "Neither"
                if len(w) > 4 or len(w) == 0:
                    return "Neither"
            return "IPv6"


        return "Neither"