# 安卓端部分

### 核心目标

实现交换唯一身份验证码
从服务器后端下载一份到多份身份码(可以考虑码+tag或者是许多表的形式)
\*实现信息展示
实现激进模式
实现激进模式的接收
\*保证传输的稳定性
key : 保证程序在后台运行时候的稳定性和可观察性(包括意外退出检测, 包括常驻通知 或者是图标颜色变化)

### 附加目标

防止广播干扰破坏, 增加安全性
想办法降低功耗
包含时间戳和记录时间戳选项 :
- 本地必须记录时间戳
- 但时间戳可选择并不上报(甚至可以完全打乱顺序后上报)
- 拥有时间戳后可以提供更多更细致的信息

# web后端部分


# qq机器人部分