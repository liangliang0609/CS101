# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

#def find_element(p,q):
 #   for e in p:
  #      if e == q:
   #         a = p.index(e)
    #        return a
     #   else:
      #      a = -1
    #return a
        

def find_element(p,t):
	i = 0
	while i < len(p):
		if p[i] == t:
			return i
		i = i + 1
	return -1

def find_element(p,t):
	i = 0
	for e in p:
		if e == t:
			return i
		i = i + 1
	return -1


#print (find_element([1,2,3],3)
#>>> 2

print(find_element(['alpha','beta'],'gamma'))
#>>> -1