
from app.models import Post,User,Comment
from app import db
import unittest

class PosTest(unittest.TestCase):
    '''
    Creating n instance of User and pitch and pass it
    '''
    def setUp(self):
        self.new_post = Post( body='input your personal blog here')

    def tearDown(self):
        Post.query.delete()
  

    def test_check_instance_variable(self):
        self.assertEquals(self.new_post.body,'input your personal blog here')

    def test_save_post(self):
        self.new_post.save_post()
        self.assertTrue(len(Post.query.all())>0)

class CommentTest(unittest.TestCase):
    def setUp(self):
        self.new_comment = Comment(comment = 'addyour comment here')

    def tearDown(self):
        Comment.query.delete()

    def test_check_instance_variable(self):
        self.assertAlmostEquals(self.new_comment,'addyour comment here')

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)


       