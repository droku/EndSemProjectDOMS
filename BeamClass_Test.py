from BeamClass import *
newBeam=Beam(10,'pinjoint')
newBeam.getDiscreteForce(3,10)
newBeam.getDiscreteForce(5,10)
newBeam.getContinuousForce(6,8,'3x^2')
newBeam.getBendingMoment(2,9)
newBeam.calcShearForceEq()
newBeam.calcBendingMomentEq()
newBeam.printLoadEquation()
newBeam.printShearForceEquation()
newBeam.printBendingMomentEquation()
newBeam.calSupportReaction()

