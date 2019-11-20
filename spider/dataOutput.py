import csv


class dataOutput():
    def __init__(self):
        '''
        创建 csv 文件，写入第一行头信息
        '''
        # 创建麦当劳的 csv 文件
        self.creat_mc_info_csv()
        # 创建城市，GDP，人口的 csv 文件
        self.creat_GDP_people_csv()
        # 创建城市分级的 csv 文件
        self.creat_city_rank_csv()

    def creat_mc_info_csv(self):
        '''
        创建麦当劳 csv，写入头信息
        :return:
        '''
        title = ['shop_name','city']
        f = open('mc_info.csv','w', encoding='utf-8',newline='')  # 创建csv
        writer = csv.writer(f)  # 写入的对象
        writer.writerow(title)  # 写入header部分
        f.close()

    def creat_GDP_people_csv(self):
        '''
        创建城市，GDP，人口的 csv 文件，并写入头信息
        :return:
        '''
        title = ['city','GDP(亿元)','people(万)']
        with open('GDP_people.csv','w',encoding='utf-8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(title)

    def creat_city_rank_csv(self):
        '''
        创建城市分级 csv，并写入头信息
        :return:
        '''
        title = ['city','rank']
        with open('city_rank.csv','w',encoding='utf-8',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(title)

    def mc_info_to_csv(self,zips):
        '''
        麦当劳店铺名称，地点写入 csv
        :param zips: [(城市，店名)....] 对应的压缩
        :return:
        '''
        with open(r'./mc_info.csv','a+',encoding='utf-8',newline='') as f:
            writer = csv.writer(f)
            for zip in zips:
                writer.writerow([zip[1].strip(),zip[0].strip()])

    def GDP_people_to_csv(self,datas):
        '''
        城市 GDP，人口写入 csv
        :param data:
        :return:
        '''
        with open('./GDP_people.csv','a',encoding='utf-8',newline='') as f:
            writer = csv.writer(f)
            for data in datas:
                writer.writerow(data)

    def city_rank_to_csv(self,datas):
        '''
        城市分级数据写入 csv
        :param datas:
        :return:
        '''
        with open('./city_rank.csv','a',encoding='utf-8',newline='') as f:
            writer = csv.writer(f)
            for data in datas:
                writer.writerow(data)
