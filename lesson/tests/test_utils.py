import json

from django.test import TestCase

from accounts.models import User
from cards.models import Card
from lesson.utils import (get_correct_answers, get_feedback_and_num_correct,
                          validate_user_answers)


class UtilsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            email='test@gmail.com',
            first_name='Имя',
            last_name='Фамилия',
            password='test12345'
        )
        Card.objects.create(
            user=cls.user,
            front_text='текст передний',
            back_text='текст задний',
        )
        Card.objects.create(
            user=cls.user,
            front_text='текст передний 2',
            back_text='текст задний 2',
        )
        Card.objects.create(
            user=cls.user,
            front_text='текст передний 3',
            back_text='текст задний 3',
        )

    def test_validate_user_answers(self):
        USER_ANSWERS_AND_EXPECTED_VALUE = {
            '{}': False,
            '{"test": "test"}': False,
            '{"1": "test", "2": "test"}': False,
            '{"1": "test", "3": "test", "2": "test"}': True
        }
        for user_answer, expected_value in \
                USER_ANSWERS_AND_EXPECTED_VALUE.items():
            with self.subTest(f'{user_answer=}, {expected_value=}'):
                user_answer = json.loads(user_answer)
                cards = Card.objects.filter(user=self.user.id).order_by('?')
                real_value = validate_user_answers(user_answer, cards)
                self.assertEqual(real_value, expected_value)

    def test_get_correct_answers(self):
        cards = Card.objects.filter(user=self.user.id)
        real_value = get_correct_answers(cards)
        expected_value = {'1': 'текст задний',
                          '2': 'текст задний 2',
                          '3': 'текст задний 3'}
        self.assertEqual(real_value, expected_value)

    def test_get_feedback_and_num_correct(self):
        with self.subTest('test 1'):
            user_answers = {}
            correct_answers = {'1': 'correct', '2': 'correct'}
            expected_num_correct = 0
            expected_feedback = {}
            real_feedback, real_num_correct = get_feedback_and_num_correct(
                user_answers, correct_answers)
            self.assertEqual([real_feedback, real_num_correct],
                             [expected_feedback, expected_num_correct])
        with self.subTest('test 2'):
            user_answers = {'2': 'correct'}
            correct_answers = {'1': 'correct', '2': 'correct'}
            expected_num_correct = 1
            expected_feedback = {'2': 'correct'}
            real_feedback, real_num_correct = get_feedback_and_num_correct(
                user_answers, correct_answers)
            self.assertEqual([real_feedback, real_num_correct],
                             [expected_feedback, expected_num_correct])
        with self.subTest('test 3'):
            user_answers = {'1': 'incorrect', '2': 'correct'}
            correct_answers = {'1': 'correct', '2': 'correct'}
            expected_num_correct = 1
            expected_feedback = {'1': 'incorrect', '2': 'correct'}
            real_feedback, real_num_correct = get_feedback_and_num_correct(
                user_answers, correct_answers)
            self.assertEqual([real_feedback, real_num_correct],
                             [expected_feedback, expected_num_correct])
        with self.subTest('test 4'):
            user_answers = {'1': 'correct', '2': 'correct'}
            correct_answers = {'1': 'correct', '2': 'correct'}
            expected_num_correct = 2
            expected_feedback = {'1': 'correct', '2': 'correct'}
            real_feedback, real_num_correct = get_feedback_and_num_correct(
                user_answers, correct_answers)
            self.assertEqual([real_feedback, real_num_correct],
                             [expected_feedback, expected_num_correct])
