"""
    项目的主入口
"""
from controller.StudentController import *
from controller.AdminController import *

from PySide2.QtWidgets import QApplication, QWidget, QPlainTextEdit, QLineEdit, QMessageBox, QTableWidget, \
    QTableWidgetItem
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, Qt
from PySide2.QtGui import QIcon

class views:
    pass

class Login(QWidget):
    def __init__(self):
        # 动态加载ui文件
        qtmp = QFile('view/login.ui')
        qtmp.open(QFile.ReadOnly)
        qtmp.close()
        self.ui = QUiLoader().load(qtmp)
        # 添加按钮的点击事件
        self.ui.login.clicked.connect(self.login_view)
    def login_view(self):
        """
        登录事件
        :return:
        """
        username = self.ui.username.text()
        password = self.ui.password.text()
        if username == '' and password == '':
            QMessageBox.critical(self.ui, '错误', '请先输入账号和密码')
        else:
            if login_controller(username=username, password=password) is False:
                # 登录失败
                QMessageBox.critical(self.ui, '错误', '账号或密码错误')
            else:
                # 将密码框中的中的内容清空
                self.ui.password.setText('')
                QMessageBox.information(self.ui, '成功', '登录成功')
                views.login.ui.hide()
                views.Main.ui.show()
class Min:
    def __init__(self):
        qtmp = QFile('view/main.ui')
        qtmp.open(QFile.ReadOnly)
        qtmp.close()
        self.ui = QUiLoader().load(qtmp)
        # 查询所有的学生信息并显示
        student_list = select_all_controller_student()
        # 将表格中的数据清空，并显示student_list数据
        self.show_list(student_list)
        # 为删除按钮添加点击事件
        self.ui.delete_btn.clicked.connect(self.delete_selected)
        # 为查询按钮添加点击事件
        self.ui.find_student.clicked.connect(self.find_student)
        # 为退出按钮添加事件
        self.ui.exit.clicked.connect(self.exit_win)

    def exit_win(self):
        views.login.ui.close()
        views.Main.ui.close()
    def find_student(self):
        # 获取到输入框的内容
        input_id = self.ui.input_num.text()
        input_name = self.ui.input_name.text()
        input_age = self.ui.input_age.text()
        input_gender = self.ui.input_gender.currentText()
        input_cls = self.ui.input_cls.text()
        if input_id != '':
            # 当id输入后，精确查询
            student = select_one_controller_student(int(input_id))
            if student is None:
                QMessageBox.warning(self.ui, '警告', '查无此人')
            else:
                student_list = []
                student_list.append(student)
                self.show_list(student_list)
        else:
            # 进行模糊查询
            sql = ''
            if input_name != '':
                sql += f"name = '{input_name}' and "
            if input_gender != '':
                sql += f"gender = '{input_gender}' and "
            if input_age != '':
                sql += f"age = {int(input_age)} and "
            if input_cls != '':
                sql += f"cls = '{input_cls}' and "
            if len(sql) == 0:
                QMessageBox.warning(self.ui, '警告', '为输入查询内容')
            sql = sql[:-5]
            student_list = select_special_controller_student(sql)
            if student_list is None:
                QMessageBox.warning(self.ui, '警告', '查无此人')
            self.show_list(student_list)
    # 删除选中
    def delete_selected(self):
        ids = self.getSelected()
        for delete_id in ids:
            if delete_controller_student(int(delete_id)) != 1:
                QMessageBox.critical(self.ui, '错误', '删除失败')
                return
        # 刷新表格
        student_list = select_all_controller_student()
        self.show_list(student_list)

    def getSelected(self):
        select_all = self.ui.table.selectedIndexes()
        rows = []
        for select in select_all:
            # 获取选中的行
            rows.append(select.row())
        # 去重
        rows = list(set(rows))
        select_id_list = []
        for row in rows:
            select_id = self.ui.table.item(row, 0).text()
            select_id_list.append(select_id)
        return select_id_list
    def cfgItemChanged(self, row, column):
        # 获取更改内容
        try:
            # 判断用户点击的是不是最后一行
            # print(row, self.ui.table.rowCount())

            stu_id = self.ui.table.item(row, 0).text()  # 首列为配置名称
            update_name = self.ui.table.item(row, 1).text()
            update_age = self.ui.table.item(row, 2).text()
            update_gender = self.ui.table.item(row, 3).text()
            update_cls = self.ui.table.item(row, 4).text()
            # print(stu_id,update_name,update_age,update_gender,update_cls)
            # 添加 业务
            if stu_id == '':
                if add_controller_student(name=update_name, age=int(update_age), gender=update_gender, cls=update_cls) != 1:
                    # 添加失败
                    QMessageBox.critical(self.ui, '错误', '添加失败')
                else:
                    # 添加成功
                    student_list = select_all_controller_student()
                    self.show_list(student_list)
            else:
                # 封装成对象
                student = Student(id=stu_id, name=update_name, gender=update_gender, age=update_age, cls=update_cls)
                # 修改业务的实现
                if update_controller_student(student) != 1:
                    # 修改失败
                    QMessageBox.critical(self.ui, '错误', '修改失败')
        except:
            pass
    def show_list(self, student_list):
        # 将列表清空
        self.ui.table.clearContents()
        self.ui.table.setRowCount(0)
        # self.ui.QTableWidget.
        for index, student in enumerate(student_list):
            stu_id = QTableWidgetItem()
            stu_name = QTableWidgetItem()
            stu_age = QTableWidgetItem()
            stu_gender = QTableWidgetItem()
            stu_cls = QTableWidgetItem()
            stu_id.setText(str(student.id))
            stu_id.setFlags(Qt.ItemIsEnabled)
            stu_id.setTextAlignment(Qt.AlignCenter)
            stu_name.setText(str(student.name))
            stu_name.setTextAlignment(Qt.AlignCenter)
            stu_age.setText(str(student.age))
            stu_age.setTextAlignment(Qt.AlignCenter)
            stu_gender.setText(str(student.gender))
            stu_gender.setTextAlignment(Qt.AlignCenter)
            stu_cls.setText(str(student.cls))
            stu_cls.setTextAlignment(Qt.AlignCenter)
            self.ui.table.insertRow(index)
            self.ui.table.setItem(index, 0, stu_id)
            self.ui.table.setItem(index, 1, stu_name)
            self.ui.table.setItem(index, 2, stu_age)
            self.ui.table.setItem(index, 3, stu_gender)
            self.ui.table.setItem(index, 4, stu_cls)
        # 为表格添加修改事件
        # 插入一行空列表，用于添加学生信息
        # print(len(student_list)+1)
        self.ui.table.insertRow(len(student_list))
        # 设置第一列不能修改
        item = QTableWidgetItem('')
        item.setFlags(Qt.ItemIsEnabled)  # 参数名字段不允许修改
        self.ui.table.setItem(len(student_list), 0, item)
        self.ui.table.cellChanged.connect(self.cfgItemChanged)

if __name__ == '__main__':
    app = QApplication([])
    views.login = Login()
    views.Main = Min()
    views.login.ui.show()
    app.exec_()



