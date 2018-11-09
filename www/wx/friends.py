#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '姜五侠'

# 导入itchat模块，操作微信个人号的接口
import itchat

# 获取数据
def get_data():
    # 扫描二维码登陆微信，实际上就是通过网页版微信登陆
    itchat.auto_login()
    # 获取所有好友信息
    friends = itchat.get_friends(update=True)  # 返回一个包含用户信息字典的列表
    return friends

def parse_data(data):
    friends = []
    for item in data[1:]:  # 第一个元素是自己，排除掉
        friend = {
            'NickName': item['NickName'],  # 昵称
            'PYQuanPin': item['PYQuanPin'],  # 账户
            #'RemarkName': item['RemarkName'],  # 备注名
            'Sex': item['Sex'],  # 性别：1男，2女，0未设置
            'Province': item['Province'],  # 省份
            'City': item['City'],  # 城市
            'Signature': item['Signature'].replace('\n', ' ').replace(',', ' '),  # 个性签名（处理签名内容换行的情况）
            'StarFriend': item['StarFriend'],  # 星标好友：1是，0否
            'ContactFlag': item['ContactFlag']  # 好友类型及权限：1和3好友，259和33027不让他看我的朋友圈，65539不看他的朋友圈，65795两项设置全禁止
        }
        print(friend)
        friends.append(friend)
    return friends

def save_to_txt():
    friends = parse_data(get_data())
    for item in friends:
        with open('friends.txt', mode='a', encoding='utf-8') as f:
            f.write('%s,%s,%d,%s,%s,%s,%d,%d\n' % (
                item['NickName'],item['UserName'], item['RemarkName'], item['Sex'], item['Province'], item['City'], item['Signature'],
                item['StarFriend'], item['ContactFlag']))


if __name__ == '__main__':
    save_to_txt()



