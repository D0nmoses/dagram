from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Tag, Post, Follow, Comment, Like

# Create your tests here.


class ProfileTestClass(TestCase):
    '''	
    Test case for the Profile class	
    '''
    def setUp(self):

        # Create instance of Profile class
        self.new_profile = Profile(bio="Trial case bio")

    def test_instance(self):

        self.assertTrue( isinstance(self.new_profile, Profile) )

    def test_get_profiles(self):

        gotten_profiles = Profile.get_profiles()

        profiles = Profile.objects.all()

        self.assertTrue(len(gotten_profiles) == len(profiles))

    def test_get_other_profiles(self):

        self.don = User(username="don")
        self.don.save()

        self.dan = User(username="dan")
        self.dan.save()

        self.test_profile = Profile(user=self.dan,bio="Another Trial")

        gotten_profiles = Profile.get_other_profiles(self.don.id)

        profiles = Profile.objects.all()

        self.assertTrue( len(gotten_profiles) < len(profiles))