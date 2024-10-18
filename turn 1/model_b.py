import unittest


class TestDataProcessing(unittest.TestCase):

    def setUp(self):
        # Dummy data with some values violating constraints
        self.dummy_data = [
            {"name": "Alice", "age": -2},  # Age constraint violation
            {"name": "Bob", "age": 150},  # Age constraint violation
            {"name": "Charlie", "age": 30},  # Valid data
            {"name": "", "age": 25},  # Name constraint violation
        ]

    def test_age_constraint(self):
        for entry in self.dummy_data:
            # Assuming the 'age' constraint is between 0 and 100
            self.assertTrue(0 <= entry["age"] <= 100, f"Age constraint violated for {entry['name']}")

    def test_name_constraint(self):
        for entry in self.dummy_data:
            # Assuming the 'name' field should not be empty
            self.assertTrue(entry["name"].strip(), f"Name constraint violated for {entry['name']}")


if __name__ == "__main__":
    unittest.main()
