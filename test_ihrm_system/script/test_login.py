# 导包
import unittest
import logging

from test_ihrm_system import app
from test_ihrm_system.api.login_api import LoginApi
from test_ihrm_system.utils import assert_common_utils


# 创建测试类


class TestLogin(unittest.TestCase):
    # 初始化测试类
    def setUp(self):
        # 实例化封装的登陆接口
        self.login_api = LoginApi()

    def tearDown(self):
        ...

    # 编写测试的函数
    # 登陆成功
    def test01_login_success(self):
        # 定义登陆成功所需要的请求体
        jsonData = {"mobile": "13800000002", "password": "123456"}

        # 利用封装的登陆接口,发送登陆请求,测试ihrm系统
        response_login = self.login_api.login(jsonData, app.headers)
        # 利用日志模块打印登陆结果
        logging.info("登陆的结果为:{}".format(response_login.json()))
        # 断言登陆的结果:响应状态码,success,code,message
        assert_common_utils(self, response_login, 200, True, 10000, "操作成功！")

    # 密码错误
    def test02_password_error(self):
        # 定义登陆成功所需要的请求体
        jsonData = {"mobile": "13800000002", "password": "1234567"}

        # 利用封装的登陆接口,发送登陆请求,测试ihrm系统
        response_login = self.login_api.login(jsonData, app.headers)
        # 利用日志模块打印登陆结果
        logging.info("登陆的结果为:{}".format(response_login.json()))
        # 断言登陆的结果:响应状态码,success,code,message
        assert_common_utils(self, response_login, 200, False, 20001, "用户名或密码错误")

    # 账号不存在
    def test03_mobile_is_not_exist(self):
        # 定义登陆成功所需要的请求体
        jsonData = {"mobile": "13900000002", "password": "123456"}

        # 利用封装的登陆接口,发送登陆请求,测试ihrm系统
        response_login = self.login_api.login(jsonData, app.headers)
        # 利用日志模块打印登陆结果
        logging.info("登陆的结果为:{}".format(response_login.json()))
        # 断言登陆的结果:响应状态码,success,code,message
        assert_common_utils(self, response_login, 200, False, 20001, "用户名或密码错误")

    # 输入的手机号码有英文字符串
    def test04_mobile_has_english(self):
        # 定义登陆成功所需要的请求体
        jsonData = {"mobile": "1380000A0X2", "password": "123456"}

        # 利用封装的登陆接口,发送登陆请求,测试ihrm系统
        response_login = self.login_api.login(jsonData, app.headers)
        # 利用日志模块打印登陆结果
        logging.info("登陆的结果为:{}".format(response_login.json()))
        # 断言登陆的结果:响应状态码,success,code,message
        assert_common_utils(self, response_login, 200, False, 20001, "用户名或密码错误")

    # 手机号码有特殊字符
    def test05_mobile_special(self):
        # 定义登陆成功所需要的请求体
        jsonData = {"mobile": "1380(*000002", "password": "123456"}

        # 利用封装的登陆接口,发送登陆请求,测试ihrm系统
        response_login = self.login_api.login(jsonData, app.headers)
        # 利用日志模块打印登陆结果
        logging.info("登陆的结果为:{}".format(response_login.json()))
        # 断言登陆的结果:响应状态码,success,code,message
        assert_common_utils(self, response_login, 200, False, 20001, "用户名或密码错误")

    # 手机号码为空--bug
    def test06_mobile_is_empty(self):
        # 定义登陆成功所需要的请求体
        jsonData = {"mobile": "", "password": "123456"}

        # 利用封装的登陆接口,发送登陆请求,测试ihrm系统
        response_login = self.login_api.login(jsonData, app.headers)
        # 利用日志模块打印登陆结果
        logging.info("登陆的结果为:{}".format(response_login.json()))
        # 断言登陆的结果:响应状态码,success,code,message
        assert_common_utils(self, response_login, 200, False, 20001, "用户名或密码错误")

    # 密码为空
    def test07_password_is_null(self):
        # 定义登陆成功所需要的请求体
        jsonData = {"mobile": "138000000002", "password": ""}

        # 利用封装的登陆接口,发送登陆请求,测试ihrm系统
        response_login = self.login_api.login(jsonData, app.headers)
        # 利用日志模块打印登陆结果
        logging.info("登陆的结果为:{}".format(response_login.json()))
        # 断言登陆的结果:响应状态码,success,code,message
        assert_common_utils(self, response_login, 200, False, 20001, "用户名或密码错误")

    # 多参-多出一个参数
    def test08_more_params(self):
        # 定义登陆成功所需要的请求体
        jsonData = {"mobile": "13800000002", "password": "123456", "sign": "123"}

        # 利用封装的登陆接口,发送登陆请求,测试ihrm系统
        response_login = self.login_api.login(jsonData, app.headers)
        # 利用日志模块打印登陆结果
        logging.info("登陆的结果为:{}".format(response_login.json()))
        # 断言登陆的结果:响应状态码,success,code,message
        assert_common_utils(self, response_login, 200, True, 10000, "操作成功")

    # 少参-缺少mobile
    def test09_less_mobile(self):
        # 定义登陆成功所需要的请求体
        jsonData = {"password": "123456"}

        # 利用封装的登陆接口,发送登陆请求,测试ihrm系统
        response_login = self.login_api.login(jsonData, app.headers)
        # 利用日志模块打印登陆结果
        logging.info("登陆的结果为:{}".format(response_login.json()))
        # 断言登陆的结果:响应状态码,success,code,message
        assert_common_utils(self, response_login, 200, False, 20001, "用户名或密码错误")

    # 少参-缺少password
    def test10_less_password(self):
        # 定义登陆成功所需要的请求体
        jsonData = {"mobile": "13800000002"}

        # 利用封装的登陆接口,发送登陆请求,测试ihrm系统
        response_login = self.login_api.login(jsonData, app.headers)
        # 利用日志模块打印登陆结果
        logging.info("登陆的结果为:{}".format(response_login.json()))
        # 断言登陆的结果:响应状态码,success,code,message
        assert_common_utils(self, response_login, 200, False, 20001, "用户名或密码错误")

    # 无参
    def test11_params_is_null(self):
        # 定义登陆成功所需要的请求体
        jsonData = None

        # 利用封装的登陆接口,发送登陆请求,测试ihrm系统
        response_login = self.login_api.login(jsonData, app.headers)
        # 利用日志模块打印登陆结果
        logging.info("登陆的结果为:{}".format(response_login.json()))
        # 断言登陆的结果:响应状态码,success,code,message
        assert_common_utils(self, response_login, 200, False, 99999, "系统繁忙")

    # 输入错误的参数
    def test12_params_error(self):
        # 定义登陆成功所需要的请求体
        jsonData = {"mboile": "138000000002", "password": "123456"}

        # 利用封装的登陆接口,发送登陆请求,测试ihrm系统
        response_login = self.login_api.login(jsonData, app.headers)
        # 利用日志模块打印登陆结果
        logging.info("登陆的结果为:{}".format(response_login.json()))
        # 断言登陆的结果:响应状态码,success,code,message
        assert_common_utils(self, response_login, 200, False, 20001, "用户名或密码错误")
