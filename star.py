
def star(n,m):
	

	for i in range(0,n):
		empty_string = ""
		empty_string += (n - i) * " " + i * "*"
		print(empty_string)	
	for j in range(1,m + 1):
		empty_string2 = ""
		empty_string2 += j * " " + (m - j) * "*" 
		print(empty_string2)
	return
	
star(20,20)