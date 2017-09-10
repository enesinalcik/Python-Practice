

def string(s1,s2):

	empty_string = ""
	for i in range(0,len(s1)):
		empty_string += s1[i] + " "
	empty_string +=" "
	for j in range(0,len(s2)):
		empty_string += s2[j] + " "

	return empty_string

result = string("Muhammed","Enes")
print(result)

	