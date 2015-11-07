@app.task(bind=True)
def random_site(self):
	try:
		res = requests.get('https://voat.co/random')
	except requests.RequestException as e:
		raise self.retry(exc=e, countdown=5)
	return res.content.decode('utf-8')
