"""
    项目的主入口
"""
from entry.Student import Student

if __name__ == '__main__':
    student_list = []
    student = Student(name='蔡申傲', cls='1094')

    student_list.append(student)
    # print(student_list)

    print(student.getmessage())



