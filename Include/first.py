# a=1
# print(a)
# if(a<1):
#     print("我是女生")
# else:
#     print("我不是女生")
# while(a<10):
#     print(a)
#     a=a+1
# '''
# 这是一个注释
#    你可以看看输出的什么
#         格式
# '''
#
# b = '''
# 这是一个注释
#    你可以看看输出的什么
#         格式
# '''
# print(b)

# 导入requests包
import requests
from bs4 import BeautifulSoup
import time


def get_html(url):
    """
    获取每一章的整体html内容
    :param url:
    :return:
    """
    strhtml = requests.get(url)  # Get方式获取网页数据
    soup = BeautifulSoup(strhtml.text, 'lxml')
    return soup


def get_alabel(url):
    """
        获取每一章的下一章按钮的a标签
        :param url:
        :return:
    """
    html = get_html(url)
    previous = html.select('#readerFt > div > div.chap_btnbox > a:nth-child(2)')  # 提取上一章
    next = html.select('#readerFt > div > div.chap_btnbox > a.nextchapter')  # 提取下一章
    return next


def get_next_url(label):
    """
        获取每一个a标签中的href
        :param label: a标签html
        :return:
    """
    nextUrl = ''
    # for nu in label:
    #     nextTitle = nu.get_text()
    #     nextUrl = nu.get('href')
    #     nextDataHook = nu.get('data-hook')
    nextUrl = label[0].get('href')
    return nextUrl


def get_content(url):
    """
        获取每一章的内容p标签数组
        :param url: 每一章的url
        :return: 数据数组
    """
    html = get_html(url)
    data = html.select('.readerPageWrap>div#reader_warp>div#readerFt>div.reader_box>div.content>p')
    return data


def get_title(url):
    """
        获取每一章的标题
        :param url: 每一章的url
        :return:    每一章的标题值
    """
    html = get_html(url)
    title = html.select('#readerFt > div > div.title > div.title_txtbox')
    return title


def get_next_url_for_num(url, num):
    """
        获取第num章的url
        :param url: 第一章的url
        :param num: 要获取的第num章数
        :return:    第num章的url值
    """
    num = num - 1   # 因为url为第一章的，所以这边num需要先减一
    numUrl = ''     # num章的url
    while (num > 0):
        label = get_alabel(url)
        url = get_next_url(label)
        if (num == 1):
            numUrl = url
        num = num - 1

    return numUrl


# file_handle = open('D:\昆仑小师兄.txt', mode='w')
url = 'http://book.zongheng.com/chapter/967301/60491429.html'

# i = 1
# while (i < 4):
#     # 章节标题
#     title = get_title(url)
#     print(title[0].get_text())
#     file_handle.write(title[0].get_text() + '\n')
#
#     # 章节内容
#     content = get_content(url)
#     for p in content:
#         print(p.get_text())
#         file_handle.write(p.get_text() + '\n')
#     # 换行
#     file_handle.write('\n')
#
#     nextLabel = get_alabel(url)
#     url = get_next_url(nextLabel)
#     i = i + 1
#     print(url)
#
#     # 休息3秒
#     time.sleep(3)
#
#     file_handle.close()

print(get_next_url_for_num(url, 2))
