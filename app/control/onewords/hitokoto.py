# coding=utf-8
"""
获取一言信息<https://hitokoto.cn/>
"""

import requests

__all__ = ['get_hitokoto_info']


def get_hitokoto_info():
    """
    从『一言』获取信息。(官网：https://hitokoto.cn/)
    :return: str,一言。
    """
    print('获取一言...')
    try:
        resp = requests.get('https://v1.hitokoto.cn/',
                            params={'encode': 'text'})
        if resp.status_code == 200:
            return resp.text
        print('一言获取失败。')
    except requests.exceptions.RequestException as exception:
        print(exception)
        return None
    # return None


get_one_words = get_hitokoto_info

if __name__ == '__main__':
    we = get_one_words()
    print(we)
