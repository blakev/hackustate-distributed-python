@app.task
def xsum(data):
	return sum(map(int, data))
	