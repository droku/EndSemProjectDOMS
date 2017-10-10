from singularityClass import *
import re
import matplotlib.pyplot as plt

class Beam:
	def __init__(self,length,supportType):
		self.loadequation=[]
		self.length=length
		self.supportType=supportType
		self.shearForceEq=[]
		self.bendingMomentEq=[]

	def getDiscreteForce(self, dist, magnitude):
		
		temp = singularity(dist,-1,magnitude)
		self.loadequation.append(temp)

	def getContinuousForce(self, leftdist, rightdistance, equation):
		equation=re.sub('-','+-',equation)
		equation=re.sub('\^','',equation)
		#print(equation)
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

			temp=singularity(leftdist,c[1],c[0])
			temp1=singularity(rightdistance,c[1],-c[0])
			temp=temp*temp1
			print(temp)
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
			B=singularity(A.constant,A.exponent,-1*A.coefficientOfFunction,A.additionalLimiter)
			temp=B.integrate()

		#	print(temp)
			self.shearForceEq.append(temp)

	def calcBendingMomentEq(self):
		for A in self.shearForceEq:
			B=singularity(A.constant,A.exponent,A.coefficientOfFunction,A.additionalLimiter)
			temp=B.integrate()
			self.bendingMomentEq.append(temp)
		
	def plotLoadEq(self):
		x=[x/100.0 for x in range(0,self.length*100,1)]
		plotpoints=[0]*self.length*100
		for someValue in self.loadequation:
			#print(someValue.additionalLimiter)
			currentpoints=someValue.plotpoints(self.length)
			i=0
			while(i<self.length*100-1):
				#print(i)
				plotpoints[i]=plotpoints[i]+currentpoints[i]
				i=i+1

		plt.plot(x,plotpoints)
		plt.show()
	def plotShearForceEq(self):
		x=[x/100.0 for x in range(0,self.length*100,1)]
		plotpoints=[0]*self.length*100
		for someValue in self.shearForceEq:
			#print(someValue.additionalLimiter)
			currentpoints=someValue.plotpoints(self.length)
			i=0
			while(i<self.length*100-1):
				#print(i)
				plotpoints[i]=plotpoints[i]+currentpoints[i]
				i=i+1

		plt.plot(x,plotpoints)
		plt.show()
	def plotBendingMomentEq(self):
		x=[x/100.0 for x in range(0,self.length*100,1)]
		plotpoints=[0]*self.length*100
		for someValue in self.bendingMomentEq:
			#print(someValue.additionalLimiter)
			currentpoints=someValue.plotpoints(self.length)
			i=0
			while(i<self.length*100-1):
				#print(i)
				plotpoints[i]=plotpoints[i]+currentpoints[i]
				i=i+1

		plt.plot(x,plotpoints)
		plt.show()