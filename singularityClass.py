import matplotlib.pyplot as plt
import numpy as np
class singularity:
    def __init__(self,constant, exponent, coefficientOfFunction,additionalLimiter=-1):
        self.constant=constant
        self.exponent= exponent
        self.coefficientOfFunction=coefficientOfFunction
        self.additionalLimiter=additionalLimiter
    def integrate(self):
        if(self.exponent <0):
            other=singularity(self.constant,self.exponent+1,self.coefficientOfFunction,self.additionalLimiter)
        else:
            other=singularity(self.constant,self.exponent+1,self.coefficientOfFunction/(self.exponent+1),self.additionalLimiter)
        return other
    def __str__(self):
        a=''
        if (self.constant>0):
            strValueOfConstant= '-'+str(self.constant)
        else:
            strValueOfConstant='+'+str(self.constant)
        if(self.coefficientOfFunction ==1):
                    a='+'+'<x'+strValueOfConstant+'>'+'^'+str(self.exponent)
        else :
            if(self.coefficientOfFunction>0):
                a='+'+str(self.coefficientOfFunction)+'*'+'<x'+strValueOfConstant+'>'+'^'+str(self.exponent)
            else:
                a='+'+str(self.coefficientOfFunction)+'*'+'<x'+strValueOfConstant+'>'+'^'+str(self.exponent)
        if(self.additionalLimiter != -1):
            a=a+'*<x-' + str(self.additionalLimiter)+'>'
        return a
    def plotpoints(self,length):
        x= [x / 100.0 for x in range(0,length*100, 1)]
        y=[]
        for someNumber in x:
            if(self.additionalLimiter== -1):
                if (someNumber< self.constant and self.exponent >= 0):
                    y.append(0)
                elif (someNumber >self.constant and self.exponent >=0):
                    y.append(self.coefficientOfFunction*((someNumber-self.constant)** self.exponent))
                elif (self.exponent == -1):
                    if (someNumber == self.constant):
                       # print("entered condition")
                        y.append(self.coefficientOfFunction)
                    else:
                        y.append(0)
                elif (self.exponent == -2):
                    y.append(0)
            else:
                #print('entered condition')
                if(someNumber<self.additionalLimiter and someNumber>self.constant):
                    y.append(self.coefficientOfFunction*((someNumber-self.constant)** self.exponent))
                else:
                    y.append(0)
        return y
    def __mul__ (self,other):
        new =singularity(self.constant,self.exponent,self.coefficientOfFunction,other.constant)
        return new