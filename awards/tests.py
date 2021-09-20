from django.test import TestCase
from . models import *
# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.user=User(id=1, username='Nixon', password='Nickson_100$')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()

class TestProject(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='Nixon')
        self.project = Projects.objects.create(id=1, title='test project', photo='https:/media/images.IMG.png', description='an image of me relaxing',
                                        user=self.user, url='http://url.com')
        def test_instance(self):
            self.assertTrue(isinstance(self.post, Projects))

        def test_save_project(self):
            self.project.save_project()
            project = Projects.objects.all()
            self.assertTrue(len(project) > 0)

        def test_get_project(self):
            self.project.save()
            project = Projects.all_projects()
            self.assertTrue(len(project) > 0)

        def test_search_project(self):
            self.project.save()
            project = Projects.search_project('test')
            self.assertTrue(len(project) > 0)

        def test_delete_project(self):
            self.project.delete_post()
            project = Projects.search_project('test')
            self.assertTrue(len(project) < 1)

class RatingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='Nixon')
        self.project = Projects.objects.create(id=1, title='test', image='https://ucarecdn.com/0ccf61ff-508e-46c6-b713-db51daa6626e', description='description',
                                        user=self.user, link='http://url.com')
        self.rating = Ratings.objects.create(id=1, design=6, usability=7, content=9, user=self.user, project=self.project)

    def test_instance(self):
            self.assertTrue(isinstance(self.rating, Ratings))

    def test_save_rating(self):
        self.rating.save_rating()
        rating = Ratings.objects.all()
        self.assertTrue(len(rating) > 0)

    
