import unittest 
from app.models import Post

class test_postModel(unittest.TestCase):



    def setUp(self):
        
        self.new_post = Post(title = 'test', description = 'motherhood',user_id =  1, category = 'music',author='evelyne')

    def test_check_instance_variables(self):
        self.assertEquals(self.new_post.title, 'test')
        self.assertEquals(self.new_post.content, 'testing is important' )
        self.assertEquals(self.new_post.user_id, 1)
        self.assertEquals(self.new_post.category, 'music')
        self.assertEquals(self.new_post.author, 'evelyne')

    def tearDown(self):
        Post.query.delete()
        User.query.delete()
    
    def test_save_post(self):
        self.new_post.save_post()
        self.assertTrue(len(Post.query.all()),1)

    def test_delete_post(self):
        self.new_post.delete_post()
        self.assertTrue(len(Post.query.all()),0)
