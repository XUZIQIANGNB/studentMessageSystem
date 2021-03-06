"""
    学生信息类
        成员变量
            学号:id 唯一、非空、int
            名字: name 非空、str
            年龄: age 非空 、int
            家庭住址: home 非空、str
            身份证号: IDCard 非空、str
            班级：cls 非空 str
        成员方法：
            __init__ ：初始化函数，将学生的信息插入
            addInformation： 完善学生的信息
"""

class Student(object):
    # 初始化函数  管理员创建出学生的名字、班级
    def __init__(self, name=None, cls=None, gender=None, age=None, id=None):
        self.id = id
        self.name = name
        self.cls = cls
        self.age = age
        self.gender = gender
    # 1911014001  19  04
    def getmessage(self):
        # 按照 学号 姓名  年龄  性别   班级   身份证号    家庭住址
        return f'{self.id}\t{self.name}\t{self.age}\t{self.gender}\t{self.cls}'
