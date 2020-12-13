import unittest
import requests
import os
import time


class Testing(unittest.TestCase):

#Beginning of the test

	def setUP(self):
	
		os.environ['NO_PROXY'] = '0.0.0.0'
		os.environ['NO_PROXY'] = '0.0.0.0/text'

	def web_api_accessible(self):
		resp = requests.get('http://0.0.0.0:5000/text')
		self.assertEqual(resp.status_code,200)

	def test_request_success(self):
	
		searchstr = {'nm' : 'I love America'}
		responce = requests.post('http://0.0.0.0:5000/text',data=searchstr)
		self.assertEqual(responce.status_code,200) 
		self.assertRegex(str(responce.content),'[+@+#]')
		
	#def test_no(self):
	#	self.asserEqual(responce.content,'no similar tweet found for now')
	
	def tearDown(self):
		pass	
	
	
if __name__ == '__main__':
	unittest.main()
#End of the test

	
		
