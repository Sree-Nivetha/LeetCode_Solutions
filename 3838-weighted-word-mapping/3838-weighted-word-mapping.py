class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        result=""
        str_dict={0:'z',1:'y',2:'x',3:'w',4:'v',5:'u',6:'t',7:'s',8:'r',9:'q',10:'p',11:'o',12:'n',13:'m',14:'l',15:'k',16:'j',17:'i',18:'h',19:'g',20:'f',21:'e',22:'d',23:'c',24:'b',25:'a'}
        rev_str_dict = {v: k for k, v in str_dict.items()}
        for i in range(len(words)):
            sum=0
            count=0
            for j in range(len(words[i])):
                get_key=rev_str_dict.get(words[i][j])
                key=25-get_key
                sum+=weights[key]
                count+=1
            sum=sum%26
            letter=str_dict.get(sum)
            result=result+letter
        
        return result