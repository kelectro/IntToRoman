class NumConverter():
    def __init__(self):



        self.val_dict= {1:'I',4:'IV',5:'V',
                9:'IX',10:'X',40:'XL',
                50:'L',90:'XC',100:'C',
                400:'CD',500:'D',900:'CM',
                1000:'M'}


        # self.RomanCalculate()
        # self.IntCalculate('MMMCMXCIX')
    
    def __str__(self):
        custom_str="A class to convert a number from int to roman\
            num and roman num to int. "
        return(custom_str)
        

    def RomanFromInt(self,num):

        self.num = num
        self.result =''
        '''Roman is the key and value is the val'''        
        for val in sorted([(x) for x in self.val_dict.keys()], reverse=True) :
            if self.num // val > 0:
                self.result += self.num // val * self.val_dict[val]
                self.num = self.num - (self.num // val * val)
        return (self.result)

    def IntFromRoman(self,roman):
        '''Use the same dict. but key pair values inverted'''

        self.roman = roman
        self.inv_dict={v:k for k,v in self.val_dict.iteritems()}
        self.roman_result = 0
        for x in range(len(self.roman)):
            if x > 0 and self.inv_dict[self.roman[x]] > self.inv_dict[self.roman[x-1]]:
                self.roman_result += self.inv_dict[self.roman[x]]-2*self.inv_dict[self.roman[x-1]]
            else :
                self.roman_result +=self.inv_dict[self.roman[x]]
        return(self.roman_result)



x = 3999
z = 'CCLVII'
num = NumConverter()
roman = num.RomanFromInt(x)
inter = num.IntFromRoman(z)
print('The roman of {a} is {b}.\nThe interger of {c} is {d}'.format(a=x, b=roman, c=z, d=inter))

