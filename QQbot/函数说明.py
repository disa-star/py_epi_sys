from QQ import Group_function
qq = Group_function(452967867)  # 群号
#  所有功能需在多窗口（多线程）进行
qq.Get_messgae_and_auto_reply()  # print群内消息q 并自动回复消息 (一直运行）

qq.G_send()  # input(x), 发送x(执行一次

qq.G_picture()  # input(1.jpg), 发送图片1.jpg(执行一次
# 图片需放在 go-cqhttp - data - image文件中

qq.G_ban()  # 群禁言
qq.G_ban_cancel()  # 群解禁

qq.u_send(u_id=123)  # 发送私信（给123用户）
# 该功能目前可能用不上





