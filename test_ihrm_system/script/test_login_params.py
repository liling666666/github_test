# 导包
import unittest
import logging

from test_ihrm_system import app
from test_ihrm_system.api.login_api import LoginApi
from test_ihrm_system.app import BASEPATH
from test_ihrm_system.utils import assert_common_utils, read_login_data
from parameterized import parameterized

# 创建测试类


class TestLogin(unittest.TestCase):
    # 初始化测试类
    def setUp(self):
        # 实例化封装的登陆接口
        self.login_api = LoginApi()

    def tearDown(self):
        ...

    # 编写测试的函数
    filename = BASEPATH + "/data/login.json"
    # 参数化
    @parameterized.expand(read_login_data(filename))
    def test01_login_success(self,case_name,jsonData,http_code,success,code,message):
        # 定义登陆成功所需要的请求体
        jsonData1 = jsonData

        # 利用封装的登陆接口,发送登陆请求,测试ihrm系统
        response_login = self.login_api.login(jsonData1, app.headers)
        # 利用日志模块打印登陆结果
        logging.info("登陆的结果为:{}".format(response_login.json()))
        # 断言登陆的结果:响应状态码,success,code,message
        assert_common_utils(self, response_login, http_code, success, code, message)


