# 专门用来存放配置选项的config.py文件

class BaseConfig:
    SECRET_KEY = "your secret key"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@127.0.0.1:3306/pythonbbs?charset=utf8mb4"

class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://[测试服务器MySQL用户名]:[测试服务器密码]@[测试服务器域名]:[测试服务器端口号]/pythonbbs?charset=utf8mb4"



