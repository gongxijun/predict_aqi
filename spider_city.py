# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
area_dict = {
    '东四': 1,
    '天坛': 2,
    '官园': 3,
    '万寿西宫': 4,
    '奥体中心': 5,
    '农展馆': 6,
    '万柳': 7, '北部新区': 8, '植物园': 9
    , '丰台花园': 10, '云岗': 11, '古城': 12
    , '房山': 13, '大兴': 14, '亦庄': 15, '∂': 16, '顺义': 17
    , '昌平': 18, '门头沟': 19, '平谷': 20, '怀柔': 21, '密云': 22,
    '延庆': 23, '定陵': 24, '八达岭': 25, '密云水库': 26, '东高村': 27
    , '永乐店': 28, '榆垡': 29,
    '琉璃河': 30, '前门': 31, '永定门内': 32,
    '西直门北': 33, '南三环': 34, '东四环': 35
}
area_list = ['东四', '天坛', '西城官园', '万寿西宫', '奥体中心', '农展馆', '海淀万柳', '北部新区', '植物园', '丰台花园', '云岗', '古城', '良乡', '黄村', '亦庄',
             '通州北苑',
             '顺义新城', '昌平镇', '双峪', '夏都', '平谷镇', '密云镇', '怀柔镇']

area_map = {'东四': '东四', '天坛': '天坛', '官园': '西城官园', '万寿西宫': '万寿西宫', '奥体中心': '奥体中心',
            '农展馆': '农展馆', '万柳': '海淀万柳', '北部新区': '北部新区', '丰台花园': '丰台花园', '云岗': '云岗',
            '古城': '古城', '房山': '良乡', '大兴': '黄村', '亦庄': '亦庄', '通州': '通州北苑',
            '顺义': '顺义新城', '昌平': '昌平镇', '门头沟': '双峪', '平谷': '平谷镇', '怀柔': '怀柔镇', '密云': '密云镇',
            '延庆': '夏都', '定陵': '昌平镇', '八达岭': '夏都', '密云水库': '密云镇', '东高村': '平谷镇', '永乐店': '通州北苑',
            '榆垡': '黄村', '琉璃河': '良乡', '前门': '天坛', '永定门内': '西城官园', '西直门北': '西城官园', '南三环': '通州北苑', '东四环': '古城'}


class Spider:
    def __init__(self):
        # 加启动配置
        self.option = webdriver.ChromeOptions()
        self.option.add_argument('disable-infobars')
       # self.option.add_argument('headless')
        # 打开chrome浏览器
        self.browser = webdriver.Chrome(chrome_options=self.option)

    def __del__(self):
        self.browser.close();

    def find_sec(self):
        self.browser.get("http://zx.bjmemc.com.cn/getAqiList.shtml?timestamp=1528094103229")  # Load page
        result = {}
        try:
            board = self.browser.find_elements_by_class_name('p3_jcz_new')
            for ind in range(0, len(board), 1):
                board_en = board[ind].text.encode('utf-8')
                print  board[ind].text
                boards = str(board_en).split('\n')
                area = boards[0].strip()
                if area in area_list:
                    aqi = boards[-1].split()[0]
                    result[area] = float(aqi)
            return result
        except NoSuchElementException:
            assert 0, "can't find element"


if __name__ == '__main__':
    spider = Spider()
    print spider.find_sec()
