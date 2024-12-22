class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        nums = str(num)
        i = 0
        while i<len(nums):
            digit = int(nums[i])

            if len(nums)-i==4:
                if digit>=1:
                    res+='M'*digit
                    #num -= digit * 1000
                i+=1
            elif len(nums)-i==3:
                if digit==4:
                    res+='CD'
                    #num -= 400
                elif digit ==9:
                    res+='CM'
                    #num -= 900
                elif digit>=5:
                    res+='D'+ 'C'*(digit-5)
                    #num -= (500 + 100*(digit-5))
                elif digit>=1:
                    res+='C'*digit
                    #num -= (100 *(digit))
                i+=1
            elif len(nums)-i==2:
                if digit==4:
                    res+='XL'
                    #num -= 40
                elif digit ==9:
                    res+='XC'
                    #num -= 90
                elif digit>=5:
                    res+='L'+ 'X'*(digit-5)
                    #num -= (50 + 10*(digit-5))
                elif digit>=1:
                    res+='X'*digit
                    #num -= (10 *(digit))
                i+=1
            elif len(nums)-i==1:
                if digit == 4:
                    res+='IV'
                    #num -= 4
                elif digit ==9:
                    res+='IX'
                    #num -= 9
                elif digit>=5:
                    res+='V'+'I'*(digit-5)
                    #num -= (5 + 1*(digit-5))
                elif digit>=1:
                    res+='I'*digit
                    #num -= (1*digit)
                i+=1
        return res




        
