# 目标:使用suite管理测试用例,并生成测试报告

# 导包
import unittest
import time

from HTMLTestRunner_PY3 import HTMLTestRunner



# 实例化suite对象
from test_ihrm_system.app import BASEPATH
from test_ihrm_system.script.test_emp import TestEmp
from test_ihrm_system.script.test_login import TestLogin

suite = unittest.TestSuite()
# 在suite里面添加测试用例
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestEmp))
# 运行测试用例,并生成测试报告
report_path = BASEPATH + "/report/ihrm{}.html".format(time.strftime("%Y%m%d %H%M%S"))
with open(report_path,"wb") as f:
    runner = HTMLTestRunner(f,
                            verbosity=1,
                            title="IHRM人力资源管理系统",
                            description="登陆模块和员工管理模块的测试")
    runner.run(suite)






