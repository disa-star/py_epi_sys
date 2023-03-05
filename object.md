# 项目总览

### python 版本

请沟通python版本(尤其是web后端和qq机器人部分需要尽可能使用相同的版本)

请沟通flask版本, 此处如果有必要可以使用anaconda

(3.1日更新) 请尽可能使用anaconda 下载地址 [https://www.anaconda.com/products/distribution](https://www.anaconda.com/products/distribution) 

熟悉anaconda: 首先在程序搜索中找到 "Anaconda Prompt(anaconda3)" 并点击运行

而后使用 `conda info --envs` 查看已有环境

用`conda create -n py3.8 python=3.8` 来新建一个py3.8版本的环境

`conda activate py3.8` 切换到指定版本

而后可以在这个版本使用 pip install 等指令, 下载包并控制版本

而后在py3.8启用的时候, 使用 `conda env export > environment.yml` 来在当前目录下生成一个环境配置信息文件

使用 `conda env create -f environment.yml` 读入配置文件并在本地创建一个新环境

**我们并不一定要用anaconda控制版本, 但是需要用yml来统一版本信息(尤其是web和qq机器人部分)**

每个支持python的IDE应该都支持使用yml, 并且我的visual studio可以连接到这个环境

**在此我强烈推荐先新建一个完全新的python环境(没有任何第三方包), 而后web和qq在任何一方需要下载新的第三方包时, 都要更新这个yml文件**, 最好的话可以在每次pull之后就使用得到的yml文件更新一下自己的环境(但这样有点浪费时间), 至少要确保yml文件在你们push的时候和自己的环境相一致, 并且在最后出成果交付的时候要统一


(3.2日更新)

tips: 如果发现 anaconda 各种无法连接到 github, 考虑一下设置 git \\ conda 的代理和 pip 的代理 **注意, 代理主要分为vpn和http两种, vpn无需像这样进行设置, 但http代理需要设置, 具体情况(ip和端口请根据实际情况进行改动)**

(3.5日更新)

建议在仓库的根目录创建一个anaconda虚拟环境, 并在本机上使用这个虚拟环境(具体怎么将vscode和vs连接到虚拟环境请自行百度)

并且, 尽可能使用 `pip install` 而不是 `conda install` 来下载第三方库, 并且请记住, 尽可能在虚拟环境中不要出现任何的项目中用不到的库, 如果出现了一不小心装错了的情况, 请在github客户端内选择discard changes

根目录下存在着一些操作系统自行创建的文件, **一定要记得最后要删掉他们**


这是anaconda的
```
conda config --set proxy_servers.http http://127.0.0.1:4780
conda config --set proxy_servers.https https://127.0.0.1:4780
```

这是pip的
```
set HTTP_PROXY=http://127.0.0.1:4780 
```

这是git的
```
git config --global http.proxy 127.0.0.1:4780 
git config --global https.proxy 127.0.0.1:4780 
```


# 安卓端部分

### 项目全局信息

将会在/Android_app文件夹下进行

由于beeware必须要项目名, 项目名设置为`pytector`

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

###核心目标

查询用户自己的身份验证码

身份验证码的数据库建构和操作，如阳性人员验证码的登记等

信息发布模块，及时通报阳性人员的表单来自动判断是否接触

（高速，稳定地提供和获取数据）

###附加任务

ban ip和流量监控的服务器安全

# qq机器人部分
1