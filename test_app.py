import unittest
import requests
import os


class Testing(unittest.TestCase):

	

#Beginning of the test

	def setUP(self):
	
		os.environ['NO_PROXY'] = '0.0.0.0'
		os.environ['NO_PROXY'] = '0.0.0.0/text'

		
	def test_access_web_api(self):
		resp = requests.get('http://localhost:5000/text')
		self.assertEqual(resp.status_code,200)

	def test_request_success(self):
	
		searchstr = {'nm' : 'I love America'}
		responce = requests.post('http://0.0.0.0:5000/text',data=searchstr)
		self.assertEqual(responce.status_code,200) 
		self.assertRegex(str(responce.content),'[+@+#]')
		
	def test_no_similarity(self):
		searchstr = {'nm' : 'anticonstitutionnellement'}
		responce = requests.post('http://0.0.0.0:5000/text',data=searchstr)
		self.assertEqual(responce.content,b'No tweet found')
	
def tearDown(self):
			pass
					
	
	
if __name__ == '__main__':
	unittest.main()
#End of the test

	
		
