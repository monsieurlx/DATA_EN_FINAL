from locust import HttpUser, TaskSet, task
import random
import json


class SampleTask(TaskSet):
	@task
	
	def post_stress(self):
		searchstr = {'str':'I love America'}
		self.client.get("/text",data=searchstr)



class stressTest(HttpUser):
	tasks = [SampleTask]
	min_wait = 60
	#max_wait = 10000
	host=("http://0.0.0.0:5000")
