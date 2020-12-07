from locust import HttpUser, TaskSet, task
import random
import json


class SampleTask(TaskSet):
	@task
	def post_stress(self):
		searchstr = {'str':'I love America'}
		self.client.post("/http://0.0.0.0:5000/text", data=searchstr)



class stressTest(HttpUser):
	tasks = [SampleTask]
	max_wait = 5000
	host="http://0.0.0.0:5000/text"
