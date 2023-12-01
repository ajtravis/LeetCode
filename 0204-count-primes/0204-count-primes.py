import math
class Solution:
    # # primes = [2,3,5,7]
    # # high = max(primes)
    # def isPrime(num):
    #         # if num < 2:
    #         #     return False
    #         # elif num == 2:
    #         #     return True
    #         # elif num % 2 == 0:
    #         #     return False
    #         # else:
    #         #     i = 3 
    #         #     while i < num/2:
    #         #         if num % i == 0:
    #         #             return False
    #         #         i += 2
    #         #         return True
    #         flag = 0
    #         # if num in Solution.primes:
    #         #     return True
    #         # elif num > Solution.high:
    #         for i in range(2, int(math.sqrt(num))+1):
    #             if(num%i==0):
    #                 flag = 1
    #                 return False
    #         # else:
    #         #     flag = 1
    #         #     return False
    #         if flag == 0:
    #             # Solution.primes.append(int(num))
    #             # Solution.high = max(Solution.primes)
    #             return True
            
    def countPrimes(self, n: int) -> int:
         
#         count = 0
#         if n <= 2:
#             return 0
#         for x in range(2, n):
#             if Solution.isPrime(x) == True:
#                 count += 1   
             
#         return count
        if n <= 2:
            return 0
        true = [True]*(n)
        true[0], true[1] = False, False
        i = 2
        while i*i < n:
            if true[i] == True:
                for x in range(i*i, n, i):
                    true[x] = False
            i += 1
        return true.count(True)