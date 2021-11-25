"""
    学生类的控制层
"""
import DAO.StudentMapper


def add_controller_student(name, age, gender, cls):
    """
    TODO 将传入的学生的基本信息进行校验 然后封装成对象，
        调用DAO.StudentMapper中的add_student(Student:student)方法
        id 无需关心，数据库设置的是主键、自增
    :param name: 学生姓名
    :param age: 年龄
    :param gender: 性别
    :param cls: 班级
    :return: None
    """
    pass

def delete_controller_student(id):
    """
    TODO 根据传入的id删除学生的信息
    :param id: 学号
    :return: None
    """
    pass

def select_one_controller_student(id):
    """
    TODO 根据传入的id查找学生的信息
    :param id: 学号
    :return: Student
    """
    pass

def select_all_controller_student():
    """
    TODO 查找所有的学生信息
    :return: list(Student)
    """
    pass

def select_special_controller_student(student):
    """
    TODO 特殊查询，判断各个变量是否为空，然后将变量名和值拼接成SQL语句（str）
        然后调用DAO层的方法
        例如： f'id={student.id} and name={student.name}'
    :param student : 要特殊查询的对象
    :return: 查询到的list(Student)类型的列表
    """
    pass

def update_controller_student(student):
    """
    TODO 根据学生id修改学生的信息，id必须要有
    :param student: 要修改的信息
    :return: None
    """
    pass
# 拓展业务， 把基础的实现之后，再去实现
def add_list_controller_student(file_path):
    """
    TODO 从Excel表中导入学生信息
    :param file_path : 要读取的Excel文件的路径
    :return: None
    """
    pass
def export_controller_student(file_path):
    """
    TODO 将学生的信息导出到Excel
    :param file_path: 要导出文件路径
    :return:
    """
    pass