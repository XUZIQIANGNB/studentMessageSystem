"""
    关于数据库的操作
"""

import sqlite3
from entry.Student import Student
def add_student(student):
    """
    向student表中添加一名学生信息
    :param student: student对象
    :return: 受影响数
    """
    # 插入学生的id必须为空
    if student.id is not None:
        return 0
    connection = sqlite3.connect(r'sqlite/student_system.db')
    sql = """insert into student(name ,age, gender, cls) values (?,?,?,?)"""
    cursor = connection.cursor()
    cursor.execute(sql, (student.name, student.age, student.gender, student.cls))
    cursor.close()
    # 注意：sqlite 添加是默认开启事务的，所以需要提交事务
    connection.commit()
    connection.close()
    # 将受影响的函数 返回
    return cursor.rowcount

def delete_student(id):
    """
    根据学生的学号，删除表中对象的学生信息
    :param id: 学号
    :return: 受影响的行数，0为操作失败
    """
    # 简单的数据校验
    if isinstance(id, int) is not True and id <= 0:
        return 0
    connection = sqlite3.connect(r'sqlite/student_system.db')
    cursor = connection.cursor()
    sql = """delete from student where id = ?"""
    cursor.execute(sql, (id,))
    cursor.close()
    # 删除默认也是开启事务的，需要进行提交
    connection.commit()
    connection.close()
    return cursor.rowcount

def select_one_student(id):
    """
    根据学生的id查找表中对应的信息
    :param id: 学号
    :return: Student
    """
    # 简单校验
    if isinstance(id, int) is not True and id <= 0:
        return
    connection = sqlite3.connect(r'sqlite/student_system.db')
    cursor = connection.cursor()
    sql = "select id, name, age, gender, cls from student where id = ?"
    cursor.execute(sql, (id, ))
    # 获取结果集
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    # print(result[0])
    # 判断结果
    if len(result) == 0:
        return None
    else:
        id, name, age, gender, cls = result[0]
        student = Student(id=id, name=name, age=age, gender=gender, cls=cls)
        return student
def select_all_student():
    """
    查询student表中的所有信息，并将其封装为列表
    :return:list(Student)
    """
    connection = sqlite3.connect(r'sqlite/student_system.db')
    cursor = connection.cursor()
    sql = "select id, name, age, gender, cls from student"
    cursor.execute(sql)
    result = cursor.fetchall()
    # 关闭连接
    cursor.close()
    connection.close()
    # 封装查询数据
    if result is None:
        return None
    student_list = []
    for student_tuple in result:
        id, name, age, gender, cls = student_tuple
        student = Student(id=id, name=name, age=age, gender=gender, cls=cls)
        student_list.append(student)
    return student_list

def select_special_student(sql_special):
    """
    特殊sql语句的查询 并将其结果封装为Student类型的列表
    :param sql_special: 特殊的sql条件
    :return: list(Student)
    """
    if sql_special is None:
        return None
    connection = sqlite3.connect(r'sqlite/student_system.db')

    cursor = connection.cursor()
    # 这里使用了sql拼接，可能会存在sql注入
    sql = "select id, name, age, gender, cls from student where "+str(sql_special)
    cursor.execute(sql)
    result = cursor.fetchall()
    if result is None:
        return None
    student_list = []
    for student_tuple in result:
        id, name, age, gender, cls = student_tuple
        student = Student(id=id, name=name, age=age, gender=gender, cls=cls)
        student_list.append(student)
    # 关闭连接
    cursor.close()
    connection.close()
    return student_list

def update_student(student):
    """
    修改学生的信息，其中student.id做为修改的查询条件
    :param student: 学生对象，其中id不能改变，其余信息为要修改的值
    :return: 受影响的数
    """
    if student.id is None:
        return 0
    connection = sqlite3.connect(r'sqlite/student_system.db')
    cursor = connection.cursor()
    sql = "update student set name=? , age = ? , gender = ? , cls = ? where id = ?"
    cursor.execute(sql, (student.name, student.age, student.gender, student.cls, student.id))
    # 关闭连接，提交事务
    cursor.close()
    connection.commit()
    connection.close()
    # 返回数据库的改变数
    return cursor.rowcount



"""
    测试
"""
# if __name__ == '__main__':
#     from entry.Student import Student
    # student = Student(name='雷军', cls='计本1905班', gender='男', age=25)
    # length = add_student(student)
    # if length == 1:
    #     print('添加成功')

    # length = delete_student(16)
    # if length == 1:
    #     print('删除成功')

    # 测试根据id查询学生信息
    # select_one_student(1)

    # 测试返回所有学生的信息
    # select_all_student()

    # 测试特殊sql查询
    # select_special_student("age<20")

    # 测试修改学生的信息
    # student = Student(id=1, name='王小波', age=40, gender='男', cls='物本1586')
    # result = update_student(student)
    # if result == 1:
    #     print('修改成功')
    # else:
    #     print('修改失败')