from spider.urlManager import urlManager
from spider.downloadHtml import downloadHtml
from spider.parseHtml import parseHtml
from spider.dataOutput import dataOutput


class spider():
    def __init__(self):
        '''
        初始化各个模块
        '''
        self.manager = urlManager()
        self.html = downloadHtml()
        self.data = parseHtml()
        self.output = dataOutput()

    def get_mc_shop_name_localtion(self):
        '''
        获取麦当劳店名地点
        :return:
        '''
        urls = self.manager.get_mc_url()
        page = 1
        for url in urls:
            response = self.html.get_html(url)
            infos = self.data.parse_mc_info(response)
            self.output.mc_info_to_csv(infos)
            print('麦当劳第 %s 页已写入' % str(page))
            page += 1

    def get_GDP_people(self):
        '''
        获得城市前100城市 GDP，人数
        :return:
        '''
        url = self.manager.get_GDP_people_url()
        response = self.html.get_html(url)
        data = self.data.GDP_people_info(response)
        self.output.GDP_people_to_csv(data)

    def get_city_rank_info(self):
        '''
        获得城市分级
        :return:
        '''
        url = self.manager.get_city_rank_url()
        response = self.html.get_html(url)
        data = self.data.city_rank_info(response)
        self.output.city_rank_to_csv(data)

    def start(self):
        '''
        主逻辑
        :return:
        '''
        # 获得麦当劳店名地点
        self.get_mc_shop_name_localtion()
        print('麦当劳数据获取完毕！')
        # 获得城市前100城市 GDP，人数
        self.get_GDP_people()
        print('城市 GDP，人数已获取完毕！')
        # 获得城市分级
        self.get_city_rank_info()
        print('城市分级获取完毕！')


if __name__ == '__main__':
    spider = spider()
    spider.start()