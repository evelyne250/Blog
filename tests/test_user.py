import unittest 
from app.models import User

class test_userModel(unittest.TestCase):

    # to test behaivours in the user model

    def setUp(self):
        self.new_user = User(password='mypassword')


    def  test_check_password(self):
        
        self.assertTrue(self.new_user.check_password('mypassword'))

    def test_save_user(self):

        self.user_Me = User(username = 'eve', password = 'eve', email = 'uevelyne@gmail.com')
        # self.user_Me.save()
        self.assertTrue(len(User.query.all()),1)

    def test_delete_user(self):
        self.user_Me = User(username = 'eve', password = 'eve', email = 'uevelyne@gmail.com')
        self.user_Me.save()
        self.me = User(username='eve',password='eve',email='uevelyne@gmail.com')
        self.me.save()
        self.me.delete()
        self.assertTrue(len(User.query.all()),1)