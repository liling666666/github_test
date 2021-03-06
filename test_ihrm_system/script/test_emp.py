# 按照设计顺序编写员工模块的增删改查测试用例脚本

# 导包
import unittest
import logging
# 创建测试类
import requests

from test_ihrm_system import app
from test_ihrm_system.api.emp_api import EmpApi
from test_ihrm_system.api.login_api import LoginApi
from test_ihrm_system.utils import assert_common_utils


class TestEmp(unittest.TestCase):
    # 初始化
    def setUp(self):
        # 实例化登陆封装的接口
        self.login_api = LoginApi()
        # 设置变量保存添加员工接口url
        self.emp_url = "http://182.92.81.159" + "/api/sys/user"
        # 实例化添加员工接口
        self.emp_api = EmpApi()

    def tearDown(self):
        ...

    # 编写测试员工增删改查的用例
    def test01_test_emp_operation(self):
        # 首先实现登陆接口
        response = self.login_api.login({"mobile": "13800000002",
                                         "password": "123456"},
                                        headers=app.headers)
        # 提取登陆接口返回的json数据
        result = response.json()
        # 输出登陆的结果
        logging.info("员工模块登陆 接口的结果为:{}".format(result))
        # 提取令牌,并保存到请求头当中
        token = result.get("data")
        headers1 = {"Content-Type": "application/json", "Authorization": "Bearer " + token}
        logging.info("登陆成功后设置的请求头为:{}".format(headers1))

        # 实现添加员工接口
        response_add = self.emp_api.add_emp("爱因斯坦SS0503", "14589042803", headers1)
        # 获取添加员工返回的json数据
        add_result = response_add.json()
        logging.info("添加员工接口返回的结果为:{}".format(add_result))
        # 提取员工id,并保存到变量当中
        emp_id = add_result.get("data").get("id")
        logging.info("获取的员工的id为:{}".format(emp_id))
        # 断言添加成功
        assert_common_utils(self, response_add, 200, True, 10000, "操作成功")

        # 实现查询员工接口
        # 发送查询员工的接口请求
        response_search = self.emp_api.search_emp(emp_id, headers1)
        logging.info("查询员工接口返回的结果为:{}".format(response_search.json()))
        # 断言查询员工
        assert_common_utils(self, response_search, 200, True, 10000, "操作成功")

        # 实现修改员工接口
        # 发送修改员工接口请求
        response_update = self.emp_api.update_emp(emp_id, "tom", headers1)
        logging.info("修改员工接口返回的结果为:{}".format(response_update.json()))
        # 断言修改员工
        assert_common_utils(self, response_update, 200, True, 10000, "操作成功")

        # 实现删除员工接口
        # 发送删除员工接口请求
        response_delete = self.emp_api.delete_emp(emp_id, headers1)
        logging.info("删除员工接口的返回结果为:{}".format(response_delete.json()))
        # 断言删除员工
        assert_common_utils(self, response_delete, 200, True, 10000, "操作成功")
