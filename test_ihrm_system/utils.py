import os
import json
# 封装通用断言函数


def assert_common_utils(self,
                        response,
                        http_code,
                        success,
                        code,
                        message):
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(message, response.json().get("message"))

# 封装读取登陆数据的函数
def read_login_data(filename):
    # filename:指登陆数据的路径和名称
    with open(filename,"r",encoding='utf-8') as f:

        jsonData = json.load(f)
        # 定义一个存放登陆数据的空列表
        result_list = []
        #遍历jsonData
        for login_data in jsonData:
            result_list.append(tuple(login_data.values()))
    return result_list

# 调试
# if __name__ == "__main__":
#     filename = os.path.dirname(os.path.abspath(__file__))+"/data/login.json"
#     print("路径为:",filename)
#     result = read_login_data(filename)
#     print(result)

# 封装读取员工模块数据的函数
def read_emp_data(filename,interface_name):
    with open(filename,"r",encoding='utf-8') as f:
        emp_jsonData = json.load(f)
        emp_result_list = list()
        emp_result_list.append(tuple(emp_jsonData.get(interface_name).values()))
    return emp_result_list
# 调试
if __name__ == "__main__":
    filename = os.path.dirname(os.path.abspath(__file__))+"/data/emp_data.json"
    print("路径为:",filename)
    result = read_emp_data(filename,"delete_emp")
    print(result)





