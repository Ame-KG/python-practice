# string manipulation function()
# SLICE OPERATOR
string = 'Domain'
string2 = 'Range'
string3 = 'TrapeziuM'
string4 = 'Code'

# Reverses a string or list
def reverser(inputs):
	reversed_input = inputs[::-1]
	print(reversed_input)

# returns every other element/char
def skipper(inputs):
	manipulated = inputs[::2]
	print(manipulated)

# takes the first and last letters and prints those first then reverses te rest. Trapezium = Tmuizepar
def crazy(inputs):
	front = inputs[0]
	end =inputs[len(inputs)-1]
	mid = inputs[1:len(inputs)-1]
	mid_versed = mid[::-1]
	print(front + end + mid_versed)

# fibonaccies a string. so 'Code', becomes 'CCoCodCode'
def fibonator(word):
	new = ''
	for i in range(len(word)+1):
		hi = (word[:i])
		new += hi
	print(new)


# skipper(string)
# crazy(string)

# lambda version of the reverser
# reversr_lambda = lambda inputs: print(inputs[::-1])
# reversr_lambda(string2)
# reverser(string2)

fibonator(string4)