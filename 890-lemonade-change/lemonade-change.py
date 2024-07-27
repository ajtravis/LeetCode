class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] != 5:
            return False
        change = {"5": 0, "10": 0,"20": 0}
        i = 0
        while i < len(bills): 
            cur = bills[i]
            if cur == 5:
                change["5"]+=1
            elif cur == 10:
                if change["5"] > 0:
                    change["10"] += 1
                    change["5"] -= 1
                else:
                    return False
            elif cur == 20:
                if change["10"] > 0 and  change["5"] > 0:
                    change["20"] += 1
                    change["10"] -= 1
                    change["5"] -= 1
                elif change["5"] >= 3:
                    change["20"] += 1
                    change["5"] -= 3
                else:
                    return False    
            i+= 1
        return True