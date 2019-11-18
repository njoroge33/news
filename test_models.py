import unittest
from models import Source, Article

class TestSource(unittest.TestCase):
		'''
		Test Case to test the behaviour of the Source Model
		Args:
			unittest.TestCase - helps in creating Test Cases
		'''
		def setUp(self):
			'''
			Inbuilt function that runs before each test is executed
			'''
			self.new_source = Source("abc-news","ABC News","Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.", "https://abcnews.go.com", "general", "en", "us")

		def test_isSourceInstance(self):
			'''
			Function to test if the object created in the setup is indeed a Source Object
			'''
			self.assertTrue(isinstance(self.new_source,Source))

class TestArticle(unittest.TestCase):
		'''
		Test Case to test the behaviour of the Article Model
		Args:
			unittest.TestCase - helps in creating Test Cases
		'''
		def setUp(self):
			'''
			Inbuilt function that runs before each test is executed
			'''
			self.new_article = Article("Panos Mourdoukoutas, Contributor, Panos Mourdoukoutas, Contributor https://www.forbes.com/sites/panosmourdoukoutas/", "XRP Keeps On Rallying, As Bitcoin, ETH, And XLM Are Catching Up -- What's Next?", "Bitcoin, XRP, ETH, XLM rise, shaking off bad news--watch BTC and ETH price action for what comes next.", "https://www.forbes.com/sites/panosmourdoukoutas/2019/10/13/xrp-keeps-on-rallying-as-bitcoin-eth-and-xlm-are-catching-up-whats-next/", "https://thumbor.forbes.com/thumbor/600x315/https%3A%2F%2Fspecials-images.forbesimg.com%2Fdam%2Fimageserve%2F915943332%2F960x0.jpg%3Ffit%3Dscale", "2019-10-13T11:48:00Z")

		def test_isArticleInstance(self):
			'''
			Function to test if the object created in the setup is indeed a Source Object
			'''
			self.assertTrue(isinstance(self.new_article,Article))

if __name__ == '__main__':
	unittest.main()