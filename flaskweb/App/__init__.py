from flask import Flask

from App.ext import init_ext
from App.settings import envs
from App.views import init_views


def create_app(env):
    app = Flask(__name__)

    # 加载配置
    app.config.from_object(envs.get(env))

    # 加载扩展包
    init_ext(app=app)

    # 记载路由
    init_views(app=app)

    return app
