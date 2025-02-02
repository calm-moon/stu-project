import os
import time
from time import sleep

class_info=[]
"""清屏"""
def clean_screen():
    os.system('cls')
"""打印首页"""
def print_menu():
    clean_screen()
    print("-------------")
    print("学生成绩管理系统")
    print("1.添加学生信息")
    print("2.查询学生信息")
    print("3.修改学生信息")
    print("4.删除学生信息")
    print("5.显示学生信息")
    print("6.显示班级整体情况")
    print("-------------")
"""新添学生"""
def add_student():
    clean_screen()
    print("欢迎使用添加学生功能")
    global class_info
    stu_id = input("请输入学生学号：\n")
    for stu_i in class_info :
        if stu_i["ID"] == stu_id :
            print("该学生成绩已经录入，请重新添加\n")
            time.sleep(2)
            add_student()
            return
    name =input("请输入学生姓名：\n")
    stu_score =[]
    stu_math = int(input("请输入学生数学成绩：\n"))
    stu_english = int(input("请输入学生英语成绩：\n"))

    score={
        "math" :stu_math,
        "english" :stu_english
    }

    student = {
        "Name" :name,
        "ID" :stu_id,
        "score" :stu_score
    }

    stu_score.append(score)
    class_info.append(student)
    print("添加成功")
    write_stu()
    time.sleep(2)
    print_menu()
"""删除学生"""
def remove_student():
    clean_screen()
    print("欢迎使用删除学生信息功能\n")
    global class_info
    stu_id = input("请输入要删除信息对应的学号：\n")
    for stu_i in class_info:
        if stu_i["ID"]== stu_id:
            class_info.remove(stu_i)
            print("删除成功\n")
            time,sleep(2)
            return
    print("未找到该同学，删除失败\n")
    time.sleep(2)
    print_menu()
"""查找学生"""
def find_student():
    clean_screen()
    global class_info
    if len(class_info) == 0:
        print("列表为空，无法查找")
    else:
        temp=input("请输入要查询的学号：")
        for stu_i in class_info:
            if stu_i["ID"] == temp:
                print_stu(stu_i)
                input("按下enter键返回菜单")
                print_menu()
                return
        print("未找到")
    time.sleep(2)
    print_menu()
"""打印学生信息"""
def print_stu(stu_i):
    print("学号：{:<12}，姓名：{:<4}，成绩：[数学：{:>3}，英语：{:>3}]".format(stu_i["ID"],stu_i["Name"],stu_i["score"][0]["math"],stu_i["score"][0]["english"]))
"""展示学生信息"""
def display_student():
    clean_screen()
    global class_info
    if len(class_info) == 0:
        print("列表为空，无法打印")
    else:
        sort_list= sorted(class_info, key= lambda x: x["ID"], reverse= False)
        for stu_i in sort_list:
            print_stu(stu_i)
    input("按下enter键返回菜单")
    print_menu()
"""展示班级信息"""
def display_class():
    clean_screen()
    global class_info
    math_temp = 0
    english_temp = 0
    max_math_score = -1
    max_english_score = -1
    min_math_score = 200
    min_english_score = 200

    len_temp = int(len(class_info))
    if len_temp == 0:
        print("无成绩录入，请下次再试")
    else:
        print("以下是班级整体情况：")
        for stu_i in class_info:
            math_temp += stu_i["score"][0]["math"]
            english_temp += stu_i["score"][0]["english"]
            if stu_i["score"][0]["math"] > max_math_score:
                max_math_score = stu_i["score"][0]["math"]
            if stu_i["score"][0]["english"] > max_english_score:
                max_english_score = stu_i["score"][0]["english"]
            if stu_i["score"][0]["math"] < min_math_score:
                min_math_score = stu_i["score"][0]["math"]
            if stu_i["score"][0]["english"] < min_english_score:
                min_english_score = stu_i["score"][0]["english"]

    math_temp = float(math_temp/len_temp)
    english_temp = float(english_temp/len_temp)
    print("班级数学均分：{:.2f}".format(math_temp))
    print("班级数学最高分：",max_math_score)
    print("班级数学最低分：",min_math_score)
    print("班级英语均分：{:.2f}".format(english_temp))
    print("班级英语最高分：", max_english_score)
    print("班级英语最低分：", min_english_score)
    input("按下enter键返回菜单")
    print_menu()
"""修改学生信息"""
def deal_student():
    clean_screen()
    global class_info
    if len(class_info) == 0:
        print("列表为空，无法查找")
    else:
        temp = input("请输入要查询的学号：")
        for stu_i in class_info:
            if stu_i["ID"] == temp:
                print("查找成功")
                print("可以开始修改该同学的成绩：")
                print("1.姓名\t2.数学成绩\t3.英语成绩")
                choose = int(input("你想修改哪一项："))
                if choose == 1:
                    name=input("请输入你想要修改的姓名：")
                    stu_i["Name"] = name
                elif choose ==2:
                    math_score = int(input("请输入你想要修改的数学成绩："))
                    stu_i["score"][0]["math"] = math_score
                elif choose ==3:
                    english_score = int(input("请输入你想要修改的英语成绩："))
                    stu_i["score"][0]["english"] = english_score
                print("修改成功")
                write_stu()
                time.sleep(2)
                print_menu()
                return
        print("未找到")
    time.sleep(2)
    print_menu()
"""读取学生信息"""
def read_stu():
    global class_info
    with open(r"C:\Users\刘晗阳\PycharmProjects\PythonProject2\student_system\stu.txt", 'r', encoding='utf-8') as file:
        for line in file:
            words=line.strip().split()
            stu_score=[]
            score = {
                "math": int(words[2]),
                "english": int(words[3])
            }
            stu_score.append(score)
            student = {
                "Name": words[1],
                "ID": words[0],
                "score": stu_score
            }
            class_info.append(student)
"""将学生信息写入txt"""
def write_stu():
    global class_info
    with open(r"C:\Users\刘晗阳\PycharmProjects\PythonProject2\student_system\stu.txt", 'w', encoding='utf-8') as file:
        for stu_i in class_info:
            file.write(stu_i["ID"]+" ")
            file.write(stu_i["Name"]+" ")
            file.write(str(stu_i["score"][0]["math"])+" ")
            file.write(str(stu_i["score"][0]["english"]))
            file.write("\n")

def main():
    while True:
        print_menu()

        choose = int(input("请输入您需要的功能:\n"))

        if choose == 1 :
            add_student()
        elif choose == 2:
            find_student()
        elif choose == 3:
            deal_student()
        elif choose ==4:
            remove_student()
        elif choose ==5:
            display_student()
        elif choose ==6:
            display_class()
        else:
            return

read_stu()
main()