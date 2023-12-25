from unittest import TestCase

from main.datago.apart_transation_api import ApartTransationApi


class Test(TestCase):

    def test_get_price(self):
        apart_transation_api = ApartTransationApi()
        response = apart_transation_api.get_price('1', '100', '41830', '202202')
        print(response)
