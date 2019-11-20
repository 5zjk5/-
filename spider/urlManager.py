class urlManager():
    def __init__(self):
        '''
        初始化 url
        '''
        # 麦当劳店铺名与地点 url
        self.mc_url = ['https://www.mcdonalds.com.cn/index/Quality/publicinfo/deliveryinfo?page={}'
                       .format(str(i)) for i in range(1,236)]
        # GDP，人口 url
        self.GDP_people_ur = 'http://caifuhao.eastmoney.com/news/20190201115604564011000'
        # 城市分级 url
        self.city_rank_url = 'https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E5%9F%8E%E5%B8%82%E6%96%B0%E5%88%86%E7%BA%A7%E5%90%8D%E5%8D%95/12702007?fr=aladdin#2'

    def get_mc_url(self):
        '''
        返回麦当劳 url
        :return:
        '''
        return self.mc_url

    def get_GDP_people_url(self):
        '''
        返回 GDP，人口的 url
        :return:
        '''
        return self.GDP_people_ur

    def get_city_rank_url(self):
        '''
        返回城市分级 uel
        :return:
        '''
        return self.city_rank_url

