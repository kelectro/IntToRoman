
class NumConverter():
    def __init__(self,num):

        self.num = num
        self.result =''
        self.NumCalculate()
    
    def __str__(self):
        custom_str="Takes one number as argument and converts it to roman numerals"
        return(custom_str)
        

    def NumCalculate(self):

        '''Roman is the key and value is the val'''

        self.val_dict= {'1':'I','4':'IV','5':'V',
                        '9':'IX','10':'X','40':'XL',
                        '50':'L','90':'XC','100':'C',
                        '400':'CD','50':'D','900':'CM',
                        '1000':'M'}
        
       
        for val in sorted([int(x) for x in self.val_dict.keys()], reverse=True) :
            if self.num // val > 0:
                self.result += self.num // val * self.val_dict[str(val)]
                self.num = self.num - (self.num // val * val)
        return (self.result)




num = NumConverter(36)
print(num.result)