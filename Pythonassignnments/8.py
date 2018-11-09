tuple_a = ('Dog', 'Cat', 'Monkey', 'Elephant')
tuple_b = ('India ', 'Korea', 'China', 'Russia')
my_list = list(zip(tuple_a,tuple_b))

for val in range(len(my_list)):
	print (my_list[val])


