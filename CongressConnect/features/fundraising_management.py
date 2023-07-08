```python
from datetime import datetime
from .database_development import Database
from .backend_development import UserSchema, CampaignSchema

class FundraisingManagement:
    def __init__(self):
        self.db = Database()
        self.currentCampaign = None

    def maintain_donor_info(self, donor_info):
        self.db.insert('donors', donor_info)

    def track_campaign(self, campaign_id):
        self.currentCampaign = self.db.query('campaigns', {'id': campaign_id})

    def send_receipt(self, donor_id, amount, campaign_id):
        donor = self.db.query('donors', {'id': donor_id})
        campaign = self.db.query('campaigns', {'id': campaign_id})
        receipt = {
            'donor': donor,
            'campaign': campaign,
            'amount': amount,
            'date': datetime.now()
        }
        self.db.insert('receipts', receipt)

    def analyze_performance(self, campaign_id):
        campaign = self.db.query('campaigns', {'id': campaign_id})
        receipts = self.db.query('receipts', {'campaign_id': campaign_id})
        total_donations = sum([receipt['amount'] for receipt in receipts])
        return {
            'campaign': campaign,
            'total_donations': total_donations,
            'average_donation': total_donations / len(receipts) if receipts else 0
        }

    def updateCampaign(self, campaign_id, updates):
        self.db.update('campaigns', {'id': campaign_id}, updates)
        self.currentCampaign = self.db.query('campaigns', {'id': campaign_id})

fundraising_management = FundraisingManagement()
```