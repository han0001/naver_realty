import requests
import xmltodict

from main.comm.key_property import CommProperty
import xml.etree.ElementTree as ET

def get_price(pageNo, pageSize,  lawd_cd, deal_ymd):


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


