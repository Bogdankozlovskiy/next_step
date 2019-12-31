from django.test import TestCase
from django.test import Client
from .models import MyVideo, Comment
from django.contrib.auth.models import User
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
import logging


class VideoTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        test_video = MyVideo.objects.create(
            id=1,
            title="test title",
            slug="test_title",
            description="test description",
            url="https://test_url.com")
        test_user = User.objects.create(id=1, username="testname")
        test_user.set_password('testpassword')
        test_user.save()
        Comment.objects.create(
            id=1,
            text="rest text comment",
            video=test_video,
            user=test_user)
        Comment.objects.create(
            id=2,
            text="rest text comment2",
            video_id=1,
            user_id=1)

    def test_have_str(self):
        video = MyVideo.objects.get(id=1)
        self.assertEqual(video.__str__(), "test title - test_title")

    def test_have_comment(self):
        video = MyVideo.objects.get(id=1)
        all_comment = Comment.objects.filter(video_id=1)
        self.assertCountEqual(video.comments, all_comment)

    def test_hello_page(self):
        response = self.client.get('/hello/')
        self.assertEqual(response.status_code, 200)

    def test_authenticate(self):
        res = self.client.login(
            username='testname',
            password='testpassword')
        self.assertEqual(res, True)

    def test_authenticate_in_page(self):
        self.client.login(
            username='testname',
            password='testpassword')
        response = self.client.get('/hello/')
        self.assertEqual(response.context['user'].username, 'testname')


class MySeleniumLocal(TestCase):
    def setUp(self):
        super().setUp()
        self.selenium = WebDriver()
        self.live_server_url = 'http://127.0.1:8000/admin/login/'

    def tearDown(self):
        super().tearDown()
        self.selenium.quit()

    def test_selenium(self):
        self.selenium.get(self.live_server_url)
        logging.warning(self.selenium.title)
        username_input = self.selenium.find_element_by_name('username')
        username_input.send_keys('bogdan')
        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('gd0d469s')
        btn = self.selenium.find_element_by_xpath('//input[@value="Войти"]')
        btn.click()
        logging.warning(self.selenium.title)


class MySeleniumGlobal(TestCase):
    def setUp(self):
        super().setUp()
        self.selenium = webdriver.Remote(
            command_executor='http://172.21.0.4:4444/wd/hub',
            desired_capabilities = {"browserName":'chrome'})
        self.live_server_url = 'http://185.227.99.68/admin/login/'

    def tearDown(self):
        super().tearDown()
        self.selenium.quit()

    def test_selenium(self):
        self.selenium.get(self.live_server_url)
        logging.warning(self.selenium.title)
        username_input = self.selenium.find_element_by_name('username')
        username_input.send_keys('bogdan')
        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('gd0d469s')
        btn = self.selenium.find_element_by_xpath('//input[@value="Log in"]')
        btn.click()
        logging.warning(self.selenium.title)
