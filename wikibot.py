import wikipedia
 
x = input("> ")

# Python code to convert string to list
def Convert(string):
	li = list(string.split(" "))
	return li

# Driver code	
list1 = wikipedia.page(x).summary



print(max(Convert(list1), key=lambda s: (len(s), s)))