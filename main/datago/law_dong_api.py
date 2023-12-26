from main.comm.key_property import CommProperty
from main.datago.response.law_dong_response import LawDongResponse
import requests
import json



# 국토교통부_전국 법정동
class LawDongApi:

    def get_law_dong(self, page_no, page_size):
        url = 'https://api.odcloud.kr/api/15063424/v1/uddi:257e1510-0eeb-44de-8883-8295c94dadf7'
        params = {
            'serviceKey': CommProperty().service_key,
            'page': page_no,
            'perPage': page_size
        }
        response = requests.get(url, params)
        items = json.loads(response.text)["data"]
        for item in items:
            law_dong_response = LawDongResponse(**item)