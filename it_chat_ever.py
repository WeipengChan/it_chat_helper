# coding:utf-8
import itchat,time
# import全部消息类型
from itchat.content import *
# 登录-持续
itchat.auto_login()
print(u"logged")

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING, PICTURE,
    RECORDING, VOICE, ATTACHMENT, VIDEO, FRIENDS, SYSTEM])
def simple_reply(msg):
    print(msg)
itchat.run()

while itchat.check_login:
    print("登录状态正常")
    time.sleep(10)




    # print(itchat.loginInfo)
    # mps = itchat.search_mps(name=u'QQ飞车手游')[0]
    # mps.send(u'签到')
