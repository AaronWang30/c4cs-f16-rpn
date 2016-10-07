import unittest
import rpn
class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate("1 1 +")
		self.assertEqual(2, result)
	def test_substract(self):
		result = rpn.calculate("5 3 -")
		self.assertEqual(2, result)
	def test_mul(self):
		result = rpn.calculate("2 1 *")
		self.assertEqual(2, result)
	def test_div(self):
		result = rpn.calculate("3 2 /")
		self.assertEqual(1.5, result)
	def test_exp(self):
		result = rpn.calculate("3 2 ^")
		self.assertEqual(9, result)
	def test_toomanythings(self):
			with self.assertRaises(TypeError):
				rpn.calculate("1 2 3 +")