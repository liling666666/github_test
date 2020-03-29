# 导包
import requests


# 封装登陆接口
class LoginApi():
    def __init__(self):
        # 定义ihrm登陆接口url
        self.login_url = "http://182.92.81.159/api/sys/login"

    # 定义封装登陆的函数
    def login(self, jsonData, headers):
        response = requests.post(url=self.login_url, json=jsonData, headers=headers)
        return response

# 防止在导入时执行类外面的代码
# if __name__ == "__main__":
#     login_api = LoginApi()
#     jsonData = {"mobile":"13800000002","password":"123456"}
#     headers = {"Content-Type":"application/json"}
#     response = login_api.login(jsonData,headers)
#     print("登陆结果为:",response.json())
