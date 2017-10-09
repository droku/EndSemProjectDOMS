from sympy import *
class Beam:
	def __init__(self,length,supportType):
		self.loadequation=0
		self.length=length
		self.supportType=supportType
		self.loadVariable=Symbol('w')
		self.shearForceEq=0
		self.bendingMomentEq=0

	def getDiscreteForce(self, dist, magnitude):
		
		self.loadequation=self.loadequation+magnitude*DiracDelta(self.loadVariable-dist)

	def getContinuousForce(self, leftdist, rightdistance, equation):
		tempx=Symbol('x')
		forceexpression=sympify(equation)*Heaviside(tempx)
		forceexpression1=forceexpression.subs(tempx,tempx-leftdist)
		forceexpression2=-1*forceexpression.subs(tempx,tempx-rightdistance)
		forceexpression=forceexpression1+forceexpression2
		self.loadequation=self.loadequation+forceexpression.subs(tempx,self.loadVariable)
	def calcShearForceEq(self):
		self.shearForceEq=integrate(self.loadequation)
	def calcBendingMomentEq(self):
		self.bendingMomentEq=integrate(self.shearForceEq)

		

