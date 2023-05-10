# app.py文件，是项目的入口文件，会默认生成一个主路由，附带视图函数
import sqlalchemy
from flask import Flask
import config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)
HOSTNAME = "127.0.0.1"
PORT = 3306
USERNAME = "root"
PASSWORD = "root"
DATABASE = "database_learn"

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"

db = SQLAlchemy(app)

with db.engine.connect() as conn:
    rs = conn.execute("select 1")
    print(rs.fetchone())


@app.route('/')
def create_app():
    with app.app_context():
        db.init_app()
    return app


if __name__ == '__main__':
    app.run()


