```python
import unittest
from CongressConnect.features.data_security_compliance import DataSecurityCompliance

class TestDataSecurityCompliance(unittest.TestCase):

    def setUp(self):
        self.data_security_compliance = DataSecurityCompliance()

    def test_role_based_access_control(self):
        self.assertTrue(self.data_security_compliance.role_based_access_control('admin'))
        self.assertFalse(self.data_security_compliance.role_based_access_control('guest'))

    def test_data_encryption(self):
        plain_text = "CongressConnect"
        encrypted_text = self.data_security_compliance.encrypt_data(plain_text)
        decrypted_text = self.data_security_compliance.decrypt_data(encrypted_text)
        self.assertEqual(plain_text, decrypted_text)

    def test_audit_trails(self):
        self.data_security_compliance.log_action('admin', 'delete', 'user', 'john_doe')
        self.assertIn('admin', self.data_security_compliance.audit_trail)
        self.assertIn('delete', self.data_security_compliance.audit_trail)
        self.assertIn('user', self.data_security_compliance.audit_trail)
        self.assertIn('john_doe', self.data_security_compliance.audit_trail)

    def test_compliance_standards(self):
        self.assertTrue(self.data_security_compliance.check_compliance('GDPR'))
        self.assertFalse(self.data_security_compliance.check_compliance('NonExistentStandard'))

if __name__ == '__main__':
    unittest.main()
```