from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        t = Team.objects.create(name='Test Team')
        self.assertIsNotNone(t.id)
    def test_user_create(self):
        t = Team.objects.create(name='Test Team2')
        u = User.objects.create_user(username='testuser', email='test@x.com', password='pw', team=t)
        self.assertIsNotNone(u.id)
    def test_activity_create(self):
        t = Team.objects.create(name='Test Team3')
        u = User.objects.create_user(username='testuser2', email='test2@x.com', password='pw', team=t)
        a = Activity.objects.create(user=u, type='run', duration=10, calories=100)
        self.assertIsNotNone(a.id)
    def test_workout_create(self):
        w = Workout.objects.create(name='W', description='desc', duration=20)
        self.assertIsNotNone(w.id)
    def test_leaderboard_create(self):
        t = Team.objects.create(name='Test Team4')
        u = User.objects.create_user(username='testuser3', email='test3@x.com', password='pw', team=t)
        l = Leaderboard.objects.create(user=u, score=123)
        self.assertIsNotNone(l.id)
