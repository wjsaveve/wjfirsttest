from calculator import Count
import unittest

class TestAdd(unittest.TestCase):

	def setUp(self):
		print("testadd start")

	def tearDown(self):
		print("testadd end")

	def test_add(self):
		j = Count(2,3)
		self.assertEqual(j.add(),5)

	def test_add2(self):
		j = Count(3,4)
		self.assertEqual(j.add(),7)

if __name__ == '__main__':
	unittest.main()