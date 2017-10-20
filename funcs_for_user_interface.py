def getValuesForNewBeam(builder,pinjoint,cantilever):
	resultantDictionary={}
	resultantDictionary['Length']=int(builder.get_object('Length_Of_Beam').get_text())
	resultantDictionary['E']=float(builder.get_object('Youngs_Modulus').get_text())
	if(pinjoint):
		resultantDictionary['Support-Type']='pin joint'
	else:
		resultantDictionary['Support-Type']='cantilever'
	builder.get_object('Length_Of_Beam').set_text('Value Set')
	builder.get_object('Youngs_Modulus').set_text('Value Set')
	return resultantDictionary
def getValuesForDiscreteForce(builder):
	resultantDictionary={}
	resultantDictionary['Distance']=int(builder.get_object('Distance_Of_Discrete_Force').get_text())
	print(builder.get_object('Distance_Of_Discrete_Force').get_text())
	resultantDictionary['Magnitude']=int(builder.get_object('Magnitude_Of_Discrete_Force').get_text())
	print(builder.get_object('Magnitude_Of_Discrete_Force').get_text())
	builder.get_object('Distance_Of_Discrete_Force').set_text('')
	builder.get_object('Magnitude_Of_Discrete_Force').set_text('')
	return resultantDictionary