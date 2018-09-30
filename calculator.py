#计算器类
class Count(object):
	'''docstring for count'''
	def __init__(self, a,b):
		self.a = int(a)
		self.b = int(b)

	#加法
	def add(self):
		return self.a + self.b

	#减法
	def  sub(self):
		return self.a - self.b
