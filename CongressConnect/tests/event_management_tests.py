```python
import unittest
from CongressConnect.features.event_management import EventManagement

class TestEventManagement(unittest.TestCase):

    def setUp(self):
        self.event_management = EventManagement()

    def test_create_event(self):
        event_data = {
            'name': 'Town Hall',
            'location': 'City Hall',
            'date': '2022-12-12',
            'time': '18:00',
            'description': 'A town hall meeting for constituents.'
        }
        result = self.event_management.create_event(event_data)
        self.assertEqual(result['status'], 'success')

    def test_update_event(self):
        event_data = {
            'name': 'Town Hall',
            'location': 'City Hall',
            'date': '2022-12-12',
            'time': '18:00',
            'description': 'A town hall meeting for constituents.'
        }
        self.event_management.create_event(event_data)
        updated_event_data = {
            'name': 'Town Hall',
            'location': 'City Hall',
            'date': '2022-12-13',
            'time': '18:00',
            'description': 'A town hall meeting for constituents.'
        }
        result = self.event_management.update_event(updated_event_data)
        self.assertEqual(result['status'], 'success')

    def test_delete_event(self):
        event_data = {
            'name': 'Town Hall',
            'location': 'City Hall',
            'date': '2022-12-12',
            'time': '18:00',
            'description': 'A town hall meeting for constituents.'
        }
        self.event_management.create_event(event_data)
        result = self.event_management.delete_event('Town Hall')
        self.assertEqual(result['status'], 'success')

    def test_get_event(self):
        event_data = {
            'name': 'Town Hall',
            'location': 'City Hall',
            'date': '2022-12-12',
            'time': '18:00',
            'description': 'A town hall meeting for constituents.'
        }
        self.event_management.create_event(event_data)
        result = self.event_management.get_event('Town Hall')
        self.assertEqual(result['name'], 'Town Hall')

if __name__ == '__main__':
    unittest.main()
```