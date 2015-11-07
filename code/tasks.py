#/usr/bin/python3
# tasks.py
from celery import Celery

# define our celery-application
# ..make sure to include the broker!
# We also want to make sure we're storing the results.
app = Celery('tasks', broker='redis://localhost', backend='redis://localhost')

# a very simple celery task
# that will simply add two numbers together.
@app.task
def add(x, y):
	return x + y