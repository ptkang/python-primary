'''
@Author: your name
@Date: 2019-12-08 21:42:37
@LastEditTime: 2019-12-10 00:08:10
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\vscode\reptile\reptile1.py
This is a module
'''
# 爬虫
# 反爬机制，自动登录，代理代理IP等辅助功能
# 巩固基本知识，演示基本编码规范，好的代码应该怎么来编写，爬虫最基本原理
# 爬虎牙直播平台：https://www.huya.com/?from=baidusem
# 第一步：明确爬虫的目的，即需求要明确：英雄联盟人气排行
# 第二步：明确帕醇的方法，即怎么来爬，即怎么抓取数据。因有了数据才能对数据进行分析和计算
#       1. 了解网站的结构, 找到最适合分析的页面
#       2. 明确分析什么，明确分析人气排行，即每个方块的右下角的观看人数
#       3. 对程序进行比较运算确认人气排行
# 爬虫的常规思路
# 1. 网页显示的原理
# 2. 正则表达式
# 爬虫前奏：
#   1. 明确目的
#   2. 找到数据对应的网页
#   3. 分析网页的结构找到数据所在的标签位置，这个是标签能够定位到我们需要抓取的信息
#       1)尽量选取具有唯一标识符的标签作为定位标签
#       2)尽量寻找最接近于我们要提取数据的标签作为定界符号
# <span class="txt">
#     <span class="avatar fl">
#         <img title="血色-kiki【717】" alt="血色-kiki【717】" src="https://huyaimg.msstatic.com/avatar/1065/a3/0cc3594b9a6e3a0aece74c74cfc8cd_180_135.jpg" data-default-img="84x84" data-original="https://huyaimg.msstatic.com/avatar/1065/a3/0cc3594b9a6e3a0aece74c74cfc8cd_180_135.jpg">
#         <i title="血色-kiki【717】" class="nick">血色-kiki【717】</i>
#     </span>
#     <span class="num"><i class="num-icon"></i><i class="js-num">15.8万</i></span>
# </span>
# </li>

# 模拟http请求，向服务器发送这个请求，获取到服务器返回给我们的HTML
# 用正则表达式提取我们要的数据（主播的名字，人气）
# 
# 断点调试
# F5：启动应用程序
# F10：单步执行
# F5：从一个断点调到另一个断点
# F11: 进入函数内部
# 注释： python注释放到类或函数的内部,被称为块注释
# 空行隔离： 要有意义才添加空行以增加块效果
# 函数大小：不要超过30行，最好在10行和20行之间
# 下面代码通用性不高，要更多融入面向对象的思想

# 爬虫库和框架：BeautifulSoup, Scrapy, 
# 爬虫、反爬虫，反反爬虫的斗争
# 爬虫效率
# 爬虫数据如何提取和利用
# 服务器IP被封, 所以爬虫频率要尽量少，否则要寻找代理IP库

from urllib import request
import re

class Spider():
    '''
    This is a class
    '''
    url = 'https://www.huya.com/g/lol'
    #root_pattern = '<span class="txt">[\s\S]*?</span>\n</li>'
    root_pattern = '<span class="txt">([\s\S]*?)</li>'
    name_pattern = '<i class="nick" title="[\s\S]*?">([\s\S]*?)</i>'
    number_pattern = '<i class="js-num">([\s\S]*?)</i>'
    # 私有方法
    def __fetch_content(self):
        '''
        This is a function
        '''
        # 打开url
        r = request.urlopen(Spider.url)
        htmls = r.read()

        # 将bytes转换为string
        htmls = str(htmls, encoding='utf-8')
        return htmls
    
    def __analysis(self, htmls):
        # <span class="txt">包含主播姓名和观看人数</span>
        #   <span class="avatar fl"> 主播姓名 </span>
        #       <i class="nick" title="黑店百地">黑店百地</i>
        #   <span class="num"> 观看人数 </span>
        #       <i class="js-num">308.3万</i>
        root_html = re.findall(Spider.root_pattern, htmls)
        # print(type(root_html))
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattern, html)
            number = re.findall(Spider.number_pattern, html)
            anchor = {'name':name, 'number':number}
            anchors.append(anchor)
        #print(anchors[0])
        return anchors
    
    def __refine(self, anchors):
        l = lambda anchor: {
            'name':anchor['name'][0].strip(),
            'number':anchor['number'][0].strip()
            }
        return map(l, anchors)
    
    def __sort_seed(self, anchor):
        r = re.findall('\d*', anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    def __sort(self, anchors):
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
        return anchors
    
    def __show(self, anchors):
        for rank in range(0, len(anchors)):
            print('rank ' + str(rank) +
            ':   ' + anchors[rank]['name'] +
            '    ' + anchors[rank]['number'])
    
    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)


spider = Spider()
spider.go()