import requests
import xmltodict

from main.comm.key_property import CommProperty
from main.datago.response.apart_transaction_response import ApartTransactionResponse


# 국토교통부_아파트실거래
class ApartTransationApi:

    def get_price(self, pageNo, pageSize,  lawd_cd, deal_ymd):
        url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev'
        params = {
            'serviceKey': CommProperty().service_key,
            'pageNo': pageNo,
            'numOfRows': pageSize,
            'LAWD_CD': lawd_cd,
            'DEAL_YMD': deal_ymd
        }
        response = requests.get(url, params)

        items = xmltodict.parse(response.content)["response"]["body"]["items"]["item"]

        for item in items:
            apart_transaction = ApartTransactionResponse(**item)
            print(apart_transaction)

        print(items)


