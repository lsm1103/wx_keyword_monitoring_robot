# from redis import ConnectionPool
# pool = ConnectionPool(host='localhost', port=6379, db=2 )
"""项目配置"""
version = '0.1'

# 机器人主人 ，使用备注名更安全，只允许一个，可远程控制机器人，如果不设置(空)则将文件助手设置为管理员，但不具备远程控制功能
bot_master_name = '小民'

# ---------------------------------------自动回复机器人功能设置--------------------------------------start
robot_list = {
    # 图灵机器人(http://www.tuling123.com/) 实名后的用户每天免费可用 100 条。88f17f853d974387af64955bed9466f4  99元一月付费版,尽情享用！
    'tuling': {'api_key': 'c6c83055db1a45c1b54ad5f125096a50'},
    # 天行机器人 ( https://www.tianapi.com/apiview/47 )。做完任务大概能免费用7万条，收费：1万条/1块钱; reply_name:回复的人的名字(可空)（也可在个人中心->机器人管理 修改）bot_name:机器人的名字（可空）
    'txapi': {'api_key': '个人中心中的key', 'reply_name': 'bbb', 'bot_name': 'xxx'},
    # 智能闲聊（腾讯）https://ai.qq.com/product/nlpchat.shtml。免费且无限量
    'qqnlpchat': {'api_id': '2125284154', 'api_key': 'KjTt71IoDe0xRG3V'},
    # 海知智能 <https://ruyi.ai/> 功能很强大，不仅仅用于聊天。需申请 key，免费
    'ruyi': {'api_key': '你申请的key'},
    # 思知机器人 <https://www.ownthink.com/> 免费，如果只是简单使用 app_key 可不申请。
    'ownthink': {'api_key': ''},
    # 一个 Al (http://www.yige.ai/)（已长时间无人维护）
    'yigeai': {'client_token': '你申请的token'},
}
# 机器人渠道（1: 图灵机器人，2: 一个AI ,3 : 青云客，4 腾讯智能闲聊，5:天行机器人,6：海知智能，7：思知机器人)
bot_channel: 'ownthink'
# ---------------------------------------自动回复机器人功能设置--------------------------------------end

# ---------------------------------------定时提醒功能设置--------------------------------------start
# True 开启定时提醒，False 关闭
is_alarm = True
alarm_info = {
    '首选大家族': {
        'user_group': False,  # 选择【True:客户 / False:群聊】进行消息定时推送,群和人只能选其一
        # [1:客户微信昵称或者备注名(不能输入微信号) / 2:群聊的名称] 必须要把需要的群聊保存到通讯录，往群定时推送消息
        'name': ['测试01', '【首选】总经办'],
        'alarm_timed': ["8:54", "18:23", "22:05"],  # 定时发送的时间
        'alarm_jitter': 0,  # 给定时时间加一个随机抖动 300 秒。定时时间【-5，+5】分钟范围内发送。（不然每天固定在同个时间段有点尴尬）（可空）
        'is_tomorrow': True,  # 是否发送明日信息（如天气，星座，万年历）
        'city_name': '杭州',   # 所在城市，用于发送天气。（可空）
        'air_quality_city': '杭州',    # 此城市的 pm2.5 值。
        # 格言渠道（1 : ONE●一个，2 : 词霸（每日英语，双语）3: 土味情话 4 : 一言，5：笑话，6 民国情书,7彩虹屁)(可空)
        'dictum_channel': 1,
        'start_date': '2018-6-15',  # 从哪天开始联系的（可空），配合 start_date_msg 使用。
        # 自定义方案（可空）， {}表示用于占位，代表天数，与 start_date 一起使用。单填无意义  默认为：『这是我们开始联系的第{}天』,参考：我们认识的第{}天
        'start_date_msg': '这是首选出生的第{}天',
        'calendar': True,   # 万历年（可空），（中老年最爱）
        # 星座运势（可空）填生日日期："1980-06-15" or "06-15" or "白羊座"，获取客户的生日自动做星座运势
        'horescope': "2018-6-15",
        'sweet_words': '--首选小x'    # 落款（可空），落款参考：['--首选小伍', '--首选小李'，'--首选小王']
    },
    '老婆': {
        'user_group': True,  # 选择【True:客户 / False:群聊】进行消息定时推送,群和人只能选其一
        # [1:客户微信昵称或者备注名(不能输入微信号) / 2:群聊的名称] 必须要把需要的群聊保存到通讯录，往群定时推送消息
        'name': ['老婆'],
        'alarm_timed': ["8:54", "12:20", "14:20", "18:23", "22:05"],  # 定时发送的时间
        'alarm_jitter': 0,  # 给定时时间加一个随机抖动 300 秒。定时时间【-5，+5】分钟范围内发送。（不然每天固定在同个时间段有点尴尬）（可空）
        'is_tomorrow': True,  # 是否发送明日信息（如天气，星座，万年历）
        'city_name': '义乌',  # 所在城市，用于发送天气。（可空）
        'air_quality_city': '义乌',  # 此城市的 pm2.5 值。
        # 格言渠道（1 : ONE●一个，2 : 词霸（每日英语，双语）3: 土味情话 4 : 一言，5：笑话，6 民国情书,7彩虹屁)(可空)
        'dictum_channel': 4,
        'start_date': '2017-10-16',  # 从哪天开始联系的（可空），配合 start_date_msg 使用。
        # 自定义方案（可空）， {}表示用于占位，代表天数，与 start_date 一起使用。单填无意义  默认为：『这是我们开始联系的第{}天』,参考：我们认识的第{}天
        'start_date_msg': '这是我爱你的第{}天😍',
        'calendar': True,  # 万历年（可空），（中老年最爱）
        # 星座运势（可空）填生日日期："1980-06-15" or "06-15" or "白羊座"，获取客户的生日自动做星座运势
        'horescope': "1998-1-27",
        'sweet_words': '--小民'  # 落款（可空），落款参考：['--首选小伍', '--首选小李'，'--首选小王']
    }
}
# ---------------------------------------定时提醒功能设置--------------------------------------end

# 自动回复
is_friend_auto_reply = False  # 好友自动回复
is_group_reply = False  # 此项表示是否所有群自动回复
is_group_at_reply = False  # 上一项开启后此项才生效 是否才@我回复
is_forward_revoke_msg = True  # 开启防撤回模式
is_forward_group_at_msg = True  # 转发群@我的消息

# 白名单
white_list = ['测试01', '群监控结果展示', '首选大家族', '【首选】总经办','测试02']
# 黑名单
black_list = ['16级新生群']

# 监听某些销售资源-群聊，如老板xx资源群
is_listen_zy_groups = True
# 在这些销售资源群里监听好友说的话，匹配模式：包含“xxx销售资源群”的群，以字典的value来区分部门，如：1:猎头，2:建筑，3:财务，4:电商，5:总经理
# listen_zy_groups = ['测试01']
group_type = {'0':'keyword_data', '1':'lt_keyword_data', '2':'jz_keyword_data', '3':'cw_keyword_data','4':'ds_keyword_data','5':'zjl_keyword_data'}
listen_zy_groups = {'测试01':'0','测试02':'3', '首选大家族':'1', '【首选】总经办':'0'}

# 监听某些好友,群聊，如老板
is_listen_friend = True
listen_friend_names = ['老婆']  # 需要监听的人名称，使用备注名更安全，允许多个用|分隔，如：主管|项目经理|产品狗
listen_friend_groups = ['测试01']  # 在这些群里监听好友说的话，匹配模式：包含“唯一集团工作群”的群


# 转发信息至群
is_forward_mode = True  # 打开转发模式，主人发送给机器人的消息都将转发至forward_groups群
forward_groups = '群监控结果展示'  # 需要将消息转发的群，匹配模式同上

# 群分享监控
is_listen_sharing = True
listen_sharing_groups = '测试01'  # 监控群分享，匹配模式同上

# 群关键字监控列表
keyword = {
    'keyword_data' : ['建筑资质', '建筑资质代办', '施工许可证','安许', '安全许可证', '机电一体化', '机电安装资质', '建筑总包资质', '工商注册','许可证'],
    'cw_keyword_data' : ['建筑资质', '建筑资质代办', '施工许可证','安许', '安全许可证', '机电一体化', '机电安装资质', '建筑总包资质', '工商注册', '工商疑难处理', '许可证', '工商注销', '注册代办公司', '工商注册代办',
    '企业代办工商注册', '工商执照代办', '营业执照代办', '注册公司', '公司注册','工商执照', '企业执照', '注销公司', '开公司', '营业执照','代理注册','公司代办',
    '委托代理','经营许可证','代办edi', '代办icp', '代办idc', '代办isp', '代办sp','节目制作经营','直播平台经营','网络直播经营','小视频经营','文化传播公司','文化经营'
    ,'电视广播经营','视频平台经营','注册动漫公司','动漫制作平台','节目视频制','承办文化活动','视频网站','广播电视经营','互联网经营','互联网出版','互联网资质','网络文化经营',
    '营业性演出','互联网出版经营','进口网络游戏审批','互联网信息服务','互联网信息服务增值电信业务经营','互联网信息服务业务经营','网络游戏备案','网络经营','经营性互联网信息服务',
    '文网文','营业性演出','商业性演出','代理记账','财务代理','财务会计','财务记账','出版物经营','零售出版物','出版物零售','出版物批发','道路运输经营','进出口','对外贸易','劳务派遣'
    ,'人力资源','食品安全','医疗器械经营','税务筹划','税收筹划','纳税筹划','企业所得税','个人所得税','税收优惠政策','税收优惠减免','税收优惠方案','税筹']
}
# 新加好友首次问候
new_friend_first_greeting = '您好，我是杭州首选的，专门做企业服务的，我们已经是好友了~~'

is_dictum = True  # 是否开启一句话查询
is_weather = True  # 是否开启天气查询
is_moviebox = True  # 是否开启电影票房
is_rubbish = True  # 是否开启垃圾查询
is_calendar = True  # 是否开启万年历查询
is_air_quality = True  # 是否开启空气质量查询
is_constellation = True  # 是否开启星座查询
is_express = False  # 是否开启快递查询
# 快递鸟（http://www.kdniao.com/）
express_info = {'app_id': '你申请的api_id', 'app_key': '你申请的app_key'}

search_dict = {'天气': '天气-杭州', '票房': '票房-20200101', '垃圾分类': '垃圾分类-香蕉皮',
               '万年历': '万年历-20191231', '空气质量': '空气质量-杭州', '星座': '星座-白羊座/10.02/1996.02.01', '快递': '快递-快递号', '一句话': '一句话-1', '时间计算': '时间计算-2018.6.15'}

#--------------------------- 群聊助手设置 --------------------------end
