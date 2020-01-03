# 关于软件使用配置说明，一定要看！！！
# ps: 如果是候补车票，需要通过人证一致性核验的用户及激活的“铁路畅行”会员可以提交候补需求，请您按照操作说明在铁路12306app.上完成人证核验
# 关于候补了之后是否还能继续捡漏的问题在此说明： 软件为全自动候补加捡漏，如果软件候补成功则会停止抢票，发出邮件通知，但是不会影响你继续捡漏，
# 如果这个时候捡漏捡到的话，也是可以付款成功的，也就是说，捡漏+候补，可以最大程度提升抢票成功率

# 刷票模式：1=刷票 2=候补+刷票
ticket_type = 1


#  Depart date
station_dates = ["2020-01-21", "2020-01-22"]


# 填入需要购买的车次(list)，"G1353"
# 修改车次填入规则，注：(以前设置的车次逻辑不变)，如果车次填入为空，那么就是当日乘车所有车次都纳入筛选返回
# 不填车次是整个list为空才算，如果不是为空，依然会判断车次的，这种是错误的写法 [""], 正确的写法 []
station_trains = []

# from station
from_station = '北京'

# To station
to_station = '安阳'

# 座位(list) 多个座位ex:
# "商务座",
# "一等座",
# "二等座",
# "特等座",
# "软卧",
# "硬卧",
# "硬座",
# "无座",
# "动卧",
set_type = ["二等座", "硬卧", "软卧"]

# 当余票小于乘车人，如果选择优先提交，则删减联系人和余票数一致在提交
# bool
is_more_ticket = True

# 乘车人(list) 多个乘车人ex:
# "张三",
# "李四"
ticket_people = ['王文鑫', '孟冉']

# 12306登录账号
user = ""
pwd = ""

# 加入小黑屋时间默认为5分钟，此功能为了防止僵尸票导致一直下单不成功错过正常的票
ticket_black_list_time = 5

# 自动打码
is_auto_code = True

# 设置2本地自动打码，需要配置tensorflow和keras库，3为云打码  
auto_code_type = 3

#cloud printing server's address :
host = "120.77.154.140:8000"
req_url = "/verify/base64/"
http_type = "http"

# host = "12306.yinaoxiong.cn" # spare server 
# req_url = "/verify/base64"
# http_type = "https"

# setting up email
# email: xxx@sina.com
# notice_email_list: "123@qq.com"
# username: xxx
# password: pwd
# host: smpt.sina.com

email_conf= {
    "is_mail": True,
    "email": "",
    "notice_email_list: "",
    "username": "",
    "password": "",
    "host": "",
    }
 
 # 是否开启 server酱 微信提醒， 使用前需要前往 http://sc.ftqq.com/3.version 扫码绑定获取 SECRET 并关注获得抢票结果通知的公众号
 server_chan_conf = {
     "is_server_chan": False,
     "secret": "",
     }
 
 # cdn searching 1:opend 2:closed
 is_cdn = 1
 
 # two type of odering 1 模拟网页自动捡漏下单（不稳定），2 模拟车次后面的购票按钮下单（稳如老狗）
 order_type = 2
 
 # 下单模式 1 为预售，整点刷新，刷新间隔0.1-0.5S, 然后会校验时间，比如12点的预售，那脚本就会在12.00整检票，刷新订单
#         2 是捡漏，捡漏的刷新间隔时间为0.5-3秒，时间间隔长，不容易封ip
order_model = 1

# 是否开启代理, 0代表关闭， 1表示开始
# 开启此功能的时候请确保代理ip是否可用，在测试放里面经过充分的测试，再开启此功能，不然可能会耽误你购票的宝贵时间
# 使用方法：
# 1、在agency/proxy_list列表下填入代理ip
# 2、测试UnitTest/TestAll/testProxy 测试代理是否可以用
# 3、开启代理ip
is_proxy = 0

# 预售放票时间, 如果是捡漏模式，可以忽略此操作
open_time = "12:59:57"

# 1=>为一直随机ua,2->只启动的时候随机一次ua
random_agent = 2

passenger_ticker_str = {
    '一等座': 'M',
    '特等座': 'P',
    '二等座': 'O',
    '商务座': 9,
    '硬座': 1,
    '无座': 1,
    '软座': 2,
    '软卧': 4,
    '硬卧': 3,
    }


max_time = 3
min_time = 1


#software version
re_version = "1.2.004"