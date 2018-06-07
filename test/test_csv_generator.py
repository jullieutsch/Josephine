import unittest
import modules.csv_generator
class TestCSVGenerator(unittest.TestCase):
	
	@classmethod
	def setUp(self):
		self.csv_generator = modules.csv_generator

	def test_generate_csv_from_dict(self):
		dict = {'2016-11-10': 63361, '2014-08-08': 477, '2016-06-01': 38473, '2017-03-18': 2586, '2016-07-08': 31007, '2014-06-05': 8939, '2016-06-23': 17330, '2016-04-25': 12139, '2015-08-06': 2944, '2017-08-17': 7667, '2018-04-08': 2617, '2016-07-02': 5316}

		self.csv_generator.generate_csv_from_dict(dict)

if __name__ == '__main__':
	unittest.main()