```python
import unittest
from CongressConnect.features.legislative_tracking import Legislation, updateLegislation

class TestLegislativeTracking(unittest.TestCase):

    def setUp(self):
        self.legislation = Legislation('Bill 1', 'Assigned', 'Voting Record 1', 'Calendar 1')
        self.updated_legislation_data = {
            'bill': 'Bill 1 Updated',
            'assignment': 'Assigned Updated',
            'voting_record': 'Voting Record 1 Updated',
            'calendar': 'Calendar 1 Updated'
        }

    def test_update_legislation(self):
        updateLegislation(self.legislation, self.updated_legislation_data)
        self.assertEqual(self.legislation.bill, self.updated_legislation_data['bill'])
        self.assertEqual(self.legislation.assignment, self.updated_legislation_data['assignment'])
        self.assertEqual(self.legislation.voting_record, self.updated_legislation_data['voting_record'])
        self.assertEqual(self.legislation.calendar, self.updated_legislation_data['calendar'])

if __name__ == '__main__':
    unittest.main()
```