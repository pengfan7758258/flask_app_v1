from flask import Blueprint, redirect, url_for, render_template, abort, request, Response

blue = Blueprint('blue', __name__)


def init_views(app):
    app.register_blueprint(blue)


@blue.route('/login', strict_slashes=False, methods=['GET', 'POST'])
def login():
    if request.method.lower() == 'get':
        return render_template('login.html')

    username = request.form.get('username')
    resp = Response('登陆成功:%s' % username)
    resp.set_cookie('username', username)
    return resp


@blue.route('/mine', strict_slashes=False)
def mine():
    username = request.cookies.get('username')
    return "欢迎回来:%s" % username


@blue.route('/redirect')
def users():
    abort(201)
    return redirect(url_for('.index'))
