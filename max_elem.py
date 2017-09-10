###### M. Enes İnalcık ###### 09.09.2017 ######



def list_maker(l):
	long_list = []
	for i in range(0,l):
		long_list.append(i + 1)
	return long_list
		
result = list_maker(10)



def max_element(m):

	max_elem = m[0]
	for x in range(0,len(m)):
		if m[x] > max_elem :
			max_elem = m[x]
	return max_elem
	
print ("Random Max Element")
print(max_element(result))

"""
print("Your Max Element List")
print(max_element([1,2,3,4,5])
"""