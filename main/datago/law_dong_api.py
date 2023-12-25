from main.comm.key_property import CommProperty
import requests
import xmltodict
import json



# 국토교통부_전국 법정동
class LawDongApi:

    def get_law_dong(self, page_no, page_size):
        url = 'https://api.odcloud.kr/api/15063424/v1/uddi:257e1510-0eeb-44de-8883-8295c94dadf7'
        params = {
            'serviceKey': CommProperty().service_key,
            'page': page_no,
            'perPage': page_size,
            # 'returnType': "XML"
        }
        response = requests.get(url, params)
        bb = json.loads(response.text)
        print(bb)