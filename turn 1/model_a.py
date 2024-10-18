import unittest

class TestDataProcessing(unittest.TestCase):

	def test_check_constraints_are_met(self):
		# Dummy data
		data = [
			{"age": 30, "income": 70000},
			{"age": 25, "income": 50000},
			{"age": 40, "income": 90000},
		]

		max_age = 65
		min_income = 30000

		for entry in data:
			age = entry.get("age")
			income = entry.get("income")

			# Assertions to check for constraints
			self.assertIsNotNone(age, "Age should not be none")
			self.assertIsNotNone(income, "Income should not be none")
			self.assertLessEqual(age, max_age, "Age should be less than or equal to maximum age")
			self.assertGreaterEqual(age, 0, "Age should be non-negative")
			self.assertGreaterEqual(income, min_income, "Income should be greater than or equal to minimum income")

if __name__ == '__main__':
	unittest.main()
