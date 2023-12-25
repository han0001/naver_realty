import configparser


class CommProperty:
    service_key = ""
    law_dong_csv_path = ""

    def __init__(self):
        properties = configparser.ConfigParser()
        properties.read('D:/workspace_python/naver_realty/config.ini')

        self.service_key = properties.get('DATAGO', 'SERVICE_KEY') 
        self.law_dong_csv_path = properties.get('FILE_PATH', 'LAW_DONG_CSV_PATH')    
