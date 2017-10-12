from singularityClass import *
import re
import matplotlib.pyplot as plt
from sympy import *
class Beam:
	def __init__(self,length,supportType):
		self.loadequation=[]
		self.length=length
		self.supportType=supportType
		self.shearForceEq=[]
		self.bendingMomentEq=[]
		self.ConcForce = []
		self.concMoment = []
		self.distributedForce = []
		self.disSupport = []
		self.x = Symbol('x')
		self.sumforce = 0
		self.summoment = 0
	def calSupportReaction(self):
	
    		for i in range(0,len(self.concForce)):
        		self.sumforce += self.concForce[i][0]
        		self.summoment += self.concForce[i][0]*self.concForce[i][1]
				
		
    		for i in range(0,len(self.concMoment)):
        		self.summoment += self.concMoment[i][0]
				
		
    		for i in range(0,len(self.distributedForce)):
        		self.sumforce += N(integrate(self.distributedForce[i][0],(self.x,self.distributedForce[i][1],self.distributedForce[i][2])))
        		self.summoment += N(integrate(self.x*self.distributedForce[i][0],(self.x,self.distributedForce[i][1],self.distributedForce[i][2])))
				

    	if self.supportType is 'pinjoint':
    		reaction2 = -(self.summoment)/float(self.distSupport[1]-self.distsupport[0])
    		reaction1 = -(self.sumforce) - reaction2
    		getDiscreteForce(self.distSupport[0],reaction1)
			getDiscreteForce(self.distSupport[1],reaction2)
		if self.supportType is 'cantilever':
        	reaction_moment = -(summoment)
        	reaction_force = -(sumforce)
        	getBendingMoment(self.distSupport[0],reaction_moment)
			getDiscreteForce(self.distSupport[0],reaction_force)
		
	def getDiscreteForce(self, dist, magnitude):
		self.ConcForce.append([magnitude,dist])
		temp = singularity(dist,-1,magnitude)
		self.loadequation.append(temp)

	def getContinuousForce(self, leftdist, rightdistance, equation):
		equation=re.sub('-','+-',equation)
		#print(equation)
		equation=re.sub('\^','',equation)
		#print(equation)
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
			print(c)
			temp=singularity(leftdist,c[1],c[0])
			self.distributedForce.append([c[0]*(self.x**c[1]),leftdist,rightdistance])
			self.loadequation.append(temp)
			temp=singularity(rightdistance,c[1],-c[0])
			self.loadequation.append(temp)
	def getBendingMoment(self,dist,magnitude):
		self.concMoment.append([magnitude,dist])
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
	
		

