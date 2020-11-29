import unittest

from flaskapp import app
from redis import Redis

class CounterTest(unittest.TestCase):
	def setUp(self):
		#pass
		self.app = app.test_client()
	def tearDown(self):
		pass
	#Test on the welcome page
	def test_welcome_pages(self):
		response= self.app.get('/')
		self.assertEqual(response.status_code, 200)
	#Test for the visit page
	def test_redis_connexion(self):
		redis=Redis(host="redis-server", db=0)
		self.app.get('/visit')
		self.app.get('/visit')
		self.app.get('/visit')
		self.app.get('/visit')
		self.app.get('/visit')
		self.assertEqual(int(redis.get("counter")),1)

if __name__ == "__main__":
	unittest.main()