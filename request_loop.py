import random 
import requests




def count():
	start = 0
	end = 60
	c=0
	rand=random.uniform(0.04, 0.06) #Set to 0.06 only if we want exactly 1000/min
	url = 'http://localhost:5000/text'
	nm = 'I love America'
	
	while(start<end):
		
		requests.post(url, data=nm)
		resp = requests.get(url)
		start = start+ rand
		c=c+1

		if resp.status_code != 200:
			print('Failed to handle request : {} '.format(c))
			return c
		
		
		if (c==999):
			print(start)
			print('Successfully withstand 1000 requests ! But I guess they are all still waiting for their results')
			return c

	return False


count()
