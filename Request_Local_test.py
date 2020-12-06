import random 



rand=random.uniform(0.03, 0.06)

def count():
	start = 0
	end = 60
	
	c=0
	while(start<end):
	
		start = start+ rand
		c=c+1
		if (c==999):
			print(start)
			print(c)
			return c
		
	print(c)
	return c
	

count()
