"""
    管理员表的管理
"""
import sqlite3

def login(username, password):
    """
    TODO sql语句查询
    :param username: 账号
    :param password: 密码
    :return: Ture|False
    """
    connection = sqlite3.connect('sqlite_system.db')
    connection
    connection.close()



if __name__ == '__main__':

    login('王坚', '147258')
