#!/usr/bin/python3
# coding: utf-8
from unittest import TestSuite, TextTestRunner, TestCase


class OrderTestCase(TestCase):
    def test_01_add(self):
        print('--add order--')

    def test_02_pay(self):
        print('--pay order--')


class UserTestCase(TestCase):

    def setUp(self):
        print('---init--')

    def test_02_get_info(self):
        print('--info---')

    def test_01_login(self):
        print('--login---')

    def tearDown(self):
        print('---over---')


def suite1():
    suite_ = TestSuite()

    suite_.addTest(UserTestCase.test_01_login)
    suite_.addTest(UserTestCase.test_02_get_info)

    return suite_


def suite2():
    suite_ = TestSuite()

    suite_.addTest(OrderTestCase.test_01_add)
    suite_.addTest(OrderTestCase.test_02_pay)

    return suite_


if __name__ == '__main__':
    TextTestRunner().run(TestSuite((suite2(), suite1())))
