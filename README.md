# 学生信息管理系统
> 使用语言：python3.8
> 所用技术：SQLite3,PySide2,xlrd,xlwt
> 使用Java开发中的MVC思想，代码虽有冗余，但更容易维护
## 数据库持久化
1. 使用`SQLite3`创建学生信息管理系统所需数据表的数据库：`student_system`数据库
2. 创建学生表，对项目中的学生信息进行存储
```sqlite
-- 学生表
create table student_system.student(
    id integer primary key autoincrement, -- 学号 int类型、主键、自增
    name text not null ,                  -- 学生姓名 name str类型、非空
    age integer default 0,             -- 学生年龄 age int类型、默认为0
    gender text default '男',           -- 学生性别 gender str类型、默认为男
    cls text not null                   -- 学生所属班级  cls str类型、非空
);
```
因为项目有登录的需求，所以创建一张管理员表
```sqlite
-- 管理员表
create table student_system.admin(
    username text not null,     -- 账号
    password text not null      -- 密码
);
```
3. 项目不需要添加管理员，管理员账号、密码的添加由管理人员代码添加
## 包介绍
### DAO包
负责将 
1.python字典对象映射为SQLite3中表的各个字段信息
2.将SQLite3中保存的数据映射为python字典对象
#### StudentMapper.py实现功能介绍
大致功能：
* `add_student(Student:student)-> None`:将传入的student字典对象添加到student表中
* `delete_student(int:student.id)-> None`: 根据学生的id删除学生信息
* `select_one_student(int:student.id) -> student`: 根据学生的id，查找学生信息，并将查找到的学生信息封装为Student对象
* `select_all_student() -> list(Student)`:将student所有数据封装为Student类型的列表
* `select_special_student(str:sql_special) -> list(Student)`:对student表进行特殊查询，根据传入的sql_special(where的条件)
* `update_student(Student:student)-> None`: student.id做为判断条件，将对象中的信息更新到student表中
#### StudentMapper.py功能介绍
* `login(username,password): -> True|False`: 对管理员输入的账号和密码进行校验
## entry包
    因为项目很小，管理就只是登录功能实现的时候用到了，所以不单独定义对象。
    进定义学生的实体类`Student`
### student.py介绍
    对数据库中student表中的字段进行映射
    `__init(self, id, name, age, gende, cls)`:初始化对象，将学生的基本信息封装为对象
    `get_message()->str`:将student对象中各个变量拼接并返回
## sqlite
此文件夹中存放的是SQLite数据库，存放的是学生信息持久化所需的数据
## view
存放的是用QT设计师制作的UI界面
## main.py
程序的主入口，调用其他包的功能，实现整个项目


## controller层介绍
### StudentController.py
```python
def add_controller_student(name, age, gender, cls):
    """
    TODO 将传入的学生的基本信息进行校验 然后封装成对象，
        调用DAO.StudentMapper中的add_student(Student:student)方法
        id 无需关心，数据库设置的是主键、自增
    :param name: 学生姓名
    :param age: 年龄
    :param gender: 性别
    :param cls: 班级
    :return: 返回受影响数"""
```
```python
def delete_controller_student(id):
    """
    TODO 根据传入的id删除学生的信息
    :param id: 学号
    :return: 受影响数
    """
```
```python
def select_one_controller_student(id):
    """
    TODO 根据传入的id查找学生的信息
    :param id: 学号
    :return: Student
    """
```
```python
def select_all_controller_student():
    """
    TODO 查找所有的学生信息
    :return: list(Student)
    """
```
```python
def select_special_controller_student(sql):
    """
    TODO 特殊查询，判断各个变量是否为空，然后将变量名和值拼接成SQL语句（str）
        然后调用DAO层的方法
        例如： f'id={student.id} and name={student.name}'
    :param sql : 要特殊查询的语句
    :return: 查询到的list(Student)类型的列表
    """
```
```python
def update_controller_student(student):
    """
    TODO 根据学生id修改学生的信息，id必须要有
    :param student: 要修改的信息
    :return: 受影响数
    """
```
```python
def add_list_controller_student(file_path):
    """
    TODO 从Excel表中导入学生信息
    :param file_path : 要读取的Excel文件的路径
    :return: True|False  是否导入成功
    """
```
```python
def export_controller_student(file_path, student_list):
    """
    TODO 将学生的信息导出到Excel
    :param file_path: 要导出文件路径
    :param student_list: 要导出的学生对象
    :return: True|False 是否导出成功
    """
```
```python
def writeInstance(sheet):
    """
    TODO 写入表头和实例
    :param sheet:
    :return: True|False 是否写入成功
    """
```
### AdminController.py
```python
def login_controller(username, password):
    """
    TODO 管理员登录的控制层 (要做简单的校验--校验是否为空)
    :param username: 账号
    :param password: 密码
    :return: True|False 是否登录成功
    """
```

### main.py对项目整合
```python
"""
    项目的主入口
"""
from controller.StudentController import *
from controller.AdminController import *

from PySide2.QtWidgets import QApplication, QWidget, QPlainTextEdit, QLineEdit, QMessageBox, QTableWidget, \
    QTableWidgetItem, QFileDialog
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
        # 设置程序的图标
        app_icon = QIcon('view/logo.ico')
        self.ui.setWindowIcon(app_icon)
        self.ui.username.setFocus()
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
        # 设置程序的图标
        app_icon = QIcon('view/logo.ico')
        self.ui.setWindowIcon(app_icon)
        # 查询所有的学生信息并显示
        self.student_list = select_all_controller_student()
        # 将表格中的数据清空，并显示student_list数据
        self.show_list()
        # 为删除按钮添加点击事件
        self.ui.delete_btn.clicked.connect(self.delete_selected)
        # 为查询按钮添加点击事件
        self.ui.find_student.clicked.connect(self.find_student)
        # 为退出按钮添加事件
        self.ui.exit.clicked.connect(self.exit_win)
        # 为导入按钮添加点击事件
        self.ui.btn_in.clicked.connect(self.fileDialog)
        # 为导出按钮添加点击事件
        self.ui.btn_out.clicked.connect(self.export)
    # 导出
    def export(self):
        # print(self.student_list)
        if not self.student_list:
            QMessageBox.warning(self.ui, '警告', '导出数据为空')
            return
        filepath = QFileDialog.getExistingDirectory(self.ui, '请选择到导出的目录')
        if export_controller_student(filepath, self.student_list) is True:
            QMessageBox.information(self.ui, '成功', '导出成功')
    # 导入
    def fileDialog(self):
        filepath = QFileDialog.getOpenFileName(self.ui, "选择要导入的文件", filter="XLS 工作表 (*.xls)")
        if filepath == '' or filepath[0] == '':
            QMessageBox.critical(self.ui, '错误', '未选择文件')
        else:
            if add_list_controller_student(filepath[0]) is False:
                QMessageBox.critical(self.ui, '错误', '导入数据失败')
            else:
                QMessageBox.information(self.ui, '成功', '导入数据成功')
                # 成功的话 重新刷新
                self.student_list = select_all_controller_student()
                self.show_list()


    def exit_win(self):
        views.Main.ui.close()
        views.login.ui.show()
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
                self.student_list = []
                self.student_list.append(student)
                self.show_list()
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
                QMessageBox.warning(self.ui, '警告', '未输入查询内容')
                # 未输入任何内容，则为刷新
                self.student_list = select_all_controller_student()
                self.show_list()
            sql = sql[:-5]
            self.student_list = select_special_controller_student(sql)
            if self.student_list is None:
                QMessageBox.warning(self.ui, '警告', '查无此人')
            self.show_list()
    # 删除选中
    def delete_selected(self):
        ids = self.getSelected()
        if ids[len(ids)-1] == '':
            ids.remove('')
        for delete_id in ids:
            if delete_controller_student(int(delete_id)) != 1:
                QMessageBox.critical(self.ui, '错误', '删除失败')
                return
        # 刷新表格
        self.student_list = select_all_controller_student()
        self.show_list()

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
                    self.student_list = select_all_controller_student()
                    self.show_list()
            else:
                # 封装成对象
                student = Student(id=stu_id, name=update_name, gender=update_gender, age=update_age, cls=update_cls)
                # 修改业务的实现
                if update_controller_student(student) != 1:
                    # 修改失败
                    QMessageBox.critical(self.ui, '错误', '修改失败')
        except:
            pass
    def show_list(self):
        # 将列表清空
        self.ui.table.clearContents()
        self.ui.table.setRowCount(0)
        # self.ui.QTableWidget.
        for index, student in enumerate(self.student_list):
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
        self.ui.table.insertRow(len(self.student_list))
        # 设置第一列不能修改
        item = QTableWidgetItem('')
        item.setFlags(Qt.ItemIsEnabled)  # 参数名字段不允许修改
        self.ui.table.setItem(len(self.student_list), 0, item)
        self.ui.table.cellChanged.connect(self.cfgItemChanged)

if __name__ == '__main__':
    app = QApplication([])
    views.login = Login()
    views.Main = Min()
    # views.Main.ui.show()
    views.login.ui.show()
    app.exec_()
```