```python
import unittest
from CongressConnect.features.communication_outreach import CommunicationOutreach

class TestCommunicationOutreach(unittest.TestCase):

    def setUp(self):
        self.communication_outreach = CommunicationOutreach()

    def test_send_newsletter(self):
        result = self.communication_outreach.send_newsletter("Test Newsletter", "This is a test newsletter.")
        self.assertEqual(result, "Newsletter sent successfully.")

    def test_send_press_release(self):
        result = self.communication_outreach.send_press_release("Test Press Release", "This is a test press release.")
        self.assertEqual(result, "Press release sent successfully.")

    def test_send_update(self):
        result = self.communication_outreach.send_update("Test Update", "This is a test update.")
        self.assertEqual(result, "Update sent successfully.")

    def test_email_marketing(self):
        result = self.communication_outreach.email_marketing("Test Email", "This is a test email.")
        self.assertEqual(result, "Email sent successfully.")

    def test_social_media_outreach(self):
        result = self.communication_outreach.social_media_outreach("Test Post", "This is a test post.")
        self.assertEqual(result, "Post published successfully.")

    def test_monitor_public_perception(self):
        result = self.communication_outreach.monitor_public_perception("Test Post")
        self.assertEqual(result, "Public perception monitored successfully.")

if __name__ == '__main__':
    unittest.main()
```