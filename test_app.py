import unittest
import requests
import os
import langdetect
import time


class Testing(unittest.TestCase):

#Beginning of the test

	def setUP(self):
	
		os.environ['NO_PROXY'] = '0.0.0.0'


	def test_input_string(self):
	
		searchstr = {'nm' : 'I love America'}
		responce = requests.post('http://0.0.0.0:5000/text',data=searchstr)
		self.assertEqual(responce.status_code,200) #Check if request was a success

	
if __name__ == '__main__':
	unittest.main()
#End of the test

	def tearDown(self):
		pass
		
