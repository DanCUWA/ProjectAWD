import unittest, os
from app import app, db
from app.models import User, Settings, GameRoom, Prompts, Message

# unit test case for the project
class TestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.getcwd(), 'test.db')
        self.app = app.test_client()
        db.create_all()
        u1 = User(id = '12345', username = 'test', roomId = '54321')
        db.session.add(u1)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User.query.get('12345')
        u.set_password('password')
        self.assertFalse(u.check_password('wrong_password'))
        self.assertTrue(u.check_password('password'))

    def test_user_repr(self):
        u = User.query.get('12345')
        self.assertEqual(str(u), '<User test, Room 54321>')

    def test_settings_repr(self):
        s = Settings.query.get('test')
        self.assertEqual(str(s), '<User test, primaryColor #3F3747, secondaryColor #26282B, textColor #ffffff>')

    def test_gameroom_repr(self):
        g = GameRoom.query.get('54321')
        self.assertEqual(str(g), '<User test, Room access 54321, roomName testRoom, playerNumber 1, turnNumber 1>')

    def test_login_page(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Log In', response.data)

    def test_register_page(self):
        response = self.app.get('/register')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Register', response.data)

    def test_login_valid_credentials(self):
        response = self.app.post('/login', data={'email': 'user@example.com', 'password': 'password'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual('user')

    def test_login_invalid_credentials(self):
        response = self.app.post('/login', data={'user': 'username', 'password': 'wrong_password'}, follow_redirects=True)
        self.assertIn(b'Invalid username or password.', response.data)
        self.assertNotIn('user')

    def test_existing_user(self):
        response = self.app.post('/register', data={'reg_user': 'username', 'reg_password': 'password'}, follow_redirects=True)
        self.assertIn(b'A user with this username already exists.', response.data)
        self.assertNotIn('user')

    def test_register_new_user(self):
        response = self.app.post('/register', data={'reg_email': 'new@example.com', 'reg_password': 'password'}, follow_redirects=True)
        self.assertIn(b'Account created successfully!', response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please log in.', response.data)

    def test_logout(self):
        with self.app:
            self.app.post('/login', data={'email': 'test@example.com', 'password': 'password'}, follow_redirects=True)
            response = self.app.get('/logout', follow_redirects=True)
            self.assertIn(b'You have been logged out.', response.data)
            self.assertNotIn('user')

    def test_main_page_without_login(self):
        response = self.app.get('/main', follow_redirects=True)
        self.assertIn(b'Please log in.', response.data)

    def test_main_page_with_login(self):
        with self.app:
            self.app.post('/login', data={'user': 'username', 'password': 'password'}, follow_redirects=True)
            response = self.app.get('/main')
            self.assertIn(b'Welcome, username', response.data)

if __name__ == '__main__':
    unittest.main()