"""
    管理员表的管理
"""
import sqlite3

def login(username, password):
    """
     sql语句查询
    :param username: 账号
    :param password: 密码
    :return: Ture|False
    """
    # 连接数据库
    connection = sqlite3.connect(r'../sqlite/student_system.db')
    # 获取一个游标
    cursor = connection.cursor()
    # 定义sql语句
    sql = """select * from admin where username = ? and password = ?"""
    # 执行sql语句
    cursor.execute(sql, (username, password))
    # 获取游标执行sql语句的结果集
    result = cursor.fetchall()
    # 关闭游标
    cursor.close()
    # 关闭连接
    connection.close()

    if len(result) == 0:
        return False
    else:
        return True

"""
    此模块的测试
"""
if __name__ == '__main__':
    is_login = login('王坚', '14725')
    if is_login:
        print('登录成功')
    else:
        print('登录失败')