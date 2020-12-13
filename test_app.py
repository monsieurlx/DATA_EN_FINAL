import unittest
import requests
import os
import time


class Testing(unittest.TestCase):

#Beginning of the test

	def setUP(self):
	
		os.environ['NO_PROXY'] = '0.0.0.0'


	def test_request_success(self):
	
		searchstr = {'nm' : 'I love America'}
		responce = requests.post('http://0.0.0.0:5000/text',data=searchstr)
		self.assertEqual(responce.status_code,200) 
		
	#def test_return_content(self):
	
		#self.asserIsNotNone(responce.content)
		#self.assertRegex(responce.content, '[A-Z]')
		
	#def test_no(self):
	#	self.asserEqual(responce.content,'no similar tweet found for now')
	
	
	
	
if __name__ == '__main__':
	unittest.main()
#End of the test

	def tearDown(self):
		pass
		
