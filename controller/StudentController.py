"""
    学生类的控制层
"""
from DAO.StudentMapper import *
import xlrd
import xlwt

def add_controller_student(name, age, gender, cls):
    """
    将传入的学生的基本信息进行校验 然后封装成对象，
        调用DAO.StudentMapper中的add_student(Student:student)方法
        id 无需关心，数据库设置的是主键、自增
    :param name: 学生姓名
    :param age: 年龄
    :param gender: 性别
    :param cls: 班级
    :return: 返回受影响数
    """
    if name is None or age is None or gender is None or cls is None:
        return 0
    student = Student(name=name, age=age, gender=gender, cls=cls)
    return add_student(student)

def delete_controller_student(id):
    """
    根据传入的id删除学生的信息
    :param id: 学号
    :return: 受影响数
    """
    if id is None:
        return 0
    return delete_student(id)


def select_one_controller_student(id):
    """
    根据传入的id查找学生的信息
    :param id: 学号
    :return: Student
    """
    if id is None:
        return None
    return select_one_student(id)

def select_all_controller_student():
    """
    查找所有的学生信息
    :return: list(Student)
    """
    return select_all_student()

def select_special_controller_student(sql):
    """
    特殊查询，判断各个变量是否为空，然后将变量名和值拼接成SQL语句（str）
        然后调用DAO层的方法
        例如： f'id={student.id} and name={student.name}'
    :param sql : 要特殊查询的语句
    :return: 查询到的list(Student)类型的列表
    """
    student_list = select_special_student(sql)
    # for student in student_list:
    #     print(student.getmessage())
    return student_list
def update_controller_student(student):
    """
    根据学生id修改学生的信息，id必须要有
    :param student: 要修改的信息
    :return: 受影响数
    """
    if student.id is None:
        return 0
    return update_student(student)

# 拓展业务， 把基础的实现之后，再去实现
def add_list_controller_student(file_path):
    """
    从Excel表中导入学生信息
    :param file_path : 要读取的Excel文件的路径
    :return: True|False  是否导入成功
    """
    data = xlrd.open_workbook(file_path)
    table = data.sheets()[0]    # 读取第一个文件
    nrows = table.nrows     # 获取文件的行数
    if nrows <= 2:
        return False
    else:
        student_list = []
        for row in range(2, nrows):
            input_name = table.row_values(row)[1]
            input_age = table.row_values(row)[2]
            input_gender = table.row_values(row)[3]
            input_cls = table.row_values(row)[4]
            # input_cls = table.row_values(row)[5]
            # print(input_name, input_age, input_gender, input_cls)
            if input_name == '' or input_age == '' or input_gender == '' or input_cls == '':
                return False
            student_list.append(Student(name=input_name, age=int(input_age), gender=input_gender, cls=input_cls))
        for student in student_list:
            if add_student(student) != 1:
                return False

    pass
def export_controller_student(file_path, student_list):
    """
    将学生的信息导出到Excel
    :param file_path: 要导出文件路径
    :param student_list: 要导出的学生对象
    :return: True|False 是否导出成功
    """
    wbk = xlwt.Workbook(encoding='utf-8')
    sheet = wbk.add_sheet('sheet1')
    writeInstance(sheet)
    for row, student in enumerate(student_list):
        sheet.write(row+2, 0, student.id)
        sheet.write(row+2, 1, student.name)
        sheet.write(row+2, 2, student.age)
        sheet.write(row+2, 3, student.gender)
        sheet.write(row+2, 4, student.cls)
    wbk.save(file_path + r'\学生数据.xls')
    return True

def writeInstance(sheet):
    """
    写入表头和实例
    :param sheet:
    :return: True|False 是否写入成功
    """
    sheet.write(0, 0, '学号')
    sheet.write(0, 1, '姓名')
    sheet.write(0, 2, '年龄')
    sheet.write(0, 3, '性别')
    sheet.write(0, 4, '班级')
    # 写入第一行的实例内容
    sheet.write(1, 0, '导入数据时,学号必须为空')
    sheet.write(1, 1, '例：张三')
    sheet.write(1, 2, '例：20')
    sheet.write(1, 3, '例：男')
    sheet.write(1, 4, '例：计本1904班')
    sheet.write(1, 5, '此行为实例，不能删除')
    return True



if __name__ == '__main__':
    # 测试
    # 添加
    # print(add_controller_student('小名', 20, '男', '1958'))
    # 删除
    # print(delete_controller_student(17))
    # 查询
    # student = select_one_controller_student(15)
    # print(student.getmessage())

    # student_list = select_all_controller_student()
    # for student in student_list:
    #     print(student.getmessage())

    # 修改
    # stu = Student(name='李四', age='15', gender='男', cls='1875', id=1)
    # print(update_controller_student(stu))

    # select_special_controller_student(f"name={str}")
    # 测试导入文件
    # add_list_controller_student(r'C:\Users\caishenao\Desktop\新建 XLS 工作表.xls')
    student_list = select_all_controller_student()
    export_controller_student(r'C:\Users\caishenao\Desktop', student_list)