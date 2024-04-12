class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def setbits(i,num):
            return (1<<i)&num>0
        sb1=0
        sb2=0
        l=['0']*31
        #print(l)
        for i in range(32):
            if(setbits(i,num1)):
                sb1+=1
            if(setbits(i,num2)):
                sb2+=1
        if(sb1==sb2):
            return num1
        elif(sb1>sb2):
            for i in range(31,-1,-1):
                if((1<<i)&num1 and sb2):
                    l[31-i-1]='1'
                    sb2-=1
            print(l)
            return int(''.join(l),2)
            pass
        else:
            for i in range(31,-1,-1):
                if((1<<i)&num1 and sb2):
                    l[31-i-1]='1'
                    sb2-=1
            for i in range(0,32):
                if((1<<i)&num1==0 and sb2):
                    l[31-i-1]='1'
                    sb2-=1
            print(l)
            return int(''.join(l),2)
            
            pass