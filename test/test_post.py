from app.models import Post,User
from app import db
import unittest

class PosTest(unittest.TestCase):
    '''
    Creating n instance of User and pitch and pass it
    '''
    def setUp(self):
        self.user_Melo = User(username = 'melo',password='1234',email = 'melo@gmail.com')
        self.new_post = Post( body='input your personal blog here',user = self.user_Melo)

    def tearDown(self):
        Post.query.delete()
        User.query.delete()

    def test_check_instance_variable(self):
        self.assertEquals(self.new_post.body,'input your personal blog here')
        self.assertEquals(self.new_post.user,self.user_Melo)

    def test_save_post(self):
        self.new_pitch.save_post()
        self.assertTrue(len(Post.query.all())>0)
