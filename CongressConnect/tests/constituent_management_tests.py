```python
import unittest
from CongressConnect.features.constituent_management import ConstituentManagement

class TestConstituentManagement(unittest.TestCase):

    def setUp(self):
        self.constituent_management = ConstituentManagement()

    def test_centralize_constituent_info(self):
        self.constituent_management.centralize_constituent_info()
        self.assertIsNotNone(self.constituent_management.currentConstituent)

    def test_segment_based_on_demographics(self):
        self.constituent_management.segment_based_on_demographics('age')
        self.assertIsNotNone(self.constituent_management.currentConstituent)

    def test_engage_via_personalized_communication_channels(self):
        self.constituent_management.engage_via_personalized_communication_channels('email')
        self.assertTrue(self.constituent_management.currentConstituent['engaged'])

    def test_track_and_address_constituent_concerns(self):
        self.constituent_management.track_and_address_constituent_concerns('concern1')
        self.assertTrue(self.constituent_management.currentConstituent['concerns']['concern1']['addressed'])

if __name__ == '__main__':
    unittest.main()
```