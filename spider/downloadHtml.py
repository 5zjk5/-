import requests
import time
from fake_useragent import UserAgent


class downloadHtml():
    def get_html(self,url):
        '''
        下载 html
        :param url:
        :return:
        '''
        count = 0 # 请求次数计数
        while True:
            ua = UserAgent()
            headers = {'User-Agent': ua.random}
            response = requests.get(url,headers=headers)
            count += 1
            if response.status_code == 200:
                response.encoding = 'utf-8'
                return response
            else:
                if count % 3 == 0:
                    time.sleep(2)
                continue




