# coding=utf-8

"""
从词霸中获取每日一句，带英文。
"""

import requests
from app.utils.common import (
    is_json
)

__all__ = ['get_acib_info']


def get_acib_info():
    """
    从词霸中获取每日一句，带英文。
    :return:str ,返回每日一句（双语）
    """
    print('获取格言信息（双语）...')
    try:
        resp = requests.get('http://open.iciba.com/dsapi')
        if resp.status_code == 200 and is_json(resp):
            content_dict = resp.json()
            content = content_dict.get('content')
            note = content_dict.get('note')
            return '{}{}'.format(content, note)

        print('没有获取到格言数据。')
    except requests.exceptions.RequestException as exception:
        print(exception)
    return None


get_one_words = get_acib_info

if __name__ == '__main__':
    we = get_one_words()
    print(we)
