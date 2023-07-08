```python
import unittest
from CongressConnect.features.fundraising_management import FundraisingManagement

class TestFundraisingManagement(unittest.TestCase):

    def setUp(self):
        self.fundraising = FundraisingManagement()

    def test_maintain_donor_information(self):
        donor_info = {
            "name": "John Doe",
            "email": "johndoe@example.com",
            "donation_amount": 500
        }
        self.fundraising.maintain_donor_information(donor_info)
        self.assertEqual(self.fundraising.donors[0], donor_info)

    def test_track_campaigns(self):
        campaign_info = {
            "campaign_name": "Campaign 1",
            "target_amount": 10000,
            "raised_amount": 5000
        }
        self.fundraising.track_campaigns(campaign_info)
        self.assertEqual(self.fundraising.campaigns[0], campaign_info)

    def test_send_donor_receipts(self):
        donor_info = {
            "name": "John Doe",
            "email": "johndoe@example.com",
            "donation_amount": 500
        }
        receipt = self.fundraising.send_donor_receipts(donor_info)
        self.assertEqual(receipt['donor_name'], donor_info['name'])
        self.assertEqual(receipt['donation_amount'], donor_info['donation_amount'])

    def test_analyze_performance(self):
        campaign_info = {
            "campaign_name": "Campaign 1",
            "target_amount": 10000,
            "raised_amount": 5000
        }
        self.fundraising.track_campaigns(campaign_info)
        performance = self.fundraising.analyze_performance()
        self.assertEqual(performance['campaign_name'], campaign_info['campaign_name'])
        self.assertEqual(performance['target_amount'], campaign_info['target_amount'])
        self.assertEqual(performance['raised_amount'], campaign_info['raised_amount'])

if __name__ == '__main__':
    unittest.main()
```