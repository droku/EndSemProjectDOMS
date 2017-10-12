from sympy import *
x = Symbol('x')
def calSupportReaction(concForce,concMoment,distributedForce,distSupport,support_type):
    sumforce = 0
    summoment = 0
    for i in range(0,len(concForce)):
        sumforce += concForce[i][0]
        summoment += concForce[i][0]*concForce[i][1]
    for i in range(0,len(concMoment)):
        summoment += concMoment[i][0]
    for i in range(0,len(distributedForce)):
        sumforce += N(integrate(distributedForce[i][0],(x,distributedForce[i][1],distributedForce[i][2])))
        summoment += N(integrate(x*distributedForce[i][0],(x,distributedForce[i][1],distributedForce[i][2])))
    if support_type is 'pinjoint':
        reaction2 = -(summoment)/float(distSupport[1])
        reaction1 = -(sumforce) - reaction2
        return [reaction1,reaction2]
    if support_type is 'cantilever':
        reaction_moment = -(summoment)
        reaction_force = -(sumforce)
        return [reaction_moment,reaction_force]

concForce =[]
concMoment = []
distributedForce = []
distSupport = []
distSupport.append(0)
distSupport.append(6)
distributedForce.append([20*x,0,6])
support_type = 'pinjoint'
reaction_forces = calSupportReaction(concForce,concMoment,distributedForce,distSupport,support_type)
print(reaction_forces)
    
