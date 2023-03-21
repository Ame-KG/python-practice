num = 2
lisst = [10, 9, 8, 7, 11]

# Lambda function to double a number
multiplyer = lambda num: print(num * 2)
multiplyer(num)

# Lambda function/mapping to double every item in a list
x2 = map(lambda num: num * 2, lisst)
print(list(x2))

# regular funtion to double a number
def doubler(num):
	print('normal func!!!')
	print(num * 2)

# regular functions to double every item in a list
def list_doubler(list):
	new = []
	for i in list:
		a = i * 2
		new.append(a)
	print(new)

doubler(num)
list_doubler(lisst)
