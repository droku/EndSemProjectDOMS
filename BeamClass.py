from singularityClass import *
import re 
import matplotlib.pyplot as plt
from sympy import symbols,Integral,N
from sympy.abc import x
class Beam:
	def __init__(self,length,supportType,x=0,y=0):
		self.loadequation=[]
		self.length=length
		self.supportType=supportType
		self.support1=x
		self.support2=y
		self.shearForceEq=[]
		self.bendingMomentEq=[]
		
	def calcSupportReac(self):
		netLoad=0
		netBendingMoment=0
		integralOfBendingMoment=[]
		for x in self.shearForceEq:
			temp=x.sub(self.length)
			netLoad=netLoad+temp
		for x in self.bendingMomentEq:
			temp=x.integrate()
			integralOfBendingMoment.append(temp)
		for x in integralOfBendingMoment:
			temp=x.sub(self.length)
			netBendingMoment=temp+netBendingMoment
		if(self.supportType=='Pin Joint'):
			self.getDiscreteForce(self.support1,(netBendingMoment-netLoad*self.support1)*-1/(self.support2-self.support1))
			self.getDiscreteForce(self.support2,(netLoad*self.support2-netBendingMoment)*-1/(self.support2-self.support1))


		netBendingMoment=0
		
	def getDiscreteForce(self, dist, magnitude):
		temp = singularity(dist,-1,magnitude)
		self.loadequation.append(temp)

	
	def getContinuousForce(self, leftdist, rightdistance, equation):
		equation=re.sub('-','+-',equation)
		print(equation)
		equation=re.sub('\^','',equation)
		print(equation)
		print(equation)
		a=re.split('[+]',equation)
		for p in a:
			b=p.split('x')
			c=[]
			for val in b:
				if(val==''):
					val='1'
				newval=float(val)
				if newval:
					c.append(newval)
			print(c)
			if(len(c)<2):
				c.append(0)
			temp=singularity(leftdist,c[1],c[0])
			self.loadequation.append(temp)
			if(rightdistance != self.length):
				temp=singularity(rightdistance,c[1],-c[0])
				self.loadequation.append(temp)
	def getBendingMoment(self,dist,magnitude):
		temp=singularity(dist,-2,magnitude)
		self.loadequation.append(temp)	
	def printLoadEquation(self):
		st=''
		for x in self.loadequation:
			st=st+' '+str(x)
		st=re.sub('\+-','-',st)
		print(st)
	def printShearForceEquation(self):
		st=''
		for x in self.shearForceEq:
			st=st+' '+str(x)
		st=re.sub('\+-','-',st)
		print(st)
	def printBendingMomentEquation(self):
		st=''
		for x in self.bendingMomentEq:
			st=st+' '+str(x)
		st=re.sub('\+-','-',st)
		print(st)
	def calcShearForceEq(self):
		for A in self.loadequation:
			A.coefficientOfFunction=-1*A.coefficientOfFunction
			temp=A.integrate()
			#print(temp)
			self.shearForceEq.append(temp)

	def calcBendingMomentEq(self):
		for A in self.shearForceEq:
			temp=A.integrate()
			self.bendingMomentEq.append(A)
	
		

