import singularityClass as sng
import re
class Beam:
	def __init__(self,length,supportType):
		self.loadequation=[]
		self.length=length
		self.supportType=supportType
		self.shearForceEq=[]
		self.bendingMomentEq=[]

	def getDiscreteForce(self, dist, magnitude):
		
		temp = sng(dist,-1,magnitude)
		self.loadequation.append(temp)

	def getContinuousForce(self, leftdist, rightdistance, equation):
		equation=re.sub('-','+-',equation)
		equation=re.sub('\^','',equation)
		print(equation)
		a=re.split('[+]',equation)
		for p in a:
			b=p.split('x')
			c=[]
			for val in b:
				if(val==' '):
					val='1'
				newval=float(val)
				if newval:
					c.append(newval)
			temp=sng(leftdist,c[1],c[0])
			self.loadequation.append(temp)
			temp=sng(rightdistance,c[1],-c[0])
			self.loadequation.append(temp)
	def getBendingMoment(self,dist,magnitude):
		temp=sng(dist,-2,magnitude)
		self.loadequation.append(temp)	
	def printLoadEquation(self):
		st=''
		for x in self.loadequation:
			st=st+str(x)
		print(st)
	def printShearForceEquation(self):
		st=''
		for x in self.shearForceEq:
			st=st+str(x)
		print(st)
	def printBendingMomentEquation(self):
		st=''
		for x in self.bendingMomentEq:
			st=st+str(x)
		print(st)
	def calcShearForceEq(self):
		self.shearForceEq=integrate(self.loadequation)

	def calcBendingMomentEq(self):
		self.bendingMomentEq=integrate(self.shearForceEq)

		

