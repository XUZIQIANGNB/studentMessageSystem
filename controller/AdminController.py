"""
    管理员的控制层
"""
from DAO.AdminMapper import *

def login_controller(username, password):
    """
    管理员登录的控制层 (要做简单的校验--校验是否为空)
    :param username: 账号
    :param password: 密码
    :return: True|False 是否登录成功
    """
    if username is None or password is None:
        return False
    return login(username, password)

# if __name__ == '__main__':
#     print(login_controller(username='147258', password='147'))
