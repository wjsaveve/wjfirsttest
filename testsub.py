from calculator import Count
import unittest

class TestSub(unittest.TestCase):
	'''这是减法测试类'''

	def setUp(self):
		print("testsub start")

	def tearDown(self):
		print("testsub end")

	def test_sub(self):
		'''这是减法测试用例1'''
		j = Count(2,3)
		self.assertEqual(j.sub(),-1)

	def test_sub2(self):
		j = Count(3,4)
		self.assertEqual(j.sub(),-1)

if __name__ == '__main__':
	unittest.main()