from BeamClass import *
from sympy import *
newBeam=Beam(10,'cantilever','circle',70*(10**9),0,0,5)
newBeam.getDiscreteForce(5 ,10)
#newBeam.getContinuousForce(3,6,'10')
#newBeam.getContinuousForce(3,6,'-5x')
newBeam.getContinuousForce(3,6,'x^2')

newBeam.calcShearForceEq()
newBeam.calcBendingMomentEq()
newBeam.calcSupportReac()
newBeam.calcShearForceEq()
newBeam.calcBendingMomentEq()
newBeam.calcDeflection()
newBeam.maxDeflection()
newBeam.maxBendingStress()
newBeam.printLoadEquation()
newBeam.printShearForceEquation()
newBeam.printBendingMomentEquation()
newBeam.plotLoadEq()
newBeam.plotShearEq()
newBeam.plotBendingMomentEq()
newBeam.plotDeflection()
