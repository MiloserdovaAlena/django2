from django.test import TestCase
from .models import EmployeeFeedback, ManagerFeedback, SelfFeedback, ColleagueFeedback
from django.contrib.auth.models import User
from django.urls import reverse

class FeedbackTestCase(TestCase):
    def setUp(self):
        # Создайте нескольких пользователей для тестов
        self.user1 = User.objects.create(username='user1')
        self.user2 = User.objects.create(username='user2')

        # Создайте примеры фидбеков для тестирования
        self.employee_feedback = EmployeeFeedback.objects.create(
            user=self.user1,
            anonymous_user='Anonymous1',
            feedback='Feedback 1',
            rating=5
        )

        self.manager_feedback = ManagerFeedback.objects.create(
            user=self.user1,
            feedback='Manager Feedback 1'
        )

    def test_employee_feedback_creation(self):
        self.assertEqual(str(self.employee_feedback), str(self.employee_feedback))
        self.assertEqual(self.employee_feedback.user, self.user1)

    def test_manager_feedback_creation(self):
        self.assertEqual(str(self.manager_feedback), str(self.manager_feedback))
        self.assertEqual(self.manager_feedback.user, self.user1)

    def test_feedback_list_view(self):
        url = reverse('onlinerating:feedback')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Feedback 1')


