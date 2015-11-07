#/usr/bin/python3

from celery import Celery

# define our celery-application
# ..make sure to include the broker!
app = Celery('tasks', broker='redis://localhost')

# a very simple celery task
# that will simply add two numbers together.
@app.task
def add(x, y):
	return x + y