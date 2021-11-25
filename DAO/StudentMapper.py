"""
    关于数据库的操作
"""

import sqlite3

def add_student(student):
    """
    TODO 向student表中添加一名学生信息
    :param student: student对象
    :return: None
    """
    pass
def delete_student(id):
    """
    TODO 根据学生的学号，删除表中对象的学生信息
    :param id: 学号
    :return: None
    """
    pass

def select_one_student(id):
    """
    TODO 根据学生的id查找表中对应的信息
    :param id: 学号
    :return: Student
    """
    pass

def select_all_student():
    """
    TODO 查询student表中的所有信息，并将其封装为列表
    :return:list(Student)
    """
    pass

def select_special_student(sql_special):
    """
    TODO 特殊sql语句的查询 并将其结果封装为Student类型的列表
    :param sql_special: 特殊的sql条件
    :return: list(Student)
    """
    pass

def update_student(student):
    """
    TODO 修改学生的信息，其中student.id做为修改的查询条件
    :param student: 学生对象，其中id不能改变，其余信息为要修改的值
    :return: None
    """
    pass



