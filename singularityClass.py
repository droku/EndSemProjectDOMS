class singularity:
    def __init__(self,constant, exponent, coefficientOfFunction):
        self.constant=constant
        self.exponent= exponent
        self.coefficientOfFunction=coefficientOfFunction
    def integrate(self):
        if(self.exponent <0):
            self.exponent=self.exponent+1
        else:
            self.exponent=self.exponent+1
            self.coefficientOfFunction=self.coefficientOfFunction/(self.exponent)
    def __str__(self):
        a=''
        if (self.constant>0):
            strValueOfConstant= '-'+str(self.constant)
        else:
            strValueOfConstant='+'+str(self.constant)
        if(self.coefficientOfFunction ==1):
                    a='<x'+strValueOfConstant+'>'+'^'+str(self.exponent)
        else :
            a=str(self.coefficientOfFunction)+'*'+'<x'+strValueOfConstant+'>'+'^'+str(self.exponent)
        return a