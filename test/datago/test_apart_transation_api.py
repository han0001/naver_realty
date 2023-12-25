from unittest import TestCase

from main.datago import apart_transation_api


class Test(TestCase):
    def test_get_price(self):

        response = apart_transation_api.get_price('1', '100', '11100', '202202')
        print(response)
