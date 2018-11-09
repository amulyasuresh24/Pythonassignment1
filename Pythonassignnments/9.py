''' Implement a program to create a dictionary of students with Registration number and names. Perform the two operations, insert and delete.''' 
dict = {'181040003':'LUFY', '181040004':'YAGAMI', '181040005':'DOMINJOON', '181040006':'JUMIN'}
print("created dictionary:\n",dict)
dict['181040006']='ZOYA'
print("Dictionary after inserting",dict)
del dict['181040003'] 
print("Dictionary after deletion",dict)