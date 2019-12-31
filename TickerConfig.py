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

# host = "12306.yinaoxiong.cn"
# req_url = "/verify/base64"
# http_type = "https"

# setting up email
# email: xxx
