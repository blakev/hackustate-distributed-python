@app.task
def page_size(data):
	if not isinstance(data, basestring):
		try:
			data = bytes(data).decode('utf-8')
		except Exception:
			return 0
	return len(data)
	