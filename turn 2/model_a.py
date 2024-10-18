import unittest
from parameterized import parameterized


class TestDataProcessing(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.constraints = {
            "age": {"min": 0, "max": 100},
            "name": {"min_length": 1},
        }
        cls.test_data = [
            {"name": "Alice", "age": -2},
            {"name": "Bob", "age": 150},
            {"name": "Charlie", "age": 30},
            {"name": "", "age": 25},
        ]

    @parameterized.expand([
        ("age", "Age constraint violated for {entry['name']}"),
        ("name", "Name constraint violated for {entry['name']}")
    ])
    def test_constraint(self, constraint_name, error_msg_template):
        for entry in self.test_data:
            constraint = self.constraints[constraint_name]
            if constraint_name == "age":
                self.assertTrue(constraint["min"] <= entry["age"] <= constraint["max"],
                                error_msg_template.format(entry=entry))
            elif constraint_name == "name":
                self.assertTrue(len(entry["name"].strip()) >= constraint["min_length"],
                                error_msg_template.format(entry=entry))


if __name__ == "__main__":
    unittest.main()
