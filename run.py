import 邮箱数据
import 过去
import 排序
import email_fof
import os
import pandas as pd
import warnings
from apscheduler.schedulers.blocking import BlockingScheduler


path=r'C:\Users\Administrator\Desktop\每日净值.csv'
path1=r'C:\Users\Administrator\Desktop\每日净值_ready.csv'

def f1():
    email_fof.f1()
    邮箱数据.f1()
    os.remove(path)
    os.remove(path1)

def f2():
    email_fof.f2()
    邮箱数据.f2()
    os.remove(path)
    os.remove(path1)

def f3():
    email_fof.f3()
    邮箱数据.f3()
    os.remove(path)
    os.remove(path1)

def f4():
    email_fof.f4()
    邮箱数据.f4()
    os.remove(path)
    os.remove(path1)

def skf1():
    email_fof.f1()
    邮箱数据.skf1()
    os.remove(path)
    os.remove(path1)

def skf2():
    email_fof.f2()
    邮箱数据.skf2()
    os.remove(path)
    os.remove(path1)

def skf3():
    email_fof.f3()
    邮箱数据.skf3()
    os.remove(path)
    os.remove(path1)

def skf4():
    email_fof.f4()
    邮箱数据.skf4()
    os.remove(path)
    os.remove(path1)

def main():
    f1()
    f2()
    f3()
    f4()
    return 
def skmain():
    skf1()
    skf2()
    skf3()
    skf4()

def sort():
    排序.sort_data('华睿稳健FOF一号净值')
    排序.sort_data('匠燃进取FOF一号')
    排序.sort_data('轩哥六号')
    排序.sort_data('华云琢玉fof一号')

def findf1(past):
    过去.f1(past)
    排序.normal_sort('华睿稳健FOF一号净值')
    邮箱数据.f1()
    os.remove(path)
    os.remove(path1)
    排序.normal_sort('华睿稳健FOF一号净值')

def findf2(past):
    过去.f2(past)
    排序.normal_sort('匠燃进取FOF一号')
    邮箱数据.f2()
    os.remove(path)
    os.remove(path1)
    排序.normal_sort('匠燃进取FOF一号')

def findf3(past):
    过去.f3(past)
    排序.normal_sort('轩哥六号')
    邮箱数据.f3()
    os.remove(path)
    os.remove(path1)
    排序.normal_sort('轩哥六号')

def findf4(past):
    过去.f4(past)
    排序.normal_sort('华云琢玉fof一号')
    邮箱数据.f4()
    os.remove(path)
    os.remove(path1)
    排序.normal_sort('华云琢玉fof一号')

def skfindf1(past):
    过去.f1(past)
    排序.sk1_sort('华睿稳健FOF一号净值')
    邮箱数据.skf1()
    os.remove(path)
    os.remove(path1)

def skfindf2(past):
    过去.f2(past)
    排序.sk2_sort('匠燃进取FOF一号')
    邮箱数据.skf2()
    os.remove(path)
    os.remove(path1)

def skfindf3(past):
    过去.f3(past)
    排序.sk3_sort('轩哥六号')
    邮箱数据.skf3()
    os.remove(path)
    os.remove(path1)

def skfindf4(past):
    过去.f4(past)
    排序.sk4_sort('华云琢玉fof一号')
    邮箱数据.skf4()
    os.remove(path)
    os.remove(path1)

def skpf1():
    skfindf1(1)
    skfindf1(2)
    #skfindf1(3)
    #skfindf1(4)
    #skfindf1(5)

def skpf2():
    skfindf2(1)
    skfindf2(2)
    skfindf2(3)
    skfindf2(4)
    skfindf2(5)

def skpf3():
    skfindf3(1)
    skfindf3(2)
    skfindf3(3)
    skfindf3(4)
    skfindf3(5)

def skpf4():
    skfindf4(1)
    skfindf4(2)
    #skfindf4(3)
    #skfindf4(4)
    #skfindf4(5)


def pf1():
    
    findf1(1)
    
def pf2():
    findf2(1)
    
def pf3():
    findf3(1)
    
def pf4():
    findf4(1)
    findf4(2)
    findf4(3)
    findf4(4)
    
   



scheduler=BlockingScheduler()
scheduler.add_job(main,'interval',minutes=20) 

if __name__ == "__main__":
    skmain()
    #skpf1()
    #skf4()
    # skf4()       