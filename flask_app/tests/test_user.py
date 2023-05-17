import unittest
import json
from flask_app import create_app

class UserTestVase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.user = {
            'id': '1',
            'name': 'Turk',
            'email': 'turk@turkleton.us'
        }

    def test_create_User(self):
        res = self.client().post('/api/v1/user', headers={'Content-Type': 'application/json'}, data=json.dumps(self.user))
        self.assertEqual(res.status_code, 201)
        self.assertIn('Turk', str(res.data))

    def test_get_user(self):
        res = self.client().post('/api/v1/user', headers={'Content Type': 'application/json'}, data=json.dumps(self.user))
        res = self.client().get('/api/v1/user/1')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Turk', str(res.data))

    def test_get_user_not_found(self):
        res = self.client().get('/api/v1/user/1000')
        self.assertEqual(res.status_code, 404)

if __name__ == '__main__':
    unittest.main()
        