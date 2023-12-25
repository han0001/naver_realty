from unittest import TestCase

from main.datago.law_dong_api import LawDongApi


class Test(TestCase):

    def test_get_law_dong(self):
        law_dong_api = LawDongApi()
        response = law_dong_api.get_law_dong('1', '100')
        print(response)
