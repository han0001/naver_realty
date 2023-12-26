from unittest import TestCase

from main.naver.naver_api import NaverApi
from main.naver.constant.naver_constant import TradeType
from main.naver.constant.naver_constant import PriceOrder
from main.naver.response.naver_article_response import NaverArticleResponse
from main.naver.response.naver_apart_response import NaverApartResponse


class Test(TestCase):

    def test_get_sido_info(self):
        naver_api = NaverApi()
        sido = naver_api.get_sido_info()
        print(sido) # 1100000000

    def test_get_gungu_info(self):
        naver_api = NaverApi()
        gungu = naver_api.get_gungu_info("1100000000")
        print(gungu) # 1168000000

    def test_get_dong_info(self):
        naver_api = NaverApi()
        dong = naver_api.get_dong_info("1168000000")
        print(dong) # 1168010300

    def test_get_apt_list(self):
        naver_api = NaverApi()
        apt_list = naver_api.get_apt_list("1168010300")
        print(apt_list) # 146479

    def test_get_apt_info(self):
        naver_api = NaverApi()
        authorization = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3MDI4ODc3MDYsImV4cCI6MTcwMjg5ODUwNn0.beMuv8GgfQMeJ_Ot-RlnbXvCUGnLcvpJvMe1jWPQ5tk"
        apart = naver_api.get_apt_info("145017", authorization)["complexDetail"]
        naver_apart_response = NaverApartResponse(**apart)
        print(naver_apart_response)

    def test_get_apt_price(self):
        naver_api = NaverApi()
        authorization = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3MDI4ODc3MDYsImV4cCI6MTcwMjg5ODUwNn0.beMuv8GgfQMeJ_Ot-RlnbXvCUGnLcvpJvMe1jWPQ5tk"
        apt_price = naver_api.get_apt_price("145017",
                                            "2",
                                            TradeType.전세.value,
                                            PriceOrder.낮은가격순.value,
                                            authorization)

        for article in apt_price['articleList']:
            article_response = NaverArticleResponse(**article)
            print(article_response)
