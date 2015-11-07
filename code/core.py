import re
import time
from celery import Celery
import requests
# define our celery-application
# ..make sure to include the broker!
# We also want to make sure we're storing the results.
app = Celery('tasks', broker='redis://localhost', backend='redis://localhost')

# a very simple celery task
# that will simply add two numbers together.
@app.task
def add(x, y):
	return x + y

@app.task
def xsum(data):
	return sum(map(int, data))

@app.task
def page_size(data):
	if not isinstance(data, str):
		try:
			data = bytes(data).decode('utf-8')
		except Exception:
			return 0
	return len(data)

@app.task(bind=True)
def random_site(self):
	try:
		res = requests.get('https://google.com')
	except requests.RequestException as e:
		raise self.retry(exc=e, countdown=5)
	return res.content.decode('utf-8')
