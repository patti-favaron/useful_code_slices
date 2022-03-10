# Algebraic-only implementation of two's complement in pure Python
#
# Written by: Patrizia Favaron

def raw_to_compl2(iRaw, iNumBits):

	# Establish minimum and maximum possible raw values
	iMinRaw = 0
	iMaxRaw = 2**iNumBits - 1
	
	# Clip value arithmetically
	if iRaw < iMinRaw:
		iRaw = iMinRaw
	if iRaw > iMaxRaw:
		iRaw = iMaxRaw
		
	# Set useful two's complement value(s)
	iMaxValue =  2**(iNumBits-1) - 1
	
	# Check cases and act accordingly
	if iRaw <= iMaxValue:
		iValue = iRaw
	else:
		iValue = iRaw - 2**iNumBits
		
	return iValue
	
	
def compl2_to_raw(iCompl2, iNumBits):

	# Set minimum and maximum two's complement values
	iMinValue = -2**(iNumBits-1)
	iMaxValue =  2**(iNumBits-1) - 1
	
	# Clip value arithmetically
	if iCompl2 < iMinValue:
		iCompl2 = iMinValue
	if iCompl2 > iMaxValue:
		iCompl2 = iMaxValue
		
	# Check cases and set accordingly
	if iCompl2 >= 0:
		iRaw = iCompl2
	else:
		iRaw = iCompl2 + 2**iNumBits
		
	return iRaw


if __name__ == "__main__":

	iRaw = 0
	print(iRaw)
	print(raw_to_compl2(iRaw,16))
	print()
	iRaw = 32767
	print(iRaw)
	print(raw_to_compl2(iRaw,16))
	print()
	iRaw = 32768
	print(iRaw)
	print(raw_to_compl2(iRaw,16))
	print()
	iRaw = 65535
	print(iRaw)
	print(raw_to_compl2(iRaw,16))
	print()
	
	iCompl2 = -1
	print(iCompl2)
	print(compl2_to_raw(iCompl2,10))
	print()
	
	iCompl2 = -2**9
	print(iCompl2)
	print(compl2_to_raw(iCompl2,10))
	print()
	
	iCompl2 = -2**9 + 1
	print(iCompl2)
	print(compl2_to_raw(iCompl2,10))
	print()
	
