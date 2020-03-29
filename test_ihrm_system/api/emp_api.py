# 导包
import requests


# 创建封装的类
class EmpApi():
    def __init__(self):
        self.emp_url = "http://182.92.81.159" + "/api/sys/user"

    # 添加员工接口
    def add_emp(self, username, mobile, headers):
        jsonData = {"username": username,
                    "mobile": mobile,
                    "timeOfEntry": "2020-03-16",
                    "formOfEmployment": 2,
                    "departmentName": "snowsnow",
                    "departmentId": "1226092852421177344",
                    "correctionTime": "2020-03-15T16:00:00.000Z"}
        return requests.post(url=self.emp_url,
                             json=jsonData,
                             headers=headers)

    # 查询员工接口
    def search_emp(self, emp_id, headers):
        # 拼接查询员工的url
        search_url = self.emp_url + "/" + emp_id
        return requests.get(url=search_url, headers=headers)

    # 修改员工接口
    def update_emp(self, emp_id, username, headers):
        # 拼接修改员工的url
        update_url = self.emp_url + "/" + emp_id
        # 设置修改的请求体
        jsonData = {"username": username}
        return requests.put(url=update_url, json=jsonData, headers=headers)

    # 删除员工接口
    def delete_emp(self, emp_id, headers):
        delete_url = self.emp_url + "/" + emp_id
        return requests.delete(url=delete_url, headers=headers)
