def simple_func(*args):
	
	if not args:
		print("No arguments")
		
			
	if len(args) == 1:
		print(args)

	else:		
		list = {}
		for arg in args:
			if type(arg) not in list.keys():
				list[type(arg)] = 1
			else:
				list[type(arg)] +=1
		print(list)




simple_func(22.5, 'name', 13, 'alex', 2.1, 3.4, 'home')


