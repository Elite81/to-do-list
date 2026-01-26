import unittest
from faker import Faker
from project import *
import uuid
from tasks.models import *
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from tasks.forms import *
import random



fake = Faker()
User = get_user_model()

class SignUpTest(TestCase):
    '''Testcase for signingup a user'''
    def test_user_signUp(self):
        password = fake.password()
        response = self.client.post(
            reverse("account_signup"),
            data={
                "username": fake.user_name(),
                "email": fake.safe_email(),
                "password1": password,
                "password2": password
            },
        )
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.first()
        self.assertIsNotNone(user.id)
        self.assertTrue(user.is_active)
        self.assertEqual(user.username, response.wsgi_request.POST.get('username'))
        self.assertEqual(response.status_code, 302)


class LoginTest(TestCase):
    def setUp(self):
        self.username = fake.user_name()
        self.email = fake.safe_email()
        self.password = fake.password()
        
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )

    def test_user_login(self):
        response = self.client.post(
            reverse("account_login"),
            data={
                "login": self.username,
                "password":self.password,
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.wsgi_request.user.is_authenticated)
        self.assertEqual(response.wsgi_request.user.username, self.username)

    def create_task(self):
        user = self.user
        data={"task": fake.words(nb=5), 
              "description":fake.sentence(nb_words=10),
              "status":random.choice(Tasks.STATUS_CHOISES)[0],
              "priority":random.choice(Tasks.PRIORITY)[0]}
        task_form = TaskForm(data=data)
        self.assertTrue(task_form.is_valid(), task_form.errors)
        if task_form.is_valid():
            task = save_new_task(task_form, user)
            return task

    def test_save_new_task(self):
        task = self.create_task()
        self.assertEqual(Tasks.objects.count(), 1)
        self.assertEqual(self.user, task.user)

# def search_task():
#     ...

    def test_save_edited_task(self):
        user = self.user
        task = self.create_task()
        edited_task = " ".join(fake.words(nb=5))
        form_data = {"task": edited_task,
                     "description":task.description,
                     "status":task.status,
                     "priority":task.priority
                    }
        task.task = edited_task
        form = TaskForm(form_data, instance=task)
        self.assertTrue(form, form.errors)
        
        edited_task = save_edited_task(form, user)
        self.assertEqual(self.user, task.user)
        self.assertEqual(task.task, edited_task.task)

    def test_delete_a_task(self):
        user = self.user
        task = self.create_task()
        task_pk = task.id
        delete_a_task(task_pk, user)
        self.assertEqual(Tasks.objects.count(), 0)

    def test_search(self):
        query = fake.words(nb=1)
        result = search_task(query)
        if result:
            for i in result:
                self.assertTrue(query in i.task or query in i.description)
        else:
            self.assertEqual(list(result), [])