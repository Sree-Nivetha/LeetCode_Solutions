import sys
sys.set_int_max_str_digits(0)

class Solution:
    def lst_to_digit(self,num_lst):
        number=0
        for i in num_lst:
            number=(number*10)+i
        return number

    def addStrings(self, num1: str, num2: str) -> str:
        num1_lst=[ord(i)-ord('0') for i in num1]
        num2_lst=[ord(i)-ord('0') for i in num2]

        number1=self.lst_to_digit(num1_lst)
        number2=self.lst_to_digit(num2_lst)

        result=str(number1+number2)
        return result