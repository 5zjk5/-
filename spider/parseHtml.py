import re


class parseHtml():
    def parse_mc_info(self,response):
        '''
        解析麦当劳响应，获取数据
        :param response:
        :return:
        '''
        pat1 = '<span>城市</span>(.*?)</td>'
        cities = re.findall(pat1,response.text,re.S)

        pat2 = '<span>门店名称</span>(.*?)</td>'
        shop_names = re.findall(pat2,response.text,re.S)

        infos = zip(cities,shop_names)
        return infos

    def GDP_people_info(self,response):
        '''
        解析获得 GDP，人口的数据
        :param response:
        :return:
        '''
        pat = '<p>(\d+.*?)</p>'
        infos = re.findall(pat,response.text,re.S)

        # 处理提取的数据，以 [(城市，GDP，人数).....] 形式保存
        datas = []
        for info in infos:
            # 人数
            pat1 = r'.*?(\d+)万）'
            people = re.findall(pat1,info)

            # GDP
            pat2 = r'(\d+)亿元，'
            GDP = re.findall(pat2,info)

            # 城市
            pat3 = r'\d+\.(.*?)\d+亿元，'
            city = re.findall(pat3,info)
            city = city[0].split('（')[0] + '市'

            try:
                datas.append((city,GDP[0],people[0]))
            except:
                pass

        return datas

    def city_rank_info(self,response):
        '''
        解析获取城市分级数据，以 [(城市，等级)...] 形式返回
        :param response:
        :return:
        '''
        # 先提取所有，再从中分级
        pat = '<div class="para-title level-3" label-module="para-title">(.*?)<div class="anchor-list">'
        city_ls = re.findall(pat,response.text,re.S)

        pat1 = 'data-lemmaid=".*?">(.*?)</a></div>'
        data = []
        for l in city_ls:
            if '一线' in l:
                rank = '一线'
            if '二线' in l:
                rank = '二线'
            if '三线' in l:
                rank = '三线'
            if '四线' in l:
                rank = '四线'
            if '五线' in l:
                rank = '五线'
            citys = re.findall(pat1, l)
            for c in citys:
                city = (c,rank)
                data.append(city)

        return data


