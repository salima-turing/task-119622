import unittest
import json

class TestDataProcessing(unittest.TestCase):

    def setUp(self):
        # Load test data from a centralized JSON file
        with open('test_data.json', 'r') as f:
            self.test_data = json.load(f)

    @parameterized.expand(test_data)
    def test_data_processing(self, name, input_data, expected_output, constraints):
        # Your data processing logic goes here
        result = process_data(input_data)
        
        # Validate the result against expected output and constraints
        self.assertEqual(result, expected_output)
        for constraint in constraints:
            self.assertTrue(constraint(result), f"Constraint violated for {name}")

if __name__ == "__main__":
    unittest.main()
