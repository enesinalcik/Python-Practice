

def even_list(l):
	
	even_lis = []
	for i in range(0,len(l)):
		if l[i] % 2 == 1 :
			even_lis.append(l[i]) 
	return even_lis

result = even_list([10,9,27,55])
print("RESULT:")
print(result)