from flask import Flask, make_response
import json

#from config import DEBUG
__author__ = 'Justin'

app = Flask(__name__)
# 从from_object里面定义的变量必须大写，否则会报错
app.config.from_object('config')

# 业务逻辑<=>视图函数=>mvc里面的control
# 路由<=>@app.route(url)
# 通过http请求访问这个函数,需要装饰器app.route(url)访问或执行这个函数
# 通过http://127.0.0.1:5000/hello打开网页
# flask对/hello/和hello做了重定向，保证唯一url
# 保证唯一url好处：如果2个url，2个url会被索引2次的，没有这个必要。
# 视图函数：返回返回值和一系列的附加信息：
#           status code:200,404,301
#           content-type http header
#           flask content-type默认值：content-type = text/html
#           content-type用于告诉浏览器如何解析返回的内容
# 状态码对显示或返回的内容有本质的影响
# 视图函数返回response 对象
# @app.route('/hello/')
# def hello():
#     headers = {
#         'content-type': 'text/plain',
#         'location': 'http://www.bing.com'   # 重定向
#     }
#     #response = make_response('<html></html>', 404)
#     response = make_response('<html></html>', 301)
#     response.headers = headers
#     return response

@app.route('/hello/')
def hello():
    headers = {
        'content-type': 'text/application/json',
        'location': 'http://www.bing.com'   # 重定向
    }
    #response = make_response('<html></html>', 301)
    #response.headers = headers
    # 下面返回形式本质上是将一个元组转换成一个Response对象返回
    return '<html></html>', 301, headers

# 基于类的视图（即插视图)
# app.route优点是比较简洁，缺点是不够灵活
# 若使用基于类的视图，则必须使用add_url_rule来注册路由

#app.add_url_rule('/hello/', view_func=hello)
# 开启flask的调试模式,即开启自动重启的模式
# host 0.0.0.0代表本机接受外网输出,若指定具体ip，则代表本机指定的ip接受外网输出，若不指定，则默认为127.0.0.1接受外网输出
# 生产环境通常不会使用flask自带的生产环境，而是使用：nginx + uwsgi组合来部署
# nginx作为前置服务器用来接受浏览器发送来的请求，并将请求转发给uwsgi
# uwsgi作为后置服务器调用fisher模块加载flask相关代码
# 所以说生产环境下若没有__name__ == '__main__'，fisher也会启动flask代码自带的web服务器，所以就会有2个web服务器

if __name__ == '__main__':
    #app.run(host='0.0.0.0', debug=DEBUG, port=81)
    #app.run(host='192.168.1.4', debug=True)
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
