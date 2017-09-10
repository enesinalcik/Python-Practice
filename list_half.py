
def list_half(h):

	halfed_lis = []

	for i in range(0,len(h)):
		a = h[i] / 2
		halfed_lis.append(a)
	return halfed_lis

result = list_half([1,2,3,4,5,6,7,8,9])
print("Halfed List")
print(result)	