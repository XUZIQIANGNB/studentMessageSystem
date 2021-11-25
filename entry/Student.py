"""
    学生信息类
        成员变量
            学号:id 唯一、非空、int
            名字: name 非空、str
            年龄: age 非空 、int
            家庭住址: home 非空、str
            身份证号: IDCard 非空、str
        成员方法：
            __init__ ：初始化函数，讲学生的信息插入
            getStudentMessage: 将学生的信息按照id   name    age     home    IDCard\n

"""

class Student:
    # 初始化函数
    def __init__(self, id, name, age, home, IDCard):
        self.id = id
        self.name = name
        self.age = age
        self.home = home
        self.IDCard = IDCard
